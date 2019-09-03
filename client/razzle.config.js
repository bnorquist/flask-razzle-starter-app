'use strict';

const razzleHeroku = require('razzle-heroku');

module.exports = {
  plugins: ['typescript'],
  modify: (config, { target, dev }, webpack) => {
    config = razzleHeroku(config, {target, dev}, webpack);

    if (config.devServer) {
      // Handle HMR within docker env: https://github.com/jaredpalmer/razzle/issues/416
      config.devServer.watchOptions['poll'] = 1000;
      config.devServer.watchOptions['aggregateTimeout'] = 300;
    }

    return config
  }
}