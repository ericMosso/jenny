from tabulate import tabulate

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

    def export(self):
        # TODO: Implement csv module
        pass

    # makes it so you can use the object inside of print() (see python magic methods)
    def __str__(self) -> str:
        output =\
            f'--- {self.name} ---\n'\
            f'headers = {self.headers}\n'\
            f'matrix ({self.numRows}row X {self.numCols}col)\n'

        output += tabulate(self.matrix, headers='firstrow', tablefmt='grid')

        return output