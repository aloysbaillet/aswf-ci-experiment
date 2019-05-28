from conans import ConanFile, tools, RunEnvironment
import os


class NumpyConan(ConanFile):
    name = "numpy"
    description = "NumPy is the fundamental package needed for scientific computing with Python."
    version = "1.12.1"
    license = "LGPL"
    url = "https://wiki.qt.io/Qt_for_Python"
    settings = "os", "compiler", "build_type", "arch", "python"
    exports = "*.tar.gz"

    def source(self):
        base = "numpy-{version}.tar.gz".format(version=self.version)
        if os.path.exists(base):
            self.output.info("Found local source tarball {}".format(base))
            tools.unzip(base)
        else:
            url = "https://github.com/numpy/numpy/releases/download/v{version}/".format(version=self.version) + base
            self.output.warn("Downloading source tarball {}".format(url))
            tools.get(url)

    def build(self):
        if self.settings.os == "Windows":
            pypath = os.path.join(self.package_folder, 'Lib/site-packages')
        else:
            pypath = os.path.join(self.package_folder, 'lib64/python2.7/site-packages')
        os.makedirs(pypath)
        with tools.environment_append({'PYTHONPATH': pypath}):
            self.run('python setup.py build -j 4 install --prefix {}'.format(self.package_folder),
                     cwd='numpy-1.12.1')

    def package(self):
        self.copy("*.egg")

    def package_info(self):
        if self.settings.os == "Windows":
            self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'Lib/site-packages'))
        else:
            self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'lib64/python2.7/site-packages'))
