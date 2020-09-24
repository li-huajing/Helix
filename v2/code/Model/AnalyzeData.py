from threading import Thread
from collections import Counter

class AnalyzeDataThread(Thread):

    def __init__(self, param, isTaskDoneSig, resultSig):
        Thread.__init__(self)
        isTaskDoneSig.emit(False)

        self.isTaskDoneSig = isTaskDoneSig
        self.resultSig = resultSig
        '''
        param( type:list  item:as follows ) 
        [data, path, checkedId, checkedDad, checkedMom, minScale, maxScale, minHori]
        '''
        self.data = param[0]
        self.path = param[1]
        self.checkedId = param[2] + '_Scale'
        self.checkedDad = str(int(param[2]) + 1) + '_Scale' if param[3] else ''
        self.checkedMom = str(int(param[2]) + 2) + '_Scale' if param[4] else ''
        self.minScale = float(param[5])
        self.maxScale = float(param[6])
        self.minHori = float(param[7])

        # judge gender
        checkIdAtColumnIndex = self.data.columns.get_loc(self.checkedId)
        hori1AtColumnIndex = self.data.columns.get_loc('HoriAverage1')
        if checkIdAtColumnIndex > hori1AtColumnIndex:
            self.gender = 'female'
        else:
            self.gender = 'male'

    def run(self):
        # filter data
        data = self.data.drop(['Chr Position Start', 'Chr Position End'], axis=1)
        if self.gender == 'male':
            horiKey = 'HoriAverage1'
        else:
            horiKey = 'HoriAverage2'
        data = data.reset_index()
        data = data.set_index('Gene1')
        data = data[data[horiKey] > self.minHori]
        data = data[(data[self.checkedId] < self.minScale) | (data[self.checkedId] > self.maxScale)]
        self.filteredData = data

        # arithmetic
        resultDictForTendency = self.getAbnormalGeneByTendency()
        resultDictForReference = self.getAbnormalGeneByReference()

        # work done
        self.resultSig.emit()
        self.isTaskDoneSig.emit(True)

    def getAbnormalGeneByTendency(self):

        def abnormalScaleWithContinousCdsCount(abnormalDataFrame):
            dataIndex = list(abnormalDataFrame.index)
            dataIndex = dict(Counter(dataIndex))
            repetitiveDataIndex = [key for key,value in dataIndex.items()if value > 1]

            for item in repetitiveDataIndex:
                df = abnormalDataFrame.loc[item]
                cdsList = [ [ df['CDS'][0], [df['Index'][0]] ] ]
                for row in range(1, len(df)):
                    if df['CDS'][row] == cdsList[len(cdsList)-1][0]:
                        cdsList[len(cdsList)-1][1].append(df['Index'][row])
                    else:
                        cdsList.append([ df['CDS'][row], [df['Index'][row]] ])
                cdsList.sort()
                print(len(df.Index), cdsList)

                if len(cdsList) < 2:
                    continue
                continousCdsIndex = []
                for idx in range(1, len(cdsList)):
                    if cdsList[idx][0] == cdsList[idx-1][0] + 1:
                        continousCdsIndex.extend(cdsList[idx][1])
                        continousCdsIndex.extend(cdsList[idx-1][1])
                continousCdsIndex = list(set(continousCdsIndex))
                print(continousCdsIndex)

                if continousCdsIndex:
                    print(item)
                    if item in result.keys():
                        result[item].extend(continousCdsIndex)
                    else:
                        result.update({item:continousCdsIndex})

        #--------------------------------------------------------------
        result = {}

        scaleKey = self.checkedId
        data = self.filteredData
        lowScaleData = data[data[scaleKey] < self.minScale]
        highScaleData = data[data[scaleKey] > self.maxScale]
        abnormalScaleWithContinousCdsCount(lowScaleData)
        abnormalScaleWithContinousCdsCount(highScaleData)

        print(result)
        return result

    def getAbnormalGeneByReference(self):
        # filter data of parent and self
        data = self.filteredData
        data = data.drop(self.checkedId, axis=1)
        if self.checkedDad:
            data = data.drop(self.checkedDad, axis=1)
        if self.checkedMom:
            data = data.drop(self.checkedMom, axis=1)
        
        referKey = []
        for item in data.columns:
            if item[-6:] == '_Scale':
                referKey.append(item)
        print(referKey)

        for item in referKey:
            data = data[(data[item] < self.maxScale) & (data[item] > self.minScale)]
        print(data)

        result = {}
        for index, item in data.iterrows():
            if index in result.keys():
                result[index].append(item.Index)
            else:
                result.update({index:[item.Index]})

        print(result)
        return result