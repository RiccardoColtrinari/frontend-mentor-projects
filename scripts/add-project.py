import click

from constants import PROJECTS_FOLDER_PATH, WORKDIR


def add_project_to_index_html(project_name: str) -> None:
    index_html_path = WORKDIR / "index.html"

    print(f"Modifying '{str(index_html_path)}' file.")

    if not index_html_path.exists():
        print(f"File not found: '{str(index_html_path)}'.")
        return

    with index_html_path.open('r') as file:
        index_html = file.read()

    capitalized_project_name = ' '.join([word.capitalize() for word in project_name.split('-')])

    to_search_line = "        <!-- PROJECTS LIST -->"

    insert_line = f'        <li><a href="./{project_name}.html">{capitalized_project_name}</a></li>\n{to_search_line}'

    if to_search_line not in index_html:
        print(f"Cannot find line '{to_search_line}' in the '{str(index_html_path)}' file.")
        return

    if project_name in index_html:
        print(f"Project '{project_name}' already contained in the '{str(index_html_path)}' file.")
        return

    new_index_html = index_html.replace(to_search_line, insert_line)

    with index_html_path.open('w') as file:
        file.write(new_index_html)

    print(f"Correctly added project {project_name} in the '{str(index_html_path)}' file.")


def add_project_to_webpack_config(project_name: str) -> None:
    webpack_config_path = WORKDIR / "webpack.config.js"

    print(f"Modifying '{str(webpack_config_path)}' file.")

    if not webpack_config_path.exists():
        print(f"File not found: '{str(webpack_config_path)}'.")
        return

    with webpack_config_path.open('r') as file:
        webpack_config = file.read()

    to_search_line = "    //  PROJECTS LIST"

    insert_line = f"""    new HtmlWebpackPlugin({{
        template: './projects/{project_name}/index.html',
        filename: '{project_name}.html'
    }}),\n{to_search_line}"""

    if to_search_line not in webpack_config:
        print(f"Cannot find line '{to_search_line}' in the '{str(webpack_config_path)}' file.")
        return

    if project_name in webpack_config:
        print(f"Project '{project_name}' already contained in the '{str(webpack_config_path)}' file.")
        return

    new_index_html = webpack_config.replace(to_search_line, insert_line)

    with webpack_config_path.open('w') as file:
        file.write(new_index_html)

    print(f"Correctly added project {project_name} in the '{str(webpack_config_path)}' file.")


@click.command()
@click.argument('project_name', type=str)
def main(
        project_name: str
):
    """
    PROJECT_NAME: The name of the project to add in the homepage.
    """

    project_path = PROJECTS_FOLDER_PATH / project_name
    assert project_path.exists(), f"Project {project_name} does not exists in the '{PROJECTS_FOLDER_PATH}' folder!"

    add_project_to_index_html(project_name)

    add_project_to_webpack_config(project_name)

    print(f"Project {project_name} correctly added to the homepage!")


if __name__ == '__main__':
    main()
