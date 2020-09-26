from threading import Thread
from collections import Counter

class AnalyzeDataThread(Thread):

    def __init__(self, param, isTaskDoneSig, resultSig):
        Thread.__init__(self)
        isTaskDoneSig.emit(False)

        self.isTaskDoneSig = isTaskDoneSig
        self.resultSig = resultSig
        print('[Task] 根据用户设定的参数对基因数据进行分析')
        
        '''
        param( type:list  item:as follows ) 
        [data, path, checkedId, checkedDad, checkedMom, minScale, maxScale, minHori]
        '''
        self.data = param[0]
        self.path = param[1]
        self.checkedId = param[2] + '_Scale'

        for idx in range(len(self.checkedId)):
            if not self.checkedId[idx].isdigit():
                num = int(self.checkedId[0:idx])
                suffix = self.checkedId[idx:]
                break
        if param[3]:
            self.checkedDad = str(num + 1) + suffix
        else:
            self.checkedDad = 'None'
        if param[4]:
            self.checkedMom = str(num + 2) + suffix
        else:
            self.checkedMom = 'None'

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
        print('[var] 检测者编号：%s 性别：%s 父亲编号：%s 母亲编号：%s' % (self.checkedId, self.gender, self.checkedDad, self.checkedMom))
        print('[var] 检测参数设置：最大范围：%f 最小范围：%f 最小检测深度：%f' % (self.maxScale, self.minScale, self.minHori))

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
        print('[run] 过滤掉不需要的数据---已完成')

        # arithmetic
        resultDictForTendency = self.getAbnormalGeneByTendency()
        resultDictForReference = self.getAbnormalGeneByReference()

        # work done
        summary = '[Summary]\n'
        summary += 'File Path: %s\n' % self.path
        summary += 'ID: %s [Father: %s  Mother: %s] Gender: %s\n' % (self.checkedId, self.checkedDad, self.checkedMom, self.gender)
        summary += 'Min Scale: %.2f Max Scale: %.2f Min Hori Average: %.2f\n' % (self.minScale, self.maxScale, self.minHori)
        summary += 'Abnormal Gene:\n'
        summary += '1) Abnormal Scale With Continuous Cds Gene Count: %d\n' % len(resultDictForTendency)
        summary += '2) Abnormal Scale Refer To Others Count: %d\n' % len(resultDictForReference)

        self.resultSig.emit(self.checkedId, summary, [resultDictForTendency, resultDictForReference])
        self.isTaskDoneSig.emit(True)

    def getAbnormalGeneByTendency(self):

        def abnormalScaleWithContinousCdsCount(abnormalDataFrame):
            dataIndex = list(abnormalDataFrame.index)
            dataIndex = dict(Counter(dataIndex))
            repetitiveDataIndex = [key for key,value in dataIndex.items()if value > 1]
            print('[run] 获取不正常刻度范围中CDS出现了两次及以上的基因')
            print('[var] ' + str(repetitiveDataIndex))

            for item in repetitiveDataIndex:
                print('[run] 处理基因：%s' % item)
                df = abnormalDataFrame.loc[item]
                cdsList = [ [ df['CDS'][0], [df['Index'][0]] ] ]
                for row in range(1, len(df)):
                    if df['CDS'][row] == cdsList[len(cdsList)-1][0]:
                        cdsList[len(cdsList)-1][1].append(df['Index'][row])
                    else:
                        cdsList.append([ df['CDS'][row], [df['Index'][row]] ])
                cdsList.sort()
                print('[var] CDS列表长度：%d 列表：%s' % (len(df.Index), str(cdsList)))

                if len(cdsList) < 2:
                    continue
                continousCdsIndex = []
                for idx in range(1, len(cdsList)):
                    if cdsList[idx][0] == cdsList[idx-1][0] + 1:
                        continousCdsIndex.extend(cdsList[idx][1])
                        continousCdsIndex.extend(cdsList[idx-1][1])
                continousCdsIndex = list(set(continousCdsIndex))
                print('[var] 连续CDS的索引：' + str(continousCdsIndex))

                if continousCdsIndex:
                    if item in result.keys():
                        result[item].extend(continousCdsIndex)
                    else:
                        result.update({item:continousCdsIndex})

        #--------------------------------------------------------------
        result = {}

        print('[run] 获取拥有连续CDS的不正常基因')
        scaleKey = self.checkedId
        data = self.filteredData
        lowScaleData = data[data[scaleKey] < self.minScale]
        highScaleData = data[data[scaleKey] > self.maxScale]
        abnormalScaleWithContinousCdsCount(lowScaleData)
        abnormalScaleWithContinousCdsCount(highScaleData)

        print('[run] 获取拥有连续CDS的不正常基因---已完成')
        print('[var] 分析结果' + str(result))
        return result

    def getAbnormalGeneByReference(self):
        print('[run] 获取不正常基因，但参考者是正常的')
        # filter data of parent and self
        data = self.filteredData
        data = data.drop(self.checkedId, axis=1)
        if self.checkedDad != 'None':
            data = data.drop(self.checkedDad, axis=1)
        if self.checkedMom != 'None':
            data = data.drop(self.checkedMom, axis=1)
        print('[run] 获取不正常刻度范围中CDS出现了两次及以上的基因')
        print('[var] 过滤其双亲作为参考者：' + self.checkedDad + self.checkedMom)

        referKey = []
        for item in data.columns:
            if item[-6:] == '_Scale':
                referKey.append(item)
        print('[var] 参考者列表：' + str(referKey))

        for item in referKey:
            data = data[(data[item] < self.maxScale) & (data[item] > self.minScale)]

        result = {'referKey': referKey}
        for index, item in data.iterrows():
            if index in result.keys():
                result[index].append(item.Index)
            else:
                result.update({index:[item.Index]})

        print('[run] 获取不正常基因，但参考者是正常的---已完成')
        print('[var] 分析结果' + str(result))
        return result