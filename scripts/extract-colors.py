import json
from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple

import click

from constants import PROJECTS_FOLDER_PATH, DESIGN_FOLDER_NAME, STYLE_GUIDE_FILENAME

# global var that can be changed by the -q option
# if set to false all yes_no_questions run with default choice
should_ask_questions: bool = True


@dataclass
class Color:
    variable_name: str
    value: str


def format_color(color: str) -> Color:
    color = color.replace('-', '').strip().split(':')
    return Color(color[0].replace(' ', '-').lower(), color[1].strip())


def get_colors_from_rows(project_path: Path, rows: List[int]) -> List[Color]:
    style_guide_path = project_path / DESIGN_FOLDER_NAME / STYLE_GUIDE_FILENAME

    if not style_guide_path.exists():
        print(f"File not found: '{str(style_guide_path)}'.")
        return []

    with style_guide_path.open('r') as fp:
        lines = fp.readlines()

    colors = []

    for row in rows:
        if row < 0 or row >= len(lines):
            print(f"Invalid row {row}!")
            continue

        colors.append(lines[row])

    colors = [format_color(color) for color in colors]

    print(f"End colors extraction process with {len(colors)} color{'s' if len(colors) > 1 else ''} found.")

    return colors


def ask_yes_no_question(question: str, default_choice: bool):
    if not should_ask_questions:
        return default_choice

    yes_value = "(y)" if default_choice == True else "y"
    no_value = "(n)" if default_choice == False else "n"

    yes_no_values = f"[{yes_value}/{no_value}]"

    while True:
        choice = input(f"{question} {yes_no_values}: ").strip().lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        elif not choice:
            return default_choice
        else:
            print(f"Invalid choice: {choice}!")


def double_check_color_names(colors: List[Color]):
    colors_keys = [color.variable_name for color in colors]
    print(f"These are the colors found {colors_keys}.")

    should_continue = ask_yes_no_question("Do you want to modify some name?", default_choice=False)

    if not should_continue:
        print(f"Saving colors: {colors_keys}")
        return

    for color in colors:
        color_name = color.variable_name

        should_modify_color = ask_yes_no_question(f"Do you want to modify the name '{color_name}'?",
                                                  default_choice=False)

        if not should_modify_color:
            continue

        while True:
            new_name = input(f"Insert a new name to replace '{color_name}': ")

            is_new_name_ok = ask_yes_no_question(f"Are you sure you want to change '{color_name}' with '{new_name}'?",
                                                 default_choice=True)

            if is_new_name_ok:
                color.variable_name = new_name
                break

    print(f"Saving colors: {[color.variable_name for color in colors]}")


@click.command()
@click.argument("project_name", type=str)
@click.argument("rows", nargs=-1, type=int)
@click.option('--no-questions', '-nq', is_flag=True, show_default=True, default=True,
              help="Disable questions during color processing. Every question fallback to default choice.")
def main(
        project_name: str,
        rows: Tuple[int],
        no_questions: bool
):
    """
    This script can be used to extract the colors from the style-guide.md.
    The output is made on stdout and no file is modified.

    PROJECT_NAME: The name of the project where you want to extract colors.

    ROWS: The comma-separated rows of the 'style-guide.md' file in which colors can be read.
    """
    global should_ask_questions
    should_ask_questions = no_questions

    project_path = PROJECTS_FOLDER_PATH / project_name
    assert project_path.exists(), f"Project {project_name} does not exists in the '{PROJECTS_FOLDER_PATH}' folder!"

    rows = [row - 1 for row in rows]

    colors = get_colors_from_rows(project_path, rows)

    double_check_color_names(colors)

    colors_dict = {
        "colors": {color.variable_name: color.value for color in colors}
    }

    print(f"\n------------ {project_name.capitalize()} Colors ------------\n")
    print(json.dumps(colors_dict, indent=4))

    print("\nYou can now copy and paste these into your tailwind.config.js")


if __name__ == '__main__':
    main()
