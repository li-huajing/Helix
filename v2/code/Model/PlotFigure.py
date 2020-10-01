import threading
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

class PlotFigureThread(threading.Thread):

    def __init__(self, data, chromosome, idUnderTest):
        threading.Thread.__init__(self)
        
        data['GeneIndex'] = data['Gene1'] + data['Index'].map(str)
        self.data = data
        self.chromosome = chromosome
        self.iut = idUnderTest
        print('[Task] 画每条染色体的基因刻度对比，染色体列表为：%s' % str(chromosome))

    def run(self):
        idList = []
        for item in self.data:
            if item[-6:] == '_Scale':
                idList.append(item)
        idList.remove(self.iut)
        idList.append(self.iut)

        for chr in self.chromosome:
            print('[run] 开始生成数据图，染色体：' + chr)
            data = self.data.loc[chr]

            x = []
            for index, item in data.iterrows():
                x.append(item['GeneIndex'])
            yList = []
            for item in idList:
                yList.append(list(data[item]))

            fig = plt.figure()
            fig.canvas.set_window_title('Chromosome' + chr)
            plt.ylim(0.0, 2.0)
            plt.xticks([])
            for y in yList:
                plt.plot(x, y)
            plt.legend(tuple(idList))

        plt.show()