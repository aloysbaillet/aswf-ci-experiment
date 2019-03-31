
import os, glob

from conans import ConanFile, tools, CMake


class OpenColorIOConan(ConanFile):
    name = "OpenColorIO"
    description = "OpenColorIO is a component of OpenEXR. OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial Light & Magic for use in computer imaging applications."
    version = "1.0.9"
    license = "BSD"
    url = "https://github.com/Mikayex/conan-OpenColorIO.git"
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    exports = "*.tar.gz"

    def source(self):
        base = "OpenColorIO-{version}.tar.gz".format(version=self.version)
        if os.path.exists(base):
            self.output.info("Found local source tarball {}".format(base))
            tools.unzip(base)
        else:
            url = "https://github.com/imageworks/OpenColorIO/archive/v{version}.tar.gz".format(version=self.version)
            self.output.warn("Downloading source tarball {}".format(url))
            tools.get(url)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="OpenColorIO-{version}".format(version=self.version))
        cmake.definitions["OCIO_BUILD_TRUELIGHT"] = "OFF"
        cmake.definitions["OCIO_BUILD_NUKE"] = "OFF"
        return cmake
    
    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include']
        self.cpp_info.libs = ['OpenColorIO']
        self.env_info.PYTHONPATH.append(os.path.join(self.package_folder, 'lib/python2.7/site-packages'))
