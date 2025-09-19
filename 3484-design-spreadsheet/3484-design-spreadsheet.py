class Spreadsheet:

    def __init__(self, rows: int):
        self.mp = {}


    def setCell(self, cell: str, value: int) -> None:
        self.mp[cell] = value

    def resetCell(self, cell: str) -> None:
        self.mp.pop(cell,None)

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split("+", 1)
        return self.token_val(x) + self.token_val(y)

    def token_val(self, token):
        return int(token) if token.isdigit() else self.mp.get(token, 0)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)