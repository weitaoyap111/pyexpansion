class BaseTable:

    def larget_space(self, *args, **kwargs):
        data = self.create_table()
        max_len = 0
        for x in data:
            for y in x:
                max_len = max(max_len, len(str(y)))
        return max_len

    def create_table(self, *args, **kwargs):
        return []

    def print_out(self, *args, **kwargs):
        space = self.larget_space()
        end = kwargs.get("end", " ")
        table_data = self.create_table()
        for row in table_data:
            for item in row:
                print(f"{str(item):>{space}}", end=end)
            print()
