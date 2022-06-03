from testsuite.testsuite import TestSuiteMaze


def load_suite(filename):
    return TestSuiteMaze.from_json_file(filename)


def load_suites(filenames: list):
    suites = []
    for fname in filenames:
        suites.append(load_suite(fname))

    return suites

suite_files = [
    "./suites/suite_1.json",
]

suites = load_suites(suite_files)

for suite in suites:
    suite.run()
    print("### Suite %s complete")