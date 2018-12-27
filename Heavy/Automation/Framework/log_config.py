import json

import global_vars


class LogConfig:
    def __init__(self):
        configFileName = global_vars.configFileName
        with open(configFileName, 'r') as outFile:
            config = json.load(outFile)
            rootPath = config['rootPath']
            self.logLevel = config['logLevel']
            self.deleteLog = config['deleteLog']
        outFile.close()

        self.logFileName = rootPath + '\\framework_log.txt'
