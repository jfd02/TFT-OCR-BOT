const
  path    = require('path'),
  fs      = require('fs'),
  semver  = require('semver'),
  zip     = require('zip-a-folder');

const handleErrors = (error, compilation) => {
  error = new Error(error)
  compilation.errors.push(error);
  throw error;
};

const PluginName = 'OverwolfPlugin';

module.exports = class OverwolfPlugin {
  constructor(env) {
    this.env = env
  }
  apply(compiler) {
    compiler.hooks.run.tapPromise(PluginName, async (compilation) => {
      try {
        const newVersion = this.env.setVersion;

        if ( newVersion && semver.valid(newVersion) )
          await this.setVersion(newVersion);
      } catch(e) {
        handleErrors(e, compilation);
      }
    });
    compiler.hooks.afterEmit.tapPromise(PluginName, async (compilation) => {
      try {
        const makeOpk = this.env.makeOpk;

        if ( makeOpk )
          await this.makeOPK(( typeof makeOpk === 'string' ) ? makeOpk : '');
      } catch(e) {
        handleErrors(e, compilation);
      }
    });
  }

  async makeOPK(suffix = '') {
    const
      packagePath = path.resolve(__dirname, './package.json'),
      manifestPath = path.resolve(__dirname, './public/manifest.json'),
      dist = path.join(__dirname, 'dist/');

    const [
      pkg,
      manifest
    ] = await Promise.all([
      this.readFile(packagePath),
      this.readFile(manifestPath)
    ]);

    if ( !pkg )
      throw 'could not read package.json';

    if ( !manifest )
      throw 'could not read manifest.json';

    const
      version = pkg.version,
      name = "TFT-Scout",
      opkPath = path.join(__dirname, `releases/${name}-${version}${(suffix) ? `.${suffix}` : ''}.opk`);

    await this.deleteFile(opkPath);
    await zip.zip(dist, opkPath);
  }

  async setVersion(newVersion) {
    const
      packagePath = path.resolve(__dirname, './package.json'),
      manifestPath = path.resolve(__dirname, './public/manifest.json');

    const [
      pkg,
      manifest
    ] = await Promise.all([
      this.readFile(packagePath),
      this.readFile(manifestPath)
    ]);

    if ( !pkg )
      throw 'could not read package.json';

    if ( !manifest )
      throw 'could not read manifest.json';

    pkg.version = newVersion;
    manifest.meta.version = newVersion;

    const
      pkgJSON = JSON.stringify(pkg, null, '  '),
      manifestJSON = JSON.stringify(manifest, null, '  ');

    await Promise.all([
      this.writeFile(packagePath, pkgJSON),
      this.writeFile(manifestPath, manifestJSON)
    ]);
  }

  readFile(filePath) { return new Promise(resolve => {
    fs.readFile(filePath, (err, response) => {
      try {
        if ( err )
          resolve(null);
        else
          resolve(JSON.parse(response));
      } catch(e) {
        resolve(null);
      }
    });
  })}

  writeFile(filePath, content) { return new Promise(resolve => {
    fs.writeFile(filePath, content, resolve);
  })}

  deleteFile(filePath) { return new Promise(resolve => {
    fs.unlink(filePath, resolve);
  })}
}