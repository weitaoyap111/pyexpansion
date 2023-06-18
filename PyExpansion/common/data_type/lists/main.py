from PyExpansion.common import message
from PyExpansion.common.data_type.lists import status_code_list


class ListExpansion(object):

    @staticmethod
    def compare_two_list_length(list1, list2):
        if len(list1) == len(list2):
            return message.return_response_with_code_list(status_code_list.correct_code_1, info=[list1, list2])
        else:
            return message.return_response_with_code_list(status_code_list.error_code_1)
