class DeadFish(object):
    """
    i - increment value by 1
    d - decrease value by 1
    s - square the value
    o - output
    """

    initial_value = 0

    def _reset(self):
        self.initial_value = 0

    def _verify(self, words):
        for word in words:
            if word not in "idso":
                return False
        return True

    def _check(self):
        if self.initial_value > 255 or self.initial_value < 0:
            self.initial_value = 0

    def i_f(self):
        self.initial_value += 1
        self._check()

    def d_f(self):
        self.initial_value -= 1
        self._check()

    def s_f(self):
        self.initial_value *= self.initial_value
        self._check()

    def o_f(self):
        print(chr(self.initial_value), end="")

    def _decode(self, words):
        self._reset()
        if not self._verify(words):
            print("Invalid Syntax")
        else:
            for x in words:
                if x == "i":
                    self.i_f()
                elif x == "d":
                    self.d_f()
                elif x == "s":
                    self.s_f()
                elif x == "o":
                    self.o_f()

    def decode(self, word):
        return self._decode(word)

    def _encode(self, word):
        self._reset()
        data_word = ""
        temp = [ord(x) for x in word]
        for count, x in enumerate(temp):
            """
            r = 'i' if x > 0 else 'd'
            data_word += abs(x) * r
            data_word += "o"
            """
            if count == 0:
                data_word += self._simplify(x)
            else:
                data_word += self._simplify(x, temp[count-1])
        return data_word

    def _simplify(self, value, start_number=0):
        import math
        record = ""
        sq_list = [x*x for x in range(1, 16)][::-1]
        if value > start_number:
            if start_number == 0:
                while value > 0:
                    if value % 2 == 0:
                        for x in sq_list:
                            if value == x:
                                value = math.sqrt(x)
                                record += "s"
                                break
                        else:
                            value -= 2
                            record += "ii"
                    else:
                        value -= 1
                        record += "i"
                record = record[::-1]
            else:
                starting = start_number
                ending = value
                while starting != ending:
                    if starting * starting <= ending:
                        starting *= starting
                        record += "s"
                    else:
                        starting += 1
                        record += "i"

                    if starting > ending:
                        starting -= 1
                        record += "d"
        else:
            record += "d" * (start_number - value)
        return record + "o"

    def encode(self, word):
        return self._encode(word)

