import pandas as pd
import math
import glob

from DataFilesReader import DataFilesReader

class Predictor:
    def __init__(self, filespath):
        self.filespath = filespath
        self.pathToFiles = glob.glob(filespath)

    def iterateThroughFiles(self):
        for pathToFile in self.pathToFiles:
            # pathToFile = 'input/input0.CSV'
            dataFilesReader = DataFilesReader(pathToFile)
            dataFilesReader.getData()
            
            output_path = 'output/' + pathToFile.split('/')[-1][:-3] + 'out'
            output_file = open(output_path, 'w+')
            output_file.write(str(dataFilesReader.expectedValue))
            output_file.write('\n')
            output_file.write(str(dataFilesReader.getMean()))

    def startAlgorithm(self):
        self.iterateThroughFiles()

if __name__ == "__main__":
    predictor = Predictor("input/*.CSV")
    predictor.startAlgorithm()
