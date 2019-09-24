'use strict';

const serialize = require('serialize-javascript');

const CLIENT_ENV_KEYS = ['API_URL']

const processEnv = () =>
  CLIENT_ENV_KEYS.reduce((acc, key) => {
    acc[key] = serialize(process.env[key])
    return acc
  }, {})


module.exports = {
  plugins: ['typescript'],
  modify: (config, { target }, webpack) => {
    if (config.devServer) {
      // Handle HMR within docker env: https://github.com/jaredpalmer/razzle/issues/416
      config.devServer.watchOptions['poll'] = 1000;
      config.devServer.watchOptions['aggregateTimeout'] = 300;
    }

    if (target === 'web') {
      config.plugins = [
        ...config.plugins,
        new webpack.DefinePlugin({
          'process.env': processEnv()
        })
      ]
    }

    return config
  }
}