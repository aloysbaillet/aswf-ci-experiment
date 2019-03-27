from conans import ConanFile, tools
import os


class NumpyTester(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    requires = "numpy/1.12.1@aswf/vfx2018"

    def test(self):
        testfile = os.path.join(self.source_folder, 'test_numpy.py')
        self.run('/usr/bin/python2.7 %s'%testfile, run_environment=True)
