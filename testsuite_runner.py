from deeplearning.testsuite.testsuite import TestSuiteMaze
import tensorflow as tf
import os, glob

physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)


def load_suite(filename):
    print(filename)
    return TestSuiteMaze.from_json_file(filename)


def load_suites(filenames: list):
    suites = []
    for fname in filenames:
        suites.append(load_suite(fname))

    return suites


def get_files_from_path(path="./suites/"):
    return glob.glob("path*")

suite_files = get_files_from_path(os.getenv("SUITEPATH", "./suites/"))
suites = load_suites(suite_files)


for suite in suites:
    print("### Run Suite %s complete" % suite.get_name())
    suite.run()
