import os
import sys

import log_message as log
from python_scripts import PythonScripts
from test_automation_config import TestAutomationConfig
from test_result_files import TestResultFiles



class TestAutomation:
    def __init__(self):
        self.config = TestAutomationConfig()
        self.testResultFiles = TestResultFiles()

        # To cleanup the test result folder before the run.
        self.testResultFiles.cleanup()

        # Add the reusable path.
        reusablePath = os.path.join(self.config.rootPath, 'reusable\\python')
        sys.path.insert(0, reusablePath)

    def uninit(self):
        self.testResultFiles.uninit()

        self.config = None
        self.testResultFiles = None



    def runTestSuite(self):
        try:
            log.logFnEntryExit(__file__, 'runTestSuite', 'begin')

            testScripts = None
            if (self.config.testPlatform == 'python'):
                testScripts = PythonScripts()
            else:
                raise Exception('Unknown test platform')

            testScripts.main()
            testScripts.uninit()
            log.logFnEntryExit(__file__, 'runTestSuite', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'runTestSuite', ex)
            return False

    def generateTestResultReport(self):
        try:
            log.logFnEntryExit(__file__, 'generateTestResultReport', 'begin')

            success = self.testResultFiles.generateReport()

            log.logFnEntryExit(__file__, 'generateTestResultReport', 'end')
            return success

        except Exception as ex:
            log.logException(__file__, 'generateTestResultReport', ex)
            return False

    def backupTestResultFiles(self):
        try:
            log.logFnEntryExit(__file__, 'backupTestResults', 'begin')

            self.testResultFiles.backup()

            log.logFnEntryExit(__file__, 'backupTestResults', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'backupTestResults', ex)
            return False

    def main(self):
        log.delete()
        log.logFnEntryExit(__file__, 'main', '### Begin ###')

        if (self.config.runTestSuite):
            if (not self.runTestSuite()):
                exit()
            log.logProgress(__file__, 'main', 'after running test suite')

        if (self.config.generateTestResultReport):
            if (not self.generateTestResultReport()):
                exit()
            log.logProgress(__file__, 'main', 'after generating test result report')

        if (not testAutomation.backupTestResultFiles()):
            exit()
        log.logProgress(__file__, 'main', 'after backup test result files')

        log.logFnEntryExit(__file__, 'main', '### End ###')
        log.logEmptyLine()


if (__name__ == '__main__'):
    testAutomation = TestAutomation()
    testAutomation.main()
    testAutomation.uninit()
