import pandas as pd
import csv

class DataFilesReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def getData(self):
        with open(self.filepath, 'r') as file:
            my_reader = csv.reader(file, delimiter=',')
            line_number = 0
            for row in my_reader:
                if line_number == 0:
                    self.expectedValue = float(row[0])
                    self.tresholds = [float(x) for x in list(filter(lambda a: a != '', row[1:]))]
                    line_number = line_number + 1
                else:
                    self.fmeans = [float(x) for x in list(filter(lambda a: a != '', row))]

        self.trainValues = self.tresholds[0:9]
        self.validationValues = self.tresholds[9:-1]
        self.testValues = self.tresholds[-1]

    def getMean(self):
        mean = 0
        for value in self.tresholds:
            mean = mean + value
        
        return mean / len(self.tresholds)