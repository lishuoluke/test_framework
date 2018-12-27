import datetime
import os

from log_config import LogConfig


def delete(source):
    config = LogConfig()
    if (config.deleteLog):
        try:
            index = source.rfind('.')
            logFileName = source[:index] + '_log.txt'
            os.remove(logFileName)
        except Exception as ex:
            print(ex)


def log(source, function, description):
    try:
        time = datetime.datetime.now().strftime("%H_%M_%S_%B_%d_%Y")
        fileName = os.path.basename(source)
        message = time + ' - ' + fileName + ' : ' + function + ' - ' + description
        print(message)

        index = source.rfind('.')
        logFileName = source[:index] + '_log.txt'
        logFile = open(logFileName, 'a')
        message = time + ' - ' + function + ' - ' + description + '\n'
        logFile.write(message)

        logFile.close()
    except Exception as ex:
        print(ex)


def logFnEntryExit(source, function, description):
    config = LogConfig()
    if (config.logLevel < 10):
        return

    log(source, function, description)


def logProgress(source, function, description):
    config = LogConfig()
    if (config.logLevel < 5):
        return

    log(source, function, description)


def logError(source, function, description):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(source, function, description)


def logException(source, function, exception):
    config = LogConfig()
    if (config.logLevel == 0):
        return

    log(source, function, 'Exception - ' + str(exception))
