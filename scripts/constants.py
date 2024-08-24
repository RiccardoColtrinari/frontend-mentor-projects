from pathlib import Path

WORKDIR = Path('..').resolve()

PROJECTS_FOLDER_NAME = "projects"

PROJECTS_FOLDER_PATH = WORKDIR / PROJECTS_FOLDER_NAME
assert PROJECTS_FOLDER_PATH.exists(), f"The '{PROJECTS_FOLDER_NAME}' folder must be available in the '{WORKDIR}' directory!"

DESIGN_FOLDER_NAME = "design"

STYLE_GUIDE_FILENAME = 'style-guide.md'
