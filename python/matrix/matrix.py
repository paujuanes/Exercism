class Matrix:
    def __init__(self, matrix_string):
        raw_matrix = matrix_string.split('\n')
        self.rows = [list(map(int, row.split(' '))) for row in raw_matrix]
        self.cols = list(map(list, zip(*self.rows)))

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.cols[index-1]
