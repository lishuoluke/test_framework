import json

import global_vars


class TestScriptsConfig:
    def __init__(self):
        configFileName = global_vars.configFileName
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            self.testSuitePath = config['testSuitePath']
        outFile.close()

        configFileName = self.testSuitePath + '\\' + 'test_script_config.json'
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            self.softwareVersion = config['softwareVersion']
            self.idleBetweenScriptsInSeconds = config['idleBetweenScriptsInSeconds']
            self.scripts = config['scripts']
            self.server = config['Test Server']
            self.serveraddress = config['Server Address']

        outFile.close()
