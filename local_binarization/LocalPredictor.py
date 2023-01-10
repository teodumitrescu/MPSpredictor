import pandas as pd
import glob
import random

from DataFileReaderLocal import DataFileReaderLocal
from FunctionPicker import FunctionPicker

class LocalPredictor:
    def __init__(self, filespath):
        self.filespath = filespath
        self.pathToFiles = glob.glob(filespath)

    def iterateThroughFiles(self):
        readers = []
        for pathToFile in self.pathToFiles:
        # pathToFile = 'input/[AVE_INT] 7_15.CSV'
            dataFilesReader = DataFileReaderLocal(pathToFile)
            dataFilesReader.getData()
            readers.append(dataFilesReader)

        self.readers = readers

    def generateSolutions(self):
        functionPicker = FunctionPicker()

        output_path = 'output/local_logs.out'
        output_file = open(output_path, 'w+')

        for i in range(10):
            print(i)
            random_nr = random.randint(2, len(self.readers[0].pixelsList[0].thresholds))
            function_number = random.randint(0, 6)
            random_indexes = []
            for nr in range(random_nr):
                random_indexes.append(random.randint(0, len(self.readers[0].pixelsList[0].thresholds) - 1))

            score = 0
            for reader in self.readers:
                true_positives = 0
                false_positives = 0
                false_negatives = 0
                
                for pixel in reader.pixelsList:
                    values = []
                    for index in random_indexes:
                        values.append(pixel.thresholds[index])

                    pixel.thresholds.append(functionPicker.random_applier(values, function_number))
                    new_groundtype = 0
                    if pixel.value < pixel.thresholds[-1]:
                        new_groundtype = 1

                    if (pixel.groundType == 0) & (new_groundtype == 0):
                        true_positives = true_positives + 1
                    elif (pixel.groundType == 0) & (new_groundtype == 1):
                        false_positives = false_positives + 1
                    elif (pixel.groundType == 1) & (new_groundtype == 0):
                        false_negatives = false_negatives + 1
                
                reader.fmeans = 0
                if (true_positives != 0 | false_negatives != 0 | false_positives != 0):   
                    reader.fmeans = true_positives / (true_positives + 0.5 * (false_positives + false_negatives))

                # print(reader.filepath + ' ' + str(reader.fmeans))
                score = score + reader.fmeans

            output_file.write(str(random_nr) + ' ')

            for index in range(random_nr):
                output_file.write(str(random_indexes[index]) + ' ')

            output_file.write(str(function_number) + ' ' + str(score / len(self.readers)) + '\n')

    def startAlgorithm(self):
        self.iterateThroughFiles()
        self.generateSolutions()

if __name__ == "__main__":
    predictor = LocalPredictor("input/*.CSV")
    predictor.startAlgorithm()