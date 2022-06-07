from deeplearning.testsuite.testsuite import TestSuiteMaze
import tensorflow as tf
import os, glob

physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)


class TestRunner:

    def __init__(self):
        self.suitepath = os.getenv("SUITEPATH", "./suites/")
        self.filenames = self._get_filenames_from_path()

    def _load_suites(self, filenames: list):
        suites = []
        for fname in filenames:
            suites.append(TestSuiteMaze.from_json_file(fname))

        return suites

    def start(self):

        print(self.suitepath)
        suites = self._load_suites(self.filenames)

        for suite in suites:
            print("### Run Suite %s complete" % suite.get_name())
            suite.run()

    def _get_filenames_from_path(self, path="./suites/"):
        return glob.glob(path + "*.json")


testrunner = TestRunner()
testrunner.start()