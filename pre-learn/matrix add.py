class Matrix:

    def __init__(self, date):
        self.date = date

    def __add__(self, other):
        a_row = len(self.date)
        a_col = len(self.date[0])

        b_row = len(other.date)
        b_col = len(other.date[0])

        if a_row != b_row and a_col != b_col:
            return "slfjgf"

        for row in range(a_row):
            for col in range(a_col):
                self.date[row][col] += other.date[row][col]

        return self

    def __str__(self):
        return str(self.date)


if __name__ == '__main__':
    a = Matrix([[1, 2], [3, 4]])
    b = Matrix([[5, 6], [7, 8]])
    print(a + b)



父母把我让你感觉不能问人家那个农夫你不给你给我如果你不GV尼日我给你温暖购物认同人体蜈蚣
