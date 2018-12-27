from abc import ABC, abstractmethod

import log_test_message as log


class PythonScriptBase(ABC):
    def __init__(self, source):
        self.source = source

        self.statusId = 1
        self.comment = ''

    @abstractmethod
    def initialise(self):
        pass

    @abstractmethod
    def uninitialise(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    def main(self):
        try:
            log.delete(self.source)
            log.logFnEntryExit(self.source, 'main', '### Begin ###')

            if (self.initialise()):
                self.execute()

            self.uninitialise()

            log.logFnEntryExit(self.source, 'main', '### End ###')
            return True

        except Exception as ex:
            log.logError(self.source, 'main', '! SHOULD NOT REACH HERE. Test script should do proper error handling. !')
            log.logException(self.source, 'main', ex)
            return False
