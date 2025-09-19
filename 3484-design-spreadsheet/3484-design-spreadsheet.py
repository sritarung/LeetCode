class Spreadsheet:

    def __init__(self, rows: int):
        self.matrix = [[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.matrix[row][col] = value  

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - 65
        row = int(cell[1:]) - 1
        self.matrix[row][col] = 0

    def getValue(self, formula: str) -> int:
        expression = formula[1:]
        x, y = expression.split("+", 1)
        if x.isdigit() and y.isdigit():
            return int(x) + int(y)
        else:
            a = None
            b = None
            if not x.isdigit():
                row1, col1 = int(x[1:]) - 1, ord(x[0]) - 65
            else:
                a = int(x)
            if not y.isdigit():
                row2, col2 = int(y[1:]) - 1, ord(y[0]) - 65
            else:
                b = int(y)
            if a is None:
                a = self.matrix[row1][col1]
            if b is None:
                b = self.matrix[row2][col2]
            return a + b
