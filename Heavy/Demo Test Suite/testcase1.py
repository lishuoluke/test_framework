import log_test_message as log
from python_script_base import PythonScriptBase
from test_scripts_config import TestScriptsConfig



class TestScript(PythonScriptBase):
    def __init__(self):
        super(TestScript, self).__init__(__file__)

    def initialise(self):
        try:
            log.logFnEntryExit(__file__, 'initialise', 'begin')

            self.config = TestScriptsConfig()

            self.addresslist = self.config.serveraddress
            for item in self.addresslist:
                if (self.config.server in item['Server']):
                    self.address = item['Address']

            print(self.address)



            log.logFnEntryExit(__file__, 'initialise', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'initialise', ex)
            self.statusId = 5
            return False

    def uninitialise(self):
        try:
            log.logFnEntryExit(__file__, 'uninitialise', 'begin')



            log.logFnEntryExit(__file__, 'uninitialise', 'end')

        except Exception as ex:
            log.logException(__file__, 'uninitialise', ex)

    def execute(self):
        try:
            log.logFnEntryExit(__file__, 'execute', 'begin')

            log.logProgress(__file__, 'main', 'This is a test1 ' + self.address)

        except Exception as ex:
            log.logException(__file__, 'execute', ex)
            self.statusId = 5

if (__name__ == '__main__'):
    testScript = TestScript()
    testScript.main()
