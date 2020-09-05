import re

class GeneNode(object):

    def __init__(self, key):
        temp = key.split('_')
        self.chromosome = temp[1]
        self.geneName = temp[0]
        #self.indexList = []
        self.lowScaleCDS = []
        self.lowScaleIndex = []
        self.highScaleCDS = []
        self.highScaleIndex = []
        self.abnormalIndexList = []

class ReportNode(object):

    def __init__(self):
        self.id = ''
        self.sex = 'male'
        self.minScale = ''
        self.maxScale = ''
        self.minHoriAverage = ''
        self.abnormalGeneList = []
        self.columnOfIdScale = ''
        self.columnOfIdHori = ''

def getCandidateId(tableHead):
    id = []
    for item in tableHead:
        if re.match(".*_Scale$", item):
            id.append(int(re.sub("\D", "", item)))
    id.sort()  
    return tuple(id)

def getAbnormalData(dataSheet, id, max, min, minHori):
    columnOfChr = 1
    columnOfCDS = 4
    columnOfGene = 5
    columnOfIdScale = ''
    columnOfHoriAverage = ''
    # Search the column index
    for index in range(6, dataSheet.ncols):
        if dataSheet.cell(0, index).value == id + '_Scale':
            columnOfIdScale = index
            break
    for index in range(columnOfIdScale, dataSheet.ncols):
        if re.match('HoriAverage.', dataSheet.cell(0, index).value):
            columnOfHoriAverage = index
            break
    # Classify data by gene name and get rig of useless data
    dataBuffer = {}
    for row in range(1, dataSheet.nrows):
        geneKey = dataSheet.cell(row, columnOfGene).value
        geneKey = geneKey + '_' + str(dataSheet.cell(row, columnOfChr).value)
        if geneKey not in dataBuffer.keys():
            dataBuffer.update({geneKey: GeneNode(geneKey)})
        #dataBuffer[geneKey].indexList.append(row)
        if dataSheet.cell(row, columnOfHoriAverage).value < minHori:
            continue
        if not dataSheet.cell(row, columnOfCDS).value:
            continue
        scale = dataSheet.cell(row, columnOfIdScale).value
        if scale < min:
            dataBuffer[geneKey].lowScaleCDS.append(int(dataSheet.cell(row, columnOfCDS).value))
            dataBuffer[geneKey].lowScaleIndex.append(row)
        elif scale > max:
            dataBuffer[geneKey].highScaleCDS.append(int(dataSheet.cell(row, columnOfCDS).value))
            dataBuffer[geneKey].highScaleIndex.append(row)
    # Determine the data and generate report
    report = ReportNode()
    report.id = id
    report.maxScale = str(max)
    report.minScale = str(min)
    report.minHoriAverage = str(minHori)
    report.columnOfIdHori = columnOfHoriAverage
    report.columnOfIdScale = columnOfIdScale
    if dataSheet.cell(0, columnOfHoriAverage).value == 'HoriAverage2':
        report.sex = 'female'

    for key in dataBuffer.keys():
        def findAbnormalDataIndex(cdsList, indexList):
            if len(cdsList) < 2:
                return
            #find continuous cds
            flag = []
            for num in range(0, len(cdsList) - 1):
                flag.append(cdsList[num+1] - cdsList[num])
            flag.append(2)

            isContinuous = 0
            for i in range(0, len(flag)):
                if flag[i] == 1 or isContinuous == 1 or flag[i] == -1 or isContinuous == -1:
                    dataBuffer[key].abnormalIndexList.append(indexList[i])
                isContinuous = flag[i]

        findAbnormalDataIndex(dataBuffer[key].lowScaleCDS, dataBuffer[key].lowScaleIndex)
        findAbnormalDataIndex(dataBuffer[key].highScaleCDS, dataBuffer[key].highScaleIndex)
        if dataBuffer[key].abnormalIndexList:
            report.abnormalGeneList.append(dataBuffer[key])

    return report

def getOutOfSpecData(dataSheet, id, max, min, minHori, flagFa, flagMo):
    columnOfCDS = 4
    columnOfHoriAverage = ''
    columnOfIdScale = ''
    columnOfRefer = []
    tableOfRefer = []

    for index in range(6, dataSheet.ncols):
        if dataSheet.cell(0, index).value == id + '_Scale':
            columnOfIdScale = index
            break

    for index in range(columnOfIdScale, dataSheet.ncols):
        if re.match('HoriAverage.', dataSheet.cell(0, index).value):
            columnOfHoriAverage = index
            break

    if flagFa == '1':
        fa = str(int(id) + 1) + '_Scale'
    else:
        fa = 'None'
    if flagMo == '1':
        mo = str(int(id) + 2) + '_Scale'
    else:
        mo = 'None'
    for index in range(6, dataSheet.ncols):
        if dataSheet.cell(0, index).value == fa:
            continue
        if dataSheet.cell(0, index).value == mo:
            continue
        if dataSheet.cell(0, index).value == id + '_Scale':
            continue
        if re.match('.*_Scale', dataSheet.cell(0, index).value):
            tableOfRefer.append(dataSheet.cell(0, index).value)
            columnOfRefer.append(index)

    dataBuffer = []
    reportOfOutOfSepc = []
    reportOfOutOfSepc.append(columnOfRefer)

    for row in range(1, dataSheet.nrows):
        if dataSheet.cell(row, columnOfHoriAverage).value < minHori:
            continue
        if not dataSheet.cell(row, columnOfCDS).value:
            continue
        if dataSheet.cell(row, columnOfIdScale).value > min and dataSheet.cell(row, columnOfIdScale).value < max:
            continue

        isOutOfSpec = 0
        for col in columnOfRefer:
            if dataSheet.cell(row, col).value > min and dataSheet.cell(row, col).value < max:
                continue
            isOutOfSpec = 1

        if isOutOfSpec:
            isOutOfSpec = 0
            continue

        dataBuffer.append(row)

    
    reportOfOutOfSepc.append(dataBuffer)
    return reportOfOutOfSepc
