from . import message


class BaseClass(object):
    error_code = ""  # error code
    correct_code = ""  # correct code

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
        return_data = {}
        if self.error_code:
            return_data.update({"Error Code": self.error_code})
            return_data.update({"Error Message": message.get_code_description(self.error_code)})
        if self.correct_code:
            return_data.update({"Correct Code": self.correct_code})
        return return_data

    """
    main core to verify function
    """
    def _verify(self):
        return None

    """
    main function to get value from _verify function
    """
    def get_info(self):
        return self._verify()

    """
    main function to process data
    """
    def get_detail(self):
        return None
