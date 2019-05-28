from conans import ConanFile, tools
import os


class NumpyTester(ConanFile):
    settings = "os", "compiler", "arch", "build_type", "python"

    def test(self):
        testfile = os.path.join(self.source_folder, 'test_numpy.py')
        self.run('python2.7 %s'%testfile, run_environment=True)
