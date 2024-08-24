# How to add new projects

## Manual Actions

This is a self reminder to correctly structure the projects in such a way that is correctly referenced by the main index page.

The ```projects``` directory stores each project.
After the download from frontend mentor extract the project in this directory.

Rename the ```{project_name}-main``` folder as ```{project_name}```, then move each design file into the ```design``` directory: ```{project_name-figma}```, if present; *style-guide.md*; *README-template.md*.

Last but not least, make sure to use a css file for the project that is named after the project itself: ```{project_name}.css```

**Adding the project to the showcase page:**

Finally make sure to add the project in the initial showcase page.

In the [index.html](./index.html) add a new link pointing to a still non-existing html, named after the project itself, as shown below:

```html
<a href="{project_name}.html"></a>
```

Even though this file does not exist, it will be created by webpack.

To do so add the following to the webpack plugin list:

```javascript
// ...
plugins: [
    new HtmlWebpackPlugin({
        template: './projects/{project_name}/index.html',
        filename: '{project_name}.html'
    }),
],
```

This will retrieve the html and all the linked files from the path defined in the *template* argument and it will create a file named as specified in the *filename* argument.

To avoid collisions in the css classes at runtime make sure that the project's css files are named after the project name.

## Automatism

To simplify operations there are several scripts in the ```scripts``` folder.

The ```init-project.sh``` in particular uses the others to create a pipeline that initializes a project starting by the frontend mentor sources.

To use it run the following command (make sure to use ```source```):

```shell
$ source init-project [PROJECT_NAME] [SOURCES_DIRECTORY] [FIGMA_DIRECTORY (Optional)] 
```

where:

- **PROJECT_NAME**: is the **mandatory** name of the project, the one that is used to store in the ```projects``` folder;
- **SOURCES_DIRECTORY**: is the **mandatory** path to the frontend mentor downloaded project sources;
- **FIGMA_DIRECTORY**: is the **optional** path to the frontend mentor downloaded figma sources;

The aforementioned script will run the following scripts sequentially:

- **create-project.py**: which sets up the project structure within the ```projects``` folder;
- **init-tailwind.py**: which sets up tailwind in the project together with any related css file;
- **add-project.py**: which adds the project to the ```index.html``` and ```webpack.config.js```, making it accessible from the showcase page.