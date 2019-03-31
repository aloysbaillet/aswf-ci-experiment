from conans import ConanFile, tools
import os


class PySideTester(ConanFile):
    settings = "os", "compiler", "arch", "build_type"

    def test(self):
        testfile = os.path.join(self.source_folder, 'test_pyside.py')
        self.run('/usr/bin/python2.7 %s'%testfile, run_environment=True)
