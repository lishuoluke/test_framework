import json

import global_vars


class TestAutomationConfig:
    def __init__(self):
        configFileName = global_vars.configFileName# the global variable is configFileName = os.path.expanduser('~/iTAS/main_config.json')
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile) #load json content
            self.rootPath = config['rootPath']
            self.testPlatform = config['testPlatform']
            self.runTestSuite = config['runTestSuite']
            self.generateTestResultReport = config['generateTestResultReport']

        outFile.close()
