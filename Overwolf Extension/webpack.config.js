const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');
const CopyPlugin = require("copy-webpack-plugin");
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const OverwolfPlugin = require('./overwolf.webpack');

module.exports = env => ({
    entry: {
        background: './src/background/background.ts',
        overlay: './src/overlay/overlay.ts',
    },
    devtool: 'inline-source-map',
    module: {
        rules: [
            {
                test: /\.ts?$/,
                use: 'ts-loader',
                exclude: /node_modules/
            }
        ]
    },
    resolve: {
        extensions: ['.ts', ".js"]
    },
    output: {
      path: `${__dirname}/dist`,
      filename: 'js/[name].js'
    },
    plugins: [
        new CleanWebpackPlugin,
        new CopyPlugin({
            patterns: [ { from: "public", to: "./" } ],
        }),
        new HtmlWebpackPlugin({
            template: './src/overlay/overlay.html',
            filename: `${__dirname}/dist/overlay.html`,
            chunks: ['overlay']
        }),
        new HtmlWebpackPlugin({
            template: './src/background/background.html',
            filename: `${__dirname}/dist/background.html`,
            chunks: ['overlay']
        }),
        new OverwolfPlugin(env)
    ]
});