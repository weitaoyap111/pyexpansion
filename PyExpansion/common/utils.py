from .constants import common as constants_common

front_pattern = "C_U_"

correct_code = front_pattern + "200"
error_code_0 = front_pattern + "500_0"
error_code_1 = front_pattern + "500_1"

code_list = {
    error_code_0: "",
    error_code_1: "",
}


class ErrorBase(object):
    error_code = ""  # error code
    correct_code = ""  # correct code
    code_list = None

    """
    reset all code
    """
    def reset(self):
        self.error_code = ""
        self.correct_code = ""

    """
    main function get function error code
    """
    def check_error(self):
        self.reset()
        self.get_detail()
        return_data = dict()
        if self.error_code:
            return_data.update({"Error Code": self.error_code})
            return_data.update({"Error Message": self.code_list[self.error_code]})
        if self.correct_code:
            return_data.update({"Correct Code": self.correct_code})
        return return_data

    """
    main core to verify function
    """
    def verify(self):
        return None

    """
    main function to get value from _verify function
    """
    def get_info(self):
        return self.verify()

    """
    main function to process data
    """
    def get_detail(self):
        return None


class PatternClass(ErrorBase):
    """
    A - capital alphabet (A~Z)
    a - small alphabet (a~z)
    # - number (0~9)
    S - symbol refer to constants/common.py
    """
    allow_character_in_pattern = "Aa#S"
    word_pattern = ""  # word pattern, example: AA##AAS
    symbol_list = constants_common.SPECIAL_SYMBOL  # use for symbol check
    abc_list = constants_common.CAPITAL_ABC
    bcode_list = code_list

    def __init__(self, word: str):
        self.word = word

    def _verify_length(self):
        return True if len(self.word) == len(self.word_pattern) else False

    def _check_word_same_as_word_pattern(self):
        for count, x in enumerate(self.word_pattern):
            if x == "#":  # number
                try:
                    int(self.word[count])
                except TypeError:
                    return False
            elif x == "C":  # character
                return False if self.word[count] not in self.abc_list else True
            elif x == "S":  # symbol
                return False if self.word[count] not in self.symbol_list else True
            else:
                return False
        return True

    def _verify(self):
        if not self._verify_length():
            self.error_code = self.bcode_list[error_code_0]
            return None
        else:
            if not self._check_word_same_as_word_pattern():
                self.error_code = self.bcode_list[error_code_1]
                return None
            else:
                return self.word


class GeneralUtils(object):

    @staticmethod
    def return_msg(is_success=True, message="", info=None):
        """
        :param is_success: Success or fail
        :param message: error message if false else ""
        :param info: display information needed
        :return:
        """
        return is_success, message, info
