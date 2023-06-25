from PyExpansion.common import message
from PyExpansion.application.human_resource.PyIC.country import base
from PyExpansion.application.human_resource.PyIC import status_code_list


class PyIC(base.PyICBase):
    country = "Singapore"
    word_pattern = "C########"

    """
    @xxxxxxx#
    
    @ is a letter that can be "S", "T", "F", "G" or "M" depending on the status of the holder.
    Singapore citizens and permanent residents born before 1 January 2000 are assigned the letter "S".
    Singapore citizens and permanent residents born on or after 1 January 2000 are assigned the letter "T".
    Foreigners issued with long-term passes before 1 January 2000 are assigned the letter "F".
    Foreigners issued with long-term passes from 1 January 2000 to 31 December 2021 are assigned the letter "G".
    Foreigners issued with long-term passes on or after 1 January 2022 are assigned the letter "M"
    
    xxxxxxx is a 7-digit serial number assigned to the document holder
    
    # is the checksum letter calculated with respect to @ and xxxxxxx
    """

    first_character_list = {
        "S": [True, "past-2000"],
        "T": [True, "2000-now"],
        "F": [False, "<2000"],
        "G": [False, "2000-2022"],
        "M": [False, "2022-now"],
    }

    def _first_character_function(self, character):
        """
        :param character: first character
        :return: [citizen, year birth]
        """
        try:
            return self.first_character_list[character]
        except:
            return [None, None]

    # valid ic
    """
    If the IC starts with S or T: 0=J, 1=Z, 2=I, 3=H, 4=G, 5=F, 6=E, 7=D, 8=C, 9=B, 10=A
    If the IC starts with F or G: 0=X, 1=W, 2=U, 3=T, 4=R, 5=Q, 6=P, 7=N, 8=M, 9=L, 10=K
    """

    valid_list = {
        "1": "JZIHGFEDCBA",
        "0": "XWUTRQPNMLK",
    }

    def valid_ic(self):
        choice = self.word[0]

        # calc
        v_list = 0
        multiple_v = [2, 7, 6, 5, 4, 3, 2]
        for x in range(1, 8):
            v_list += int(self.word[x]) * multiple_v[x-1]

        v_list = v_list % 11

        if choice == "S" or choice == "T":
            return self.valid_list["1"][v_list] == self.word[len(self.word)-1]
        elif choice == "F" or choice == "G" or choice == "M":
            return self.valid_list["0"][v_list] == self.word[len(self.word)-1]
        else:
            return None

    def get_detail(self):
        if not self.get_info():
            return message.error_default_message(False)
        else:
            temp = self.get_info()
            [citizen, valid] = self._first_character_function(temp[0])
            checksum = temp[len(temp)-1]
            self.correct_code = status_code_list.correct_code
            return {"citizen": citizen, "birth year range": valid, "checksum": checksum, "error": False}
