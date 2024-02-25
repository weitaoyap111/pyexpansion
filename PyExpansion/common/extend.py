

class ListExpand(list):
    def __init__(self, iterable=None):
        self.iterable = iterable
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    # product list that ignore certain condition
    def create(self, start, end, all_even_odd="", ignore_list=None):
        """
        :param start: starting number of the list
        :param end: end number of the list
        :param all_even_odd: default none, element condition in list, "e" mean even, 'o' mean odd
        :param ignore_list: optional,
        :return:
        """
        if ignore_list is None:
            ignore_list = list()
        temp_list = []
        for x in range(start, end+1):
            skip = False
            if ignore_list:
                for y in ignore_list:
                    if x == y:
                        skip = True
            if not skip:
                if all_even_odd == "e":
                    if x % 2 == 0:
                        temp_list.append(x)
                elif all_even_odd == "o":
                    if x % 2 == 1:
                        temp_list.append(x)
                else:
                    temp_list.append(x)
        super().extend(temp_list)

    def is_empty(self):
        return False if len(self.iterable) == 0 else True

    def all_number(self):
        for x in self.iterable:
            try:
                float(x)
            except:
                raise Exception("all element list must be a number")
        return True

    def all_str(self):
        for x in self.iterable:
            try:
                str(x)
            except:
                raise Exception("all element in list must be a string")
        return True

    # check no zero in objects
    def no_zero(self):
        if self.all_number():
            for x in self.iterable:
                if float(x) == 0:
                    return False
            return True
        return []

    # increase the value in the list
    def inc(self, max_value=21, start=0, step=1):
        """
        :param max_value: max value of element in list, and will be 0(default) if more than 21
        :param start: starting value
        :param step: increment by
        :return:
        """
        max_length = len(self.iterable)
        self.iterable[max_length-1] += step

        # check increment
        for x in range(max_length):
            if self.iterable[max_length-x-1] == max_value:
                self.iterable[max_length-x-1] = start
                if(max_length-x-2) >= 0:
                    self.iterable[max_length-x-2] += 1
                else:
                    self.iterable.insert(0, 1)
        return self.iterable


class ListOperationFunction(object):

    def __init__(self, lists: list):
        self.lists = lists
        self.expand = ListExpand()

    # subtraction of lists
    def sub(self, start=0):
        if self.expand.all_number():
            result = self.lists[0]
            for x in self.lists:
                result -= x
            return result + start
        return []

    # multiple of lists
    def multi(self, start=0):
        if self.expand.is_empty():
            result = 1
            for x in self.lists:
                result *= x
            return result + start
        return None

    # division of lists
    def div(self, start=0):
        result = self.lists[0]
        if self.expand.is_empty():
            if self.expand.no_zero():
                for count, x in enumerate(self.lists):
                    if count >= 1:
                        result /= x
            return result + start
        return None
