import time

import log_test_message as log
from python_script_base import PythonScriptBase


class TestScript(PythonScriptBase):
    def __init__(self):
        super(TestScript, self).__init__(__file__)

    def initialise(self):
        try:
            log.logFnEntryExit(__file__, 'initialise', 'begin')

            # Read configuration file.
            # Set up pre-conditions.

            log.logFnEntryExit(__file__, 'initialise', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'initialise', ex)
            return False

    def uninitialise(self):
        try:
            log.logFnEntryExit(__file__, 'uninitialise', 'begin')

            # Remove pre-conditions.
            # Scan logs for unexpected errors.
            # Set the test result (statusId) and comments.
            # statusId:
            # 1 = passed, 2 = blocked, 3 = untested, 4 = retest, 5 = failed.

            log.logFnEntryExit(__file__, 'uninitialise', 'end')

        except Exception as ex:
            log.logException(__file__, 'uninitialise', ex)

    def execute(self):
        try:
            log.logFnEntryExit(__file__, 'execute', 'begin')

            # Perform the actual test steps.

            time.sleep(5)  # Can be removed.

        except Exception as ex:
            log.logException(__file__, 'execute', ex)


if (__name__ == '__main__'):
    testScript = TestScript()
    testScript.main()
