from PyExpansion.common import table


class MathBaseTable(table.BaseTable):

    symbol = ""

    def __init__(self, row, col):
        self._check_symbol()
        self.row = row
        self.col = col
        self.size = self.row * self.col

    def _check_symbol(self):
        if not self.symbol:
            raise Exception("symbol must be set")

    def _large_space(self):
        return str(len(str(self.operation(self.row, self.col))) + 1)

    def create_table(self, row_no=0, column_no=0, exclude_list=None):
        if not row_no:
            row_no = self.row
        if not column_no:
            column_no = self.col
        data_x = [x for x in range(0, column_no + 1)]
        data_y = [y for y in range(0, row_no + 1)]
        new_data = list()
        for count, y in enumerate(data_y):
            temp = []
            for count2, x in enumerate(data_x):
                break_flag = False
                if exclude_list:
                    for coord_y, coord_x in exclude_list:
                        if count == coord_y - 1 and count2 == coord_x - 1:
                            temp.append(" ")
                            break_flag = True
                            break

                if not break_flag:
                    if count == 0 and count2 == 0:
                        temp.append(self.symbol)
                    if count == 0 and count2 > 0:
                        temp.append(x)
                    if count > 0 and count2 == 0:
                        temp.append(y)
                    if count > 0 and count2 > 0:
                        temp.append(self.operation(x, y))
            new_data.append(temp)
        return new_data

    def operation(self, a, b):
        return 0


class AdditionTable(MathBaseTable):
    symbol = "+"

    def operation(self, a, b):
        return a + b


class MultiplicationTable(MathBaseTable):
    symbol = "x"

    def operation(self, a, b):
        return a * b


class SquareTable(MathBaseTable):
    symbol = "2"

    def operation(self, a, b):
        return a ** b


if __name__ == "__main__":
    AdditionTable(10, 10).print_out()
    MultiplicationTable(10, 10).print_out()
    SquareTable(10, 10).print_out()
