from PyExpansion.common import utils, message
from PyExpansion.application.PyIC import status_code_list
from PyExpansion.application.PyIC.country import Malaysia, Singapore


class PyIC(utils.BaseClass):

    def __init__(self, country, ic_word):
        self.country = country
        self.ic_word = ic_word
        self.py_ic = self._router()

    def _router(self):
        if self.country == "Malaysia":
            return Malaysia.PyIC(self.ic_word)
        elif self.country == "Singapore":
            return Singapore.PyIC(self.ic_word)
        else:
            return None

    def get_detail(self):
        if self._router():
            return self._router().get_detail()
        else:
            self.error_code = status_code_list.error_code_1
            return message.error_default_message(False)

    def check_error(self):
        if self._router():
            return self._router().check_error()
        else:
            return utils.BaseClass.check_error(self)
