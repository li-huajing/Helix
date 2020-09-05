import sys
sys.path.append('..')

from Model import GeAnalyzer
from Model import GeDatabase
import xlrd, threading, os, time

class Dispatcher(object):
    
    def __init__(self):
        pass

    #---------------------------
    # Log 
    #---------------------------
    def configLogger(self, viewer):
        self.logger = viewer

    def message(self, string):
        self.logger.printLog(string, 'message')

    def information(self, string):
        self.logger.printLog(string, 'information')

    def error(self, string):
        self.logger.printLog(string, 'error')

    def warning(self, string):
        self.logger.printLog(string, 'warning')

    #---------------------------
    # Process Bar
    #---------------------------
    def processBarShow(self, estimatedTotalTime, processBar, frame, signal):
        sleepTime = estimatedTotalTime / 100
        for i in range(99):
            if signal.isSet():
                processBar["value"] = 100
            else:
                processBar["value"] = i + 1
            frame.update()
            time.sleep(sleepTime)
        signal.wait()
        processBar["value"] = 100

    #---------------------------
    # Gene
    #---------------------------
    def openDataFile(self, path, candidateList, signal, processBar, frame):
        if not os.path.isfile(path):
            self.error("Please check the location of file!\n")
            return

        def threadForOpenDataFile():
            bookHandle = xlrd.open_workbook(path)
            self.dataSheet = bookHandle.sheet_by_index(0)
            bookHandle.release_resources()
            head = [str(self.dataSheet.cell_value(0, col)) for col in range(0, self.dataSheet.ncols)]
            candidateList['value'] = GeAnalyzer.getCandidateId(head)
            self.analysisResult = ""
            self.message("The Gene data parse completed~\n")
            signal.set()

        def threadForProcessBarShow():
            fsize = os.path.getsize(path)
            estimatedTimeForParse = fsize / 180000 # unit:s
            self.processBarShow(estimatedTimeForParse, processBar, frame, signal)

        threading.Thread(target = threadForOpenDataFile).start()
        threading.Thread(target = threadForProcessBarShow).start()

    def analyzeData(self, id, max, min, minHori, reportBoard, signal, processBar, frame, flagFa, flagMo):
        def threadForAnalyzeData():
            self.analysisResult = GeAnalyzer.getAbnormalData(self.dataSheet, id, max, min, minHori)
            self.outOfSpecResult = GeAnalyzer.getOutOfSpecData(self.dataSheet, id, max, min, minHori, flagFa, flagMo)

            res = self.analysisResult
            showReoprt = "ID: %s  sex: %s\n" % (res.id, res.sex)
            showReoprt += "minScale: %s  maxScale: %s  minHoriAverage: %s\n" % (res.minScale, res.maxScale, res.minHoriAverage)
            showReoprt += 'generate on time: %s\n' % time.asctime(time.localtime(time.time()))
            showReoprt += 'Abnormal Gene:\n'
            for item in res.abnormalGeneList:
                showReoprt += 'chromosome: %s gene: %s\n' % (item.chromosome, item.geneName)
            reportBoard["text"] = showReoprt
            self.message("The Gene data analysis completed~\n")
            signal.set()
        
        def threadForProcessBarShow():
            self.processBarShow(3, processBar, frame, signal)

        threading.Thread(target = threadForAnalyzeData).start()
        threading.Thread(target = threadForProcessBarShow).start()

    def generateReport(self, fp, signal, processBar, frame):

        def threadForGenerateReport():
            res = self.analysisResult
            fp.write("-" * 100 + "\n")
            fp.write("-  ID: %s  sex: %s\n" % (res.id, res.sex))
            fp.write("-  Generated time: %s\n" % time.ctime())
            fp.write("-  Parameter: minScale[%s] maxScale[%s] minHoriAverage[%s]\n" % (res.minScale, res.maxScale, res.minHoriAverage))
            fp.write("-" * 100 + "\n")
    
            num = 0
            ChrPosStartCol = 2
            ChrPosEndCol = 3
            CDSCol = 4
            scaleCol = res.columnOfIdScale
            horiCol = res.columnOfIdHori
            for item in res.abnormalGeneList:
                fp.write("\n[%d]Chromosome: %s  Gene: %s " % (num, item.chromosome, item.geneName))
                try:
                    fp.write("CHN: %s inheritance: %s\n" % (self.DB[item.geneName].chnName, self.DB[item.geneName].inheritance))
                    fp.write("Description: %s\n" % self.DB[item.geneName].description)
                except KeyError:
                    fp.write("\nShort of data in database!\n")
                fp.write("[ index ]\t[Chr Position Start]\t[Chr Position End]\t[CDS]\t[HoriAverage]\t[   Scale   ]\n")
                for index in item.abnormalIndexList:
                    fp.write("%9d\t%20d\t%18d\t%5d\t%.9f\t%.11f\n" % (
                        index,
                        self.dataSheet.cell(index, ChrPosStartCol).value,
                        self.dataSheet.cell(index, ChrPosEndCol).value,
                        int(self.dataSheet.cell(index, CDSCol).value),
                        self.dataSheet.cell(index, scaleCol).value,
                        self.dataSheet.cell(index, horiCol).value,
                    )) 
    
            fp.write('=' * 60 + '\n')
            fp.write('= Out Of Specification\n')
            fp.write('=' * 60 + '\n')
    
            tempDict = {}
            columnOfGene = 5
            for item in self.outOfSpecResult[1]:
                geneKey = self.dataSheet.cell(item, columnOfGene).value
                if geneKey not in tempDict.keys():
                    tempDict.update({geneKey: []})
                tempDict[geneKey].append(item)

            for item in tempDict.keys():
                fp.write("\nGene: %s " % item)
                try:
                    fp.write("CHN: %s inheritance: %s\n" % (self.DB[item].chnName, self.DB[item].inheritance))
                    fp.write("Description: %s\n" % self.DB[item].description)
                except KeyError:
                    fp.write("\nShort of data in database!\n")    
                fp.write("[ index ]\t[Chr Position Start]\t[Chr Position End]\t[CDS]\t[HoriAverage]\t[   Scale   ]\t[Reference]\n")
                for index in tempDict[item]:
                    fp.write("%9d\t%20d\t%18d\t%5d\t%.9f\t%.11f" % (
                        index,
                        self.dataSheet.cell(index, ChrPosStartCol).value,
                        self.dataSheet.cell(index, ChrPosEndCol).value,
                        int(self.dataSheet.cell(index, CDSCol).value),
                        self.dataSheet.cell(index, scaleCol).value,
                        self.dataSheet.cell(index, horiCol).value,
                    ))
                    for col in self.outOfSpecResult[0]:
                        fp.write("\t%f" % self.dataSheet.cell(index, col).value)
                    fp.write("\n")
    
            fp.close()
            self.message("The report have been generated successfully~\n")
            signal.set()
            
        def threadForProcessBarShow():
            self.processBarShow(3, processBar, frame, signal)

        threading.Thread(target = threadForGenerateReport).start()
        threading.Thread(target = threadForProcessBarShow).start()

    #---------------------------
    # Updata DB
    #---------------------------
    def initializeDatabase(self, frame, databaseDescription, geneList):
        self.DB = GeDatabase.getDB(databaseDescription)
        geneList['value'] = tuple(self.DB.keys())
        frame.update()

    def updateDatabase(self, path, signal, processBar, frame, databaseDescription, geneList):
        if not os.path.isfile(path):
            self.error("Please check the location of file!\n")
            return

        def threadForUpdateDatabase():
            bookHandle = xlrd.open_workbook(path)
            dataSheet = bookHandle.sheet_by_index(0)
            bookHandle.release_resources()
            GeDatabase.updateDB(dataSheet, os.path.basename(path), time.ctime())
            self.initializeDatabase(frame, databaseDescription, geneList)
            self.message("The Gene database have been updated successfully~\n")
            signal.set()

        def threadForProcessBarShow():
            fsize = os.path.getsize(path)
            estimatedTimeForParse = fsize / 180000 # unit:s
            self.processBarShow(estimatedTimeForParse, processBar, frame, signal)

        threading.Thread(target = threadForUpdateDatabase).start()
        threading.Thread(target = threadForProcessBarShow).start()

    def checkDescriptionByGeneName(self, checkGene, showResult):
        if checkGene in self.DB.keys():
            showResult['text'] = '%s(%s) inheritance:%s\n' % (checkGene, self.DB[checkGene].chnName, self.DB[checkGene].inheritance)
            showResult['text'] += self.DB[checkGene].description
        else:
            showResult['text'] = 'Can\'t find the gene in Database\n'