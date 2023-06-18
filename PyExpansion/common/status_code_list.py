# common
from PyExpansion.common.data_type.lists import status_code_list as dtl_scl

# application
from PyExpansion.application.PyIC import status_code_list as pyic_scl
# from PyExpansion.application.PyCarPlate import status_code_list as pycp_scl

# main list
code_list = {
    # common
    "200": "OK",
    "500": "Server Internal Error",
}

# common
# lists
code_list.update(dtl_scl.code_list)

# application
# PyIC
code_list.update(pyic_scl.code_list)

# PyCarPlate
# code_list.update(pycp_scl.code_list)
