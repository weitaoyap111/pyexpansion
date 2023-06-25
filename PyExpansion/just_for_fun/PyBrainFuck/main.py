"""
Allow character +-.,[]><

meaning of each symbol
> = increases memory pointer, or moves the pointer to the right 1 block.
< = decreases memory pointer, or moves the pointer to the left 1 block.
+ = increases value stored at the block pointed to by the memory pointer
- = decreases value stored at the block pointed to by the memory pointer
[ = like c while(cur_block_value != 0) loop.
] = if block currently pointed to value is not zero, jump back to [
, = like c getchar(). input 1 character.
. = like c putchar(). print 1 character to the console
"""


class BrainFuck(object):
    allow_symbol = "[]><+-.,"

    _ptr = 0  # initial pointer
    _array = [0]  # use for pointer

    _user_input = []  # to store user input
    _loop_table = {}
    _loop_stack = []
    _result_list = []

    def _decode_reset(self):
        self._ptr = 0
        self._array = [0]
        self._user_input = []
        self._loop_table = {}
        self._loop_stack = []
        self._result_list = []

    def _verify_decode(self, data):
        for x in data:
            if x not in self.allow_symbol:
                return False
        return True

    def _verify_encode(self, data):
        for x in data:
            try:
                ord(x)
            except:
                return False
        return True

    def check_value(self, min_v=0, max_v=255):
        value = self._array[self._ptr]
        if value > max_v:
            self._array[self._ptr] = min_v
        if value < min_v:
            self._array[self._ptr] = max_v

    def _inc_ptr(self, inc_v=1):
        self._ptr += inc_v
        if self._ptr > len(self._array) - 1:
            self._array.append(0)

    def _dec_ptr(self, dec_v=1):
        self._ptr -= dec_v
        if self._ptr < 0:
            self._ptr = 0

    def _inc_ptr_v(self, inc_v=1):
        self._array[self._ptr] += inc_v
        self.check_value()

    def _dec_ptr_v(self, dec_v=1):
        self._array[self._ptr] -= dec_v
        self.check_value()

    def print_out(self, return_data=False):
        if not return_data:
            print(chr(self._array[self._ptr]), end="")
        self._result_list.append(chr(self._array[self._ptr]))

    def read_input(self):
        if not self._user_input:
            self._user_input = list(input("Your Input: "))
        self._array[self._ptr] = ord(self._user_input.pop(0))

    def left_loop(self, count):
        if not self._array[self._ptr]:
            count = self._loop_table[count]
        return count

    def right_loop(self, count):
        if self._array[self._ptr]:
            count = self._loop_table[count]
        return count

    def _decode(self, data, return_data):
        for count, x in enumerate(data):
            if x == "[":
                self._loop_stack.append(count)
            elif x == "]":
                begin_index = self._loop_stack.pop()
                self._loop_table[begin_index] = count
                self._loop_table[count] = begin_index

        count = 0
        while count < len(data):
            x = data[count]
            if x == "+":
                self._inc_ptr_v()
            elif x == "-":
                self._dec_ptr_v()
            elif x == ">":
                self._inc_ptr()
            elif x == "<":
                self._dec_ptr()
            elif x == ".":
                self.print_out(return_data)
            elif x == ",":
                self.read_input()
            elif x == "[":
                count = self.left_loop(count)
            elif x == "]":
                count = self.right_loop(count)

            count += 1

    def bf_to_word(self, data, return_data=False):
        if self._verify_decode(data):
            self._decode_reset()
            self._decode(data, return_data)
            if return_data:
                return self._result_list
        else:
            if return_data:
                return "Invalid format"
            else:
                print("Invalid format")

    def _encode(self, data):
        output_list = list()
        prev = 0
        for count, x in enumerate(data):
            if count == 0:
                word = "+" * ord(x)
            else:
                if ord(x) > prev:
                    word = "+" * (ord(x) - prev)
                elif ord(x) < prev:
                    word = "-" * (prev - ord(x))
                else:
                    word = ""
            prev = ord(x)
            word += "."
            output_list.append(word)

        return output_list

    def word_to_bf(self, data, return_data=False):
        if self._verify_encode(data):
            return self._encode(data)
        else:
            if return_data:
                return "Invalid format"
            else:
                print("Invalid format")
