import threading

class GenerateReportThread(threading.Thread):

    def __init__(self, path, report, db, dataFrame):
        threading.Thread.__init__(self)
        self.path = path
        self.report = report
        self.db = db
        self.df = dataFrame
        self.id = report[0]

    def run(self):
        fp = open(self.path, 'w')

        # print Summary
        fp.write('*' * 100 + '\n')
        fp.write(self.report[1])
        fp.write('*' * 100 + '\n')

        # print Genes have Abnormal Scale With Continous CDS
        fp.write('\n\n' + '-' * 60 + '\n')
        fp.write('- ' + 'The Genes have Abnormal Scale With Continous CDS\n')
        fp.write('-' * 60 + '\n')

        idx = 0
        rp = self.report[2][0]
        if self.df.columns.get_loc(self.id) > self.df.columns.get_loc('HoriAverage1'):
            horiKey = 'HoriAverage2'
        else:
            horiKey = 'HoriAverage1'

        for gene in rp.keys():
            fp.write('\n[%d] Gene Name: %s\n' % (idx, gene))
            try:
                fp.write(self.db[gene])
            except KeyError:
                fp.write("Short of data in database!\n")
            # print original data
            fp.write("[ index ]\t[Chr Position Start]\t[Chr Position End]\t[CDS]\t[HoriAverage]\t[   Scale   ]\n")
            for dataIndex in rp[gene]:
                fp.write("%9d\t%20d\t%18d\t%5d\t%.9f\t%.11f\n" % (
                        dataIndex,
                        self.df['Chr Position Start'][dataIndex],
                        self.df['Chr Position End'][dataIndex],
                        int(self.df['CDS'][dataIndex]),
                        self.df[horiKey][dataIndex],
                        self.df[self.id][dataIndex],
                    )) 
        
        # print Genes have Abnormal Scale With Continous CDS
        fp.write('\n\n' + '-' * 60 + '\n')
        fp.write('- ' + 'The Genes have Abnormal Scale Refer To Other Spec-In Scale\n')
        fp.write('-' * 60 + '\n')

        idx = 0
        rp = self.report[2][1]
        reference = rp['referKey']
        del rp['referKey']

        for gene in rp.keys():
            fp.write('\n[%d] Gene Name: %s\n' % (idx, gene))
            try:
                fp.write(self.db[gene])
            except KeyError:
                fp.write("Short of data in database!\n")
            # print original data
            fp.write("[ index ]\t[Chr Position Start]\t[Chr Position End]\t[   Scale   ]\t[Reference]\n")
            for dataIndex in rp[gene]:
                fp.write("%9d\t%20d\t%18d\t%.11f" % (
                        dataIndex,
                        self.df['Chr Position Start'][dataIndex],
                        self.df['Chr Position End'][dataIndex],
                        self.df[self.id][dataIndex],
                    ))
                for scale in reference:
                    fp.write("\t%f" % self.df[scale][dataIndex])
                fp.write("\n")
        
        # save
        fp.close()

        