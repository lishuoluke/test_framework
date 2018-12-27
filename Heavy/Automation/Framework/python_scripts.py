import importlib
import sys

import generate_test_result_file as gtrf
from test_scripts_base import TestScriptsBase


class PythonScripts(TestScriptsBase):
    def __init__(self):
        super(PythonScripts, self).__init__(__file__)

        sys.path.insert(0, self.config.testSuitePath)

    def runScript(self, script):
        mod = importlib.import_module(script['filename'])
        testScript = mod.TestScript()
        testScript.main()

        # Check whether to generate test result file.
        if (script['caseId'] != 0):
            gtrf.generateTestResultFile(script['caseId'], testScript.statusId,
                                        self.config.softwareVersion, testScript.comment)
        return (testScript.statusId == 1)


if (__name__ == '__main__'):
    pythonScripts = PythonScripts()
    pythonScripts.run()
    pythonScripts.uninit()
