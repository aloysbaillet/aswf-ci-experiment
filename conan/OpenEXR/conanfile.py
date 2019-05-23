from conans import ConanFile, CMake, RunEnvironment, tools
import os


class OpenEXRConan(ConanFile):
    name = "OpenEXR"
    description = "OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial Light & " \
                  "Magic for use in computer imaging applications."
    version = "2.2.1"
    license = "BSD"
    url = "https://github.com/openexr/openexr"
    settings = "os", "compiler", "build_type", "arch", "cppstd"
    generators = "cmake_find_package"
    exports_sources = "OpenEXR/*", "cmake/FindOpenEXR.cmake", "CMakeLists.txt", "LICENSE"

    def requirements(self):
        self.requires('IlmBase/2.2.1@aswf/vfx2018')

    def source(self):
        base = "openexr-{version}.tar.gz".format(version=self.version)
        if os.path.exists(base):
            self.output.info("Found local source tarball {}".format(base))
            tools.unzip(base)
        else:
            url = "https://github.com/openexr/openexr/releases/download/v{version}/".format(version=self.version) + base
            self.output.warn("Downloading source tarball {}".format(url))
            tools.get(url)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["OPENEXR_BUILD_ILMBASE"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_OPENEXR"] = "ON"
        cmake.definitions["OPENEXR_BUILD_PYTHON_LIBS"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_UTILS"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_VIEWERS"] = "OFF"
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        with tools.environment_append(RunEnvironment(self).vars): # needed by dwaLookups during build and the tests
            cmake.build()
            cmake.test()

    def package(self):
        self.copy("FindOpenEXR.cmake", src="cmake", keep_path=False)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ['include', os.path.join('include', 'OpenEXR')]
        self.cpp_info.libs = ['IlmImf', 'IlmImfUtil']
