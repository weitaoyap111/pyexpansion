from . import http_code

# main list
http_code_list = http_code.HTTP_STANDARD
http_code_list.update(http_code.HTTP_NOT_STANDARD)


def get_code_description(code: str, code_list=None):
    if code_list is None:
        code_list = http_code_list
    return code_list[code]
