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
        template: './qr_code_component/qr-code-component-main/index.html',
        filename: 'qr-code-component.html'
    }),
    new HtmlWebpackPlugin({
        template: './blog_preview_card/blog-preview-card-main/index.html',
        filename: 'blog-preview-card.html'
    }),
  ],
};