import pandas as pd
import csv

from Pixel import Pixel

class DataFileReaderLocal:
    def __init__(self, filepath):
        self.filepath = filepath
        self.pixelsList = []


    def getData(self):
        with open(self.filepath, 'r') as file:
            my_reader = csv.reader(file, delimiter=',')
            for row in my_reader:
                pixelValue = float(row[0])
                pixelGroundType = int(row[1])
                pixelTresholds = [float(x) for x in list(filter(lambda a: a != '', row[2:]))]
                self.pixelsList.append(Pixel(pixelValue, pixelGroundType, pixelTresholds))
