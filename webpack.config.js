const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
  entry: './index.html',
  mode: 'development',
  output: {
    path: path.resolve(__dirname, 'docs'),
  },
  module: {
    rules: [
        {
            test: /\.html$/,
            use: ['html-loader'],
        }
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
        template: './index.html',
        filename: 'index.html'
    }),
    new HtmlWebpackPlugin({
        template: './projects/qr-code-component/index.html',
        filename: 'qr-code-component.html'
    }),
    new HtmlWebpackPlugin({
        template: './projects/blog-preview-card/index.html',
        filename: 'blog-preview-card.html'
    }),
    new HtmlWebpackPlugin({
        template: './projects/social-links-profile/index.html',
        filename: 'social-links-profile.html'
    }),
    new HtmlWebpackPlugin({
        template: './projects/recipe-page/index.html',
        filename: 'recipe-page.html'
    }),
    //  PROJECTS LIST
  ],
};
