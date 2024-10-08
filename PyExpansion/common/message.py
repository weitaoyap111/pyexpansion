
def return_response(code: int, message: str, info=None):
    return {"code": code, "message": message, "info": info}


def return_single_response(message: str):
    return {"message": message}


def return_response_with_code_list(code: str, list_code=None, info=None):
    """
    :param code: response status
    :param list_code: list of the code, default is use code_list
    :param info: information that bring from function to function, default is None
    :return: code, flag [True if info is none else false], message of the code, information
    """
    return_data = dict()
    return_data.update({"code": code})
    return_data.update(error_default_message(True) if info else error_default_message(False))
    return_data.update({"message": list_code[code]})
    return_data.update({"info": info})
    return return_data


def error_default_message(error: bool):
    return {"flag": error}
