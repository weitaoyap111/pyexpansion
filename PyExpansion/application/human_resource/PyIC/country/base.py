from PyExpansion.common import utils
from PyExpansion.application.human_resource.PyIC import status_code_list


class PyICBase(utils.PatternClass):
    country = ""
    code_list = status_code_list.code_list
