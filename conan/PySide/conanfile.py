from conans import ConanFile, AutoToolsBuildEnvironment, RunEnvironment, tools
import os


class PySideConan(ConanFile):
    name = "PySide"
    description = "PySide is a high dynamic-range (HDR) image file format developed by Industrial Light & " \
                  "Magic for use in computer imaging applications."
    version = "2.2.0"
    license = "BSD"
    url = "https://github.com/jgsogo/conan-openexr.git"
    settings = "os", "compiler", "build_type", "arch", "python"
    exports = "*.tgz"

    def requirements(self):
        self.requires('Qt/5.6.1@aswf/vfx2018')

    def source(self):
        base = "PySide2-Maya2018Update5.tgz"
        if os.path.exists(base):
            self.output.info("Found local source tarball {}".format(base))
            tools.unzip(base)
        else:
            url = "https://www.autodesk.com/content/dam/autodesk/www/Company/files/" + base
            self.output.warn("Downloading source tarball {}".format(url))
            tools.get(url)

    def build(self):
        # with tools.environment_append(self.env):
        # pypath = os.path.join(self.package_folder, 'lib64/python2.7/site-packages')
        # os.makedirs(pypath)
        # with tools.environment_append({'PYTHONPATH': pypath}):
        self.run('python setup.py build install --prefix {}'.format(self.package_folder),
                 cwd='pyside-setup', run_environment=True)

    def package(self):
        self.copy("*.egg")

    def package_info(self):
        self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'lib64/python2.7/site-packages'))
