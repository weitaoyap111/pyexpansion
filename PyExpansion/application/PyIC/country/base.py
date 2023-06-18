from PyExpansion.common import utils
from PyExpansion.application.PyIC import status_code_list


class PyICBase(utils.BaseClass):
    country = ""  # country name
    ic_length = 12  # length of the ic
    separator = "-"  # symbol use in ic for separator purpose
    max_length_after_separator = 3  # how many group separate by separator

    def __init__(self, ic_word: str):
        self.ic_word = ic_word

    def _get_data_after_separator(self):
        return self.ic_word.split(self.separator)

    def _valid_length(self):
        return True if len(self.ic_word) == self.ic_length else False

    def _verify(self):
        get_data = self._get_data_after_separator()
        if len(get_data) == 1 or len(get_data) == self.max_length_after_separator:
            flag = True
        else:
            flag = False

        if not flag:
            self.error_code = status_code_list.error_code_2
            return None
        else:
            if len(get_data) == 1:
                if not len(self.ic_word) == self.ic_length:
                    self.error_code = status_code_list.error_code_3
                    return None
                else:
                    return get_data[0]
            elif len(get_data) == self.max_length_after_separator:
                temp_ic_word = "".join(get_data)
                if not len(temp_ic_word) == self.ic_length:
                    self.error_code = status_code_list.error_code_3
                    return None
                else:
                    return temp_ic_word
            else:
                return None
