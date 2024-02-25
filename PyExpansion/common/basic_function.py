
def check_function_exist(base, function_name):
    """
    this function is to check function is exist
    :param base:
    :param function_name:
    :return:
    """
    valid_function = getattr(base, function_name, None)
    return callable(valid_function)
