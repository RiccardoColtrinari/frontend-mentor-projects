# Usage ./create-project.py project_name path_to_project_files (opt) path_to_design_files (opt)
import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Union

import click

from jinja2 import Environment, PackageLoader

from constants import PROJECTS_FOLDER_PATH


@dataclass
class Color:
    variable_name: str
    value: str


def init_npm(project_path: Path):
    print("Running command 'npm init -y'...")
    subprocess.run(["npm", "init", "-y"], stdout=subprocess.DEVNULL)

    package_json_file = project_path / "package.json"

    with package_json_file.open('r') as fp:
        package_json = json.load(fp)

    print("Customizing generated 'package.json' file...")

    project_name = project_path.name

    package_json['name'] = project_name
    package_json['main'] = "index.html"
    package_json["scripts"] = {
        "tailwind:watch": f"npx tailwindcss -i ./src/styles.css -o ./src/{project_name}.css --watch",
        "tailwind:build": f"npx tailwindcss -i ./src/styles.css -o ./src/{project_name}.css",
    }
    package_json["author"] = "Riccardo Coltrinari"
    package_json["description"] = f"{project_name.replace('-', ' ').capitalize()} challenge for frontendmentor."

    with package_json_file.open('w') as fp:
        json.dump(package_json, fp, indent=4)

    print("Correctly modified 'package.json' file.")


def get_colors(project_path: Path) -> Union[List[Color], None]:
    print("Trying to extract colors from style guides.")
    style_guide_path = project_path / 'design/style-guide.md'

    if not style_guide_path.exists():
        print(f"File not found: '{str(style_guide_path)}'.")
        return None

    with style_guide_path.open('r') as fp:
        style_guide_content = fp.readlines()

    colors_start_index = -1
    colors_end_index = -1

    for index, line in enumerate(style_guide_content):
        if colors_start_index == -1 and "colors" not in line.lower():
            continue

        if colors_start_index == -1:
            colors_start_index = index if style_guide_content[index + 1] != '\n' else index + 2
            continue

        if index > colors_start_index and line == '\n':
            colors_end_index = index
            break

        if '#' in line:
            colors_start_index = -1
            colors_end_index = -1
            break

    if colors_start_index == -1 or colors_end_index == -1:
        print("End colors extraction process with no color found.")
        return None

    colors = style_guide_content[colors_start_index:colors_end_index]

    colors = [color.replace('-', '').strip().split(':') for color in colors]

    print(f"End colors extraction process with {len(colors)} color{'s' if len(colors) > 1 else ''} found.")

    return [Color(color[0].replace(' ', '-').lower(), color[1].strip()) for color in colors]


def add_tailwind_config_js(project_path: Path):
    tailwind_config_js_path = project_path / "tailwind.config.js"

    if tailwind_config_js_path.exists():
        print("Cannot generate 'tailwind.config.js', already existing file!")
        return

    print("Running command 'npm install -D tailwindcss'...")
    subprocess.run(["npm", "install", "-D tailwindcss"], stdout=subprocess.DEVNULL)

    env = Environment(loader=PackageLoader('init-tailwind'))

    tailwind_config_js_template = env.get_template('tailwind.config.js.jinja2')

    colors = get_colors(project_path)

    print("Rendering 'tailwind.config.js' file...")

    tailwind_config_js_content = tailwind_config_js_template.render({
        'colors': colors
    })

    with tailwind_config_js_path.open('w') as fp:
        fp.write(tailwind_config_js_content)

    print("Correctly generated 'tailwind.config.js' file...")


def add_styles_css(project_path: Path) -> None:
    src_path = project_path / "src"

    if not src_path.exists():
        print("Creating folder 'src'...")
        src_path.mkdir()

    styles_css_path = src_path / 'styles.css'

    if styles_css_path.exists():
        print(f"'styles.css' already exists in the 'src' folder!")
        return

    with styles_css_path.open('w') as fp:
        fp.write("""@tailwind base;
@tailwind components;
@tailwind utilities;
        """)

    print("File 'styles.css' correctly generated in the 'src' folder.")


def modify_index_html(project_path: Path) -> None:
    index_html_path = project_path / "index.html"

    print(f"Modifying '{str(index_html_path)}' file.")

    if not index_html_path.exists():
        print(f"File not found: '{str(index_html_path)}'.")
        return

    with index_html_path.open('r') as file:
        index_html = file.read()

    insert_line = f'  <link href="./src/{project_path.name}.css" rel="stylesheet">'

    if insert_line in index_html:
        print(f"Line '{insert_line}' already contained in the '{str(index_html_path)}' file.")
        return

    new_index_html = index_html.replace('</head>', f'{insert_line}\n</head>')

    with index_html_path.open('w') as file:
        file.write(new_index_html)

    print(f"Correctly modified '{str(index_html_path)}' file.")


def initialize_tailwind(project_path: Path):
    init_npm(project_path)

    add_tailwind_config_js(project_path)

    add_styles_css(project_path)

    print("Running command 'npm run tailwind:build'...")
    subprocess.run(["npm", "run", "tailwind:build"], stdout=subprocess.DEVNULL)

    modify_index_html(project_path)


@click.command()
@click.argument('project_name')
def main(
        project_name: str
):
    project_path = PROJECTS_FOLDER_PATH / project_name

    if not project_path.exists():
        print(f"Project {project_name} does not exist! Create it before initializing tailwind!")
        return

    current_workdir = os.getcwd()
    os.chdir(project_path)

    initialize_tailwind(project_path)

    os.chdir(current_workdir)

    print("Tailwind initialization completed.")


if __name__ == "__main__":
    main()
