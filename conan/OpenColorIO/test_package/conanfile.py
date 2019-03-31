from conans import ConanFile, tools
import os


class PyOpenColorIOTester(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    requires = "OpenColorIO/1.0.9@aswf/vfx2018"

    def test(self):
        testfile = os.path.join(self.source_folder, 'test_ocio.py')
        self.run('/usr/bin/python2.7 %s'%testfile, run_environment=True)
