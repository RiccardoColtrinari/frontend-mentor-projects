#!/bin/bash

# Usage: source p.sh PROJECT_NAME SOURCES_DIRECTORY FIGMA_DIRECTORY(Optional)

activate() {
	source venv/bin/activate
}

usage() {
	echo ""
	echo "Usage: source p.sh PROJECT_NAME SOURCES_DIRECTORY FIGMA_DIRECTORY(Optional)"
}

show_header() {
	command=$*
	echo ""
	echo "------------- Running Command '$command' -------------"
	echo ""
}

PROJECT_NAME=${1:?"Mandatory PROJECT_NAME not found!"}
SOURCES_DIRECTORY=${2:?"Mandatory SOURCES_DIRECTORY not found!"}
FIGMA_DIRECTORY=$3

if [[ -z $PROJECT_NAME || -z $SOURCES_DIRECTORY ]]; then
	usage
	return
fi

create_project_input="$PROJECT_NAME $SOURCES_DIRECTORY"

if [[ -n $FIGMA_DIRECTORY ]]; then
	create_project_input="-f $FIGMA_DIRECTORY $create_project_input"
fi

create_project_script="create-project.py $create_project_input"

init_tailwind_script="init-tailwind.py $PROJECT_NAME"

add_project_script="add-project.py $PROJECT_NAME"

activate

show_header $create_project_script
python $create_project_script

show_header $init_tailwind_script
python $init_tailwind_script

show_header $add_project_script
python $add_project_script


deactivate