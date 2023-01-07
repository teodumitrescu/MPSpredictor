import pandas as pd
import math
import glob
import platform
import random
import sys
import os
print(sys.version)
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from DataFileReaderLocal import DataFileReaderLocal
from FunctionPicker import FunctionPicker
from Pixel import Pixel

class LocalPredictor:
    def __init__(self, filespath):
        self.filespath = filespath
        self.pathToFiles = glob.glob(filespath)

    def iterateThroughFiles(self):
        readers = []
        # for pathToFile in self.pathToFiles:
        pathToFile = 'input\\input5.CSV'
        dataFilesReader = DataFileReaderLocal(pathToFile)
        dataFilesReader.getData()
        
        if (platform.system() == 'Linux'):
            output_path = 'output/' + pathToFile.split('/')[-1][:-3] + 'out'
        else:
            output_path = 'output/' + pathToFile.split('\\')[-1][:-3] + 'out'
        output_file = open(output_path, 'w+')

        readers.append(dataFilesReader)

        self.readers = readers

    def generateSolutions(self):
        functionPicker = FunctionPicker()

        output_path = 'output/local_logs.out'
        output_file = open(output_path, 'w+')

        for i in range(1000):
            random_nr = random.randint(2, len(self.readers[0].pixelsList[0].thresholds))
            function_number = random.randint(0, 6)
            random_indexes = []
            for nr in range(random_nr):
                random_indexes.append(random.randint(0, len(self.readers[0].pixelsList[0].thresholds) - 1))

            score = 0
            for reader in self.readers:
                for pixel in reader.pixelsList:
                    values = []
                    for index in random_indexes:
                        values.append(pixel.thresholds[index])

                pixel.thresholds.append(functionPicker.random_applier(values, function_number))
                score = score + (pixel.fmeans())

            output_file.write(str(random_nr) + ' ' + str(random_indexes) + ' ' + str(function_number) + ' ' + str(score / len(self.readers)) + '\n')
            
    def startAlgorithm(self):
        self.iterateThroughFiles()
        self.generateSolutions()

if __name__ == "__main__":
    predictor = LocalPredictor("input/*.CSV")
    predictor.startAlgorithm()