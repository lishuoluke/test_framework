import datetime
import os

from log_config import LogConfig


def delete():
    config = LogConfig()
    if (config.deleteLog):
        try:
            os.remove(config.logFileName)
        except Exception as ex:
            print(ex)


def log(logFileName, source, function, description):
    try:
        time = datetime.datetime.now().strftime("%H_%M_%S_%B_%d_%Y")
        fileName = os.path.basename(source)
        message = time + ' - ' + fileName + ' : ' + function + ' - ' + description
        print(message)

        logFile = open(logFileName, 'a')
        message += '\n'
        logFile.write(message)

        logFile.close()
    except Exception as ex:
        print(ex)


def logEmptyLine():
    config = LogConfig()

    print('')
    logFile = open(config.logFileName, 'a')
    logFile.write('\n')

    logFile.close()

def logFnEntryExit(source, function, description):
    config = LogConfig()
    if (config.logLevel < 10):
        return

    log(config.logFileName, source, function, description)


def logProgress(source, function, description):
    config = LogConfig()
    if (config.logLevel < 5):
        return

    log(config.logFileName, source, function, description)


def logError(source, function, description):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(config.logFileName, source, function, description)


def logException(source, function, exception):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(config.logFileName, source, function, 'Exception - ' + str(exception))
