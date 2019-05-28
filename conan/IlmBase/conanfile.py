import os
from conans import ConanFile, CMake, tools, RunEnvironment


class IlmBaseConan(ConanFile):
    name = "IlmBase"
    description = "IlmBase is a component of OpenEXR. OpenEXR is a high dynamic-range (HDR) image file format developed by Industrial Light & Magic for use in computer imaging applications."
    version = "2.2.1"
    license = "BSD"
    url = "https://github.com/openexr/openexr"
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_paths"
    exports = "FindIlmBase.cmake", "*.tar.gz"

    def requirements(self):
        if self.settings.os == "Windows":
            # On linux we rely on the system zlib library
            self.requires('zlib/1.2.11@conan/stable')

    def source(self):
        base = "openexr-{version}.tar.gz".format(version=self.version)
        if os.path.exists(base):
            self.output.info("Found local source tarball {}".format(base))
            tools.unzip(base)
        else:
            url = "https://github.com/openexr/openexr/archive/v{version}/".format(version=self.version) + base
            self.output.warn("Downloading source tarball {}".format(url))
            tools.get(url)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions['CMAKE_TOOLCHAIN_FILE'] = 'conan_paths.cmake'
        cmake.definitions["OPENEXR_BUILD_ILMBASE"] = "ON"
        cmake.definitions["OPENEXR_BUILD_OPENEXR"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_PYTHON_LIBS"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_UTILS"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_VIEWERS"] = "OFF"
        cmake.definitions["OPENEXR_BUILD_TESTS"] = "OFF"
        cmake.configure(source_folder="openexr-{version}/IlmBase".format(version=self.version))
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy("FindIlmBase.cmake")
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        parsed_version = self.version.split('.')
        version_suffix = "-%s_%s" % (parsed_version[0], parsed_version[1])

        if self.settings.os == "Windows":
            self.cpp_info.defines.append("OPENEXR_DLL")
        else:
            self.cpp_info.cppflags = ["-pthread"]

        self.cpp_info.includedirs = ['include', 'include/OpenEXR']
        self.cpp_info.libs = ["Imath" + version_suffix, "IexMath" + version_suffix, "Half", "Iex" + version_suffix,
                              "IlmThread" + version_suffix]
