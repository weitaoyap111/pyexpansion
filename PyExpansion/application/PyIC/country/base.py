from PyExpansion.common import utils
from PyExpansion.application.PyIC import status_code_list


class PyICBase(utils.BaseClass):
    country = ""  # country name
    separator = "-"  # symbol use in ic for separator purpose
    max_length_after_separator = 3  # how many group separate by separator
    ic_pattern = ""  # pattern of ic, # mean number, C mean character, S mean symbol
    symbol_list = "[@_!#$%^&*()<>?/\\|}{~:]"  # use for symbol check
    abc_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, ic_word: str):
        self.ic_word = ic_word

    def _valid_length(self):
        return True if len(self.ic_word) == len(self.ic_pattern) else False

    def _check_ic_word_same_as_pattern(self):
        for count, x in enumerate(self.ic_pattern):
            if x == "#":  # number
                try:
                    v = int(self.ic_word[count])
                except:
                    return False
            elif x == "C":  # character
                return False if self.ic_word[count] not in self.abc_list else True
            elif x == "S":  # symbol
                return False if self.ic_word[count] not in self.symbol_list else True
            else:
                return False
        return True

    def _verify(self):
        if not self._valid_length():
            self.error_code = status_code_list.error_code_3
            return None
        else:
            if not self._check_ic_word_same_as_pattern():
                self.error_code = status_code_list.error_code_2
                return None
            else:
                return self.ic_word
