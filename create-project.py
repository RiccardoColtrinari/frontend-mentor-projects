# Usage ./create-project.py project_name path_to_project_files (opt) path_to_design_files (opt)

from pathlib import Path
import click
import os


PROJECTS_FOLDER_NAME = "projects"

PROJECTS_FOLDER_PATH = Path(PROJECTS_FOLDER_NAME).resolve()
assert PROJECTS_FOLDER_PATH.exists(), f"The '{PROJECTS_FOLDER_NAME}' folder must be available in the current directory!"


def create_from_sources(project_folder_path: Path, sources_dir: Path):
    sources_dir.rename(project_folder_path)


def handle_figma_sources(project_design_folder_path: Path, figma_dir: Path) -> None:
    figma_dir.rename(project_design_folder_path / "figma")


def handle_design_resources(project_folder_path: Path, figma_dir: Path = None):
    PROJECT_DESIGN_FOLDER_PATH = project_folder_path / "design"

    if not PROJECT_DESIGN_FOLDER_PATH.exists():
        print(f"Unable to handle design files! Cannot find the '{PROJECT_DESIGN_FOLDER_PATH.name}' folder in the "
              "project directory!")
        return

    resources_files = ["style-guide.md", "README-template.md"]

    resources_paths = [project_folder_path / filename for filename in resources_files]

    for resource_path in resources_paths:
        resource_name = resource_path.name

        if not resource_path.exists():
            print(f"File not found! Cannot move {resource_name} into the '{PROJECT_DESIGN_FOLDER_PATH}' folder")
            continue

        resource_path.rename(PROJECT_DESIGN_FOLDER_PATH / resource_path.name)

        print(f"File {resource_name} successfully moved into the {PROJECT_DESIGN_FOLDER_PATH} folder!")

    if figma_dir:
        handle_figma_sources(PROJECT_DESIGN_FOLDER_PATH, figma_dir)
        print("Figma folder successfully moved!")
    else:
        print("No figma folder given!")



def create_structure(project_name: str, sources_dir: Path = None, figma_dir: Path = None):
    project_folder_path = PROJECTS_FOLDER_PATH / project_name

    assert not project_folder_path.exists(), f"Project '{project_name}' already existing in the '{PROJECTS_FOLDER_NAME}' folder!"

    if not sources_dir:
        project_folder_path.mkdir()
        print(f"Empty project {project_name} created successfully!")
        return

    create_from_sources(project_folder_path, sources_dir)
    print(f"'{project_name}' project successfully initialized with source directory content!")

    handle_design_resources(project_folder_path, figma_dir)
    print("Design files successfully handled!")


@click.command()
@click.argument('project_name')
@click.option('--sources-dir', '-s', default=None, type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=Path), help="(Optional) Directory containing project source code. When passed its content is extracted and put into the project folder.")
@click.option('--figma-dir', '-f', default=None, type=click.Path(exists=True, file_okay=False, resolve_path=True, path_type=Path), help="(Optional) Directory containing project figma design. When passed its content is extracted and put into the 'design' folder of the project.")
def main(
    project_name: str,
    sources_dir: Path,
    figma_dir: Path
):
    current_workdir = os.getcwd()
    os.chdir(PROJECTS_FOLDER_PATH)

    create_structure(project_name, sources_dir, figma_dir)

    os.chdir(current_workdir)


if __name__ == "__main__":
    main()
