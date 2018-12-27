import json
import os

import global_vars


class TestResultConfig:
    def __init__(self):
        configFileName = global_vars.configFileName
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            if ('testResultPath' in config):
                self.testResultPath = config['testResultPath']
            else:
                self.testResultPath = os.path.join(config['testSuitePath'], 'test_result')
            if (not os.path.exists(self.testResultPath)):
                os.makedirs(self.testResultPath)

        outFile.close()
