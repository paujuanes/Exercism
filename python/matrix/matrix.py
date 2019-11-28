class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string

    def row(self, index):
        rows = self.matrix.split('\n')
        row = [int(num) for num in rows[index-1].split(' ')]
        return row

    def column(self, index):
        rows = self.matrix.split('\n')
        rowsCln = [rows[i].split(' ') for i in range(len(rows))]
        col = [int(rowsCln[i][index-1]) for i in range(len(rows))]
        return col
