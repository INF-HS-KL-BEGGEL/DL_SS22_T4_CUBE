from deeplearning.testsuite.testsuite import TestSuiteMaze
import tensorflow as tf

physical_devices = tf.config.list_physical_devices('GPU')
for device in physical_devices:
    tf.config.experimental.set_memory_growth(device, True)


def load_suite(filename):
    return TestSuiteMaze.from_json_file(filename)


def load_suites(filenames: list):
    suites = []
    for fname in filenames:
        suites.append(load_suite(fname))

    return suites

suite_files = [
    "/suites/suite_1.json",
]

suites = load_suites(suite_files)

for suite in suites:
    suite.run()
    print("### Suite %s complete")