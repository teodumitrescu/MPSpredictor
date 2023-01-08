import pandas as pd
import math
import glob
import platform
import random
import csv
import os

from DataFilesReader import DataFilesReader
from FunctionPicker import FunctionPicker

class Predictor:
    def __init__(self, filespath):
        self.filespath = filespath
        self.pathToFiles = glob.glob(filespath)
        self.logoutput = 'output/logs.out'
        self.treeoutput = 'output/tree-output.out'

    def iterateThroughFiles(self):
        readers = []
        for pathToFile in self.pathToFiles:
            dataFilesReader = DataFilesReader(pathToFile)
            dataFilesReader.getData()

            readers.append(dataFilesReader)

        self.readers = readers

    def generateSolutions(self):
        functionPicker = FunctionPicker()

        log_output_file = open(self.logoutput, 'w+')
        biggest_score = 0

        for i in range(200):
            print('Iteration:' + str(i))
            random_nr = random.randint(2, len(self.readers[0].trainValues))
            function_number = random.randint(0, 6)
            random_indexes = []
            for nr in range(random_nr):
                random_indexes.append(random.randint(0, len(self.readers[0].trainValues) - 1))

            score = 0
            for reader in self.readers:
                values = []
                for index in random_indexes:
                    values.append(reader.trainValues[index])

                reader.trainValues.append(functionPicker.random_applier(values, function_number))
                score_index = round(255 * reader.trainValues[-1])
                score = score + reader.fmeans[score_index]

            log_output_file.write(str(random_nr) + ' ')

            for index in range(random_nr):
                log_output_file.write(str(random_indexes[index]) + ' ')

            log_output_file.write(str(function_number) + ' ' + str(score / len(self.readers)) + '\n')

            if (score / len(self.readers) > biggest_score):
                biggest_score = score / len(self.readers)

        print(biggest_score)
        log_output_file.close()
        self.getBestTree(biggest_score)

    def getBestTree(self, biggest_score):
        tree_output_file = open(self.treeoutput, 'w+')
        
        with open(self.logoutput, 'r') as file:
            my_reader = csv.reader(file, delimiter=' ')

            for row in my_reader:
                # print(str(row[-1]) + ' ' + str(biggest_score) + ' ' + str(biggest_score == float(row[-1])))
                for index in range(len(row) - 1):
                    tree_output_file.write(row[index] + ' ')
                tree_output_file.write(row[-1] + '\n')

                if (float(row[-1]) == biggest_score):
                    break

        tree_output_file.close()
        os.remove(self.logoutput)


    def startAlgorithm(self):
        self.iterateThroughFiles()
        self.generateSolutions()

if __name__ == "__main__":
    predictor = Predictor("input/*.CSV")
    predictor.startAlgorithm()
