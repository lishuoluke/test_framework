import datetime
import os
import shutil

import log_message as log
import log_test_message as logT
import json
#from testrail import *
from test_result_config import TestResultConfig


class TestResultFiles:
    def __init__(self):
        self.config = TestResultConfig()
        self.testResultPath = self.config.testResultPath;
        self.uploadStartTime = None

    def uninit(self):
        self.config = None

    def findTestResultFiles(self):
        log.logFnEntryExit(__file__, 'findTestResultFiles', 'begin')

        files = []
        for file in os.listdir(self.testResultPath):
            if file.endswith(".json"):
                files.append(file)

        log.logFnEntryExit(__file__, 'findTestResultFiles', 'end')
        return files

    def getTestResultStats(self, files):
        log.logFnEntryExit(__file__, 'getTestResultStats', 'begin')

        stats = [[], [], [], [], []]

        for file in files:
            try:
                resultFileName = self.testResultPath + '\\' + file
                f = open(resultFileName)
                content = json.load(f)
                statusId = content['result'][0]['status_id']
                stats[statusId - 1].append(file)
                f.close()

            except Exception as ex:
                log.logException(__file__, 'getTestResultStats', ex)
                continue

        log.logFnEntryExit(__file__, 'getTestResultStats', 'end')
        return stats

    def dumpStatsToFile(self, stats):
        log.logFnEntryExit(__file__, 'dumpStatsToFile', 'begin')

        # Prepare the statistics.
        content = {'passed': len(stats[0]), 'blocked': len(stats[1]), 'untested': len(stats[2]),
                   'retest': len(stats[3]), 'failed': len(stats[4])}

        # Add failed filenames.
        if (content['failed'] > 0):
            content['failed_files'] = []
            for file in stats[4]:
                failed = {}
                failed['file'] = file
                content['failed_files'].append(failed)

        # Dump to file.
        reportFileName = self.testResultPath + '\\test_result_report.txt'
        with open(reportFileName, 'w') as outFile:
            json.dump(content, outFile, indent=4)
        outFile.close()

        log.logFnEntryExit(__file__, 'dumpStatsToFile', 'end')

    def cleanup(self):
        log.logFnEntryExit(__file__, 'cleanup', 'begin')

        files = self.findTestResultFiles()

        # Add test_result_report.txt to the delete list.
        files.append('test_result_report.txt')

        # Delete.
        for file in files:
            try:
                resultFileName = self.testResultPath + '\\' + file
                if (os.path.isfile(resultFileName)):
                    os.remove(resultFileName)

            except Exception as ex:
                log.logException(__file__, 'cleanup', ex)
                continue

        log.logFnEntryExit(__file__, 'cleanup', 'end')

    def generateReport(self):
        try:
            log.logFnEntryExit(__file__, 'generateReport', 'begin')

            files = self.findTestResultFiles()
            stats = self.getTestResultStats(files)
            self.dumpStatsToFile(stats)

            log.logFnEntryExit(__file__, 'generateReport', 'end')
            return True

        except Exception as ex:
            log.logException(__file__, 'generateReport', ex)
            return False


    def backup(self):
        log.logFnEntryExit(__file__, 'backup', 'begin')

        files = self.findTestResultFiles()
        if (len(files) == 0):
            return

        if (self.uploadStartTime == None):
            folderPostfix = datetime.datetime.now().strftime("%H_%M_%S_%B_%d_%Y")
        else:
            folderPostfix = self.uploadStartTime
        self.uploadStartTime = None

        # Create the backup folder.
        backupPath = self.testResultPath + '\\Backup ' + folderPostfix
        os.makedirs(backupPath)

        # Add test_result_report.txt to the backup list.
        files.append('test_result_report.txt')

        # Backup.
        for file in files:
            try:
                resultFileName = self.testResultPath + '\\' + file
                archiveFileName = backupPath + '\\' + file
                shutil.move(resultFileName, archiveFileName)

            except Exception as ex:
                log.logException(__file__, 'backup', ex)
                continue

        log.logFnEntryExit(__file__, 'backup', 'end')


if (__name__ == '__main__'):
    testResultFiles = TestResultFiles()
    testResultFiles.generateReport()

