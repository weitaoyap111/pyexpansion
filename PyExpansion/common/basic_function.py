
def check_function_exist(base, function_name):
    valid_function = getattr(base, function_name, None)
    return callable(valid_function)
