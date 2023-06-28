class MorseCode(object):
    MORSE_CODE_LIST = {
        "A": "._",
        "B": "_...",
        "C": "_._.",
        "D": "_..",
        "E": ".",
        "F": ".._.",
        "G": "__.",
        "H": "....",
        "I": "..",
        "J": ".___",
        "K": "_._.",
        "L": "._..",
        "M": "__",
        "N": "_.",
        "O": "___",
        "P": ".__.",
        "Q": "__.",
        "R": "._.",
        "S": "...",
        "T": "_",
        "U": ".._",
        "V": "..._",
        "W": ".__",
        "X": "_.._",
        "Y": "_.__",
        "Z": "__..",
        "1": ".____",
        "2": "..___",
        "3": "...__",
        "4": "...._",
        "5": ".....",
        "6": "_....",
        "7": "__...",
        "8": "___..",
        "9": "____.",
        "0": "_____",
    }

    def _get_data(self, character: str):
        try:
            return self.MORSE_CODE_LIST[character.upper()]
        except KeyError:
            return "|"

    def decode(self, morse_code):
        word = ""
        morse_code_lists = morse_code.split(" ")
        for morse_code_list in morse_code_lists:
            count = 0
            for count, data in enumerate(self.MORSE_CODE_LIST):
                if self.MORSE_CODE_LIST[data] == morse_code_list:
                    word += data
                    break
            if count == len(self.MORSE_CODE_LIST) - 1:
                word += " "
        return word

    def encode(self, word):
        morse_code = ""
        for count, w in enumerate(word):
            morse_code += self._get_data(w)
            if count != len(word) - 1:
                morse_code += " "
        return morse_code
