import time
from abc import ABC, abstractmethod

import log_message as log
from test_scripts_config import TestScriptsConfig


class TestScriptsBase(ABC):
    def __init__(self, source):
        self.source = source

        self.config = TestScriptsConfig()

    def uninit(self):
        self.config = None

    @abstractmethod
    def runScript(self, script):
        pass


    def main(self):
        log.logFnEntryExit(self.source, 'run', '### Begin ###')

        # Enumerate through the list of test scripts.
        for script in self.config.scripts:
            try:
                if (not self.config.server in script['Server']):
                    continue

                success = self.runScript(script)
                time.sleep(self.config.idleBetweenScriptsInSeconds)
                if (not success):
                    continue


            except Exception as ex:
                log.logException(self.source, 'run', ex)
                continue

        log.logFnEntryExit(self.source, 'run', '### End ###')
