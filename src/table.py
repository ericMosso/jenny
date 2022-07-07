import os
import csv
from tabulate import tabulate
from config import PROJECT_ROOT

class Table:

    # constructor (see python magic methods)
    def __init__(self, name: str, headers: list) -> None:
        self.name = name
        self.headers = headers
        self.numCols = len(headers)
        self.numRows = 1
        self.matrix = [headers]

    def addRow(self, *values) -> None:
        row = []
        for val in values:
            row.append(val)

        self.matrix.append(row)
        self.numRows += 1

    def export(self, filename: str, append=True):
        # create output directory if doesn't exist
        outputDir = os.path.join(PROJECT_ROOT, 'output')
        if not os.path.exists(outputDir):
            os.mkdir(outputDir)

        # output to {PROJECT_ROOT}/output/{filename}
        path = os.path.join(PROJECT_ROOT, 'output', filename)

        # ensure filename has .csv file extension
        ext = filename.split('.')[-1]
        if ext != 'csv':
            print ('Invalid filename in Table.export()')
            return

        # open file in append mode or replace mode
        if append and os.path.exists(path) and os.path.isfile(path):
            outfile = open(path, 'a')
        else:
            outfile = open(path, 'w')

        # create a file writer
        csvWriter = csv.writer(outfile, delimiter=',', dialect='unix')

        # write rows, skip header if append mode
        if append:
            headlessMatrix = self.matrix[1:]
            csvWriter.writerows(headlessMatrix)
        else:
            csvWriter.writerows(self.matrix)
        
        # close the file
        outfile.close()


    # makes it so you can use the object inside of print() (see python magic methods)
    def __str__(self) -> str:
        output =\
            f'--- {self.name} ---\n'\
            f'headers = {self.headers}\n'\
            f'matrix ({self.numRows}row X {self.numCols}col)\n'

        output += tabulate(self.matrix, headers='firstrow', tablefmt='grid')

        return output