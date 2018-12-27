import json
import sys

import log_message as log
from test_result_config import TestResultConfig


def generateTestResultFile(caseId, statusId, version, comment, custom={}):
    try:
        log.logFnEntryExit(__file__, 'generateTestResultFile', 'begin')

        config = TestResultConfig()

        # Prepare the testrail fields.
        test = {'case_id': caseId, 'status_id': statusId, 'version': version, 'comment': comment}

        # Add custom fields if any.
        for k, v in custom.items():
            test[k] = v

        content = {'result': []}
        content['result'].append(test)

        # Dump to file.
        fileName = 'runId_' + '_caseId_' + str(caseId) + '.json'
        resultFileName = config.testResultPath + '\\' + fileName
        with open(resultFileName, 'w') as outFile:
            json.dump(content, outFile, indent=4)
        outFile.close()

        log.logFnEntryExit(__file__, 'generateTestResultFile', 'end')
        return True

    except Exception as ex:
        log.logException(__file__, 'generateTestResultFile', ex)
        return False


if (__name__ == '__main__'):
    if (len(sys.argv) >= 5):
        caseId = int(sys.argv[1])
        statusId = int(sys.argv[2])
        version = sys.argv[3]
        comment = sys.argv[4]

        cust = {}
        for item in sys.argv[5:]:
            index = item.find(':')
            cust[item[:index]] = item[index + 1:]

        generateTestResultFile(caseId, statusId, version, comment, cust)
