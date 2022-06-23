from deeplearning.testsuite.testsuite_maze import TestSuiteMaze
from deeplearning.testsuite.testsuite_cube import TestSuiteCube
from deeplearning.testsuite.testsuite_base import TestSuiteBase
import os, glob


class TestRunner:

    def __init__(self):
        self.suitepath = os.getenv("SUITEPATH", "./suites/")
        self.filenames = self._get_filenames_from_path()

    def _load_suites(self, filenames: list):
        suites = []
        for fname in filenames:
            suites.append(TestSuiteMaze.from_json_file(fname))
            suites.append(TestSuiteCube.from_json_file(fname))
        return suites

    def start(self):

        print(self.suitepath)
        print(self.filenames)
        suites = self._load_suites(self.filenames)
        print("---------------------------------------------------------")
        for suite in suites:
            if (not suite or suite.is_deactivated()):
                continue
            print("### Run Suite %s complete" % suite.get_name())
            print()
            suite.run()

    def _get_filenames_from_path(self, path="./suites/"):
        return glob.glob(path + "*.json")


testrunner = TestRunner()
testrunner.start()
