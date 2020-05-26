// npm i -D postcss-loader

module.exports = {
	module: {
		rules: [
			{
				test: /\.css$/,
				use: [ 'style-loader', 'postcss-loader' ] // postcss.config.js
			},
			
			// another:
			{
				test: /\.s[ac]ss$/i,
				use: [
					'style-loader',
					{ loader: 'css-loader', options: { importLoaders: 1 } },
					{ loader: 'postcss-loader', options: {plugins: [require('autoprefixer'),require('rtlcss')]} },
					'sass-loader',
				],
			},
		],
	},
};