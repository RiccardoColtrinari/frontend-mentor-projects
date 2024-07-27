# How to add new projects

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