import os

ASCII_NOT_ALLOW_UNIX = ["/"]
ASCII_NOT_ALLOW_WIN = ["<", ">", ":", "/", "\\", "|", "?", "*"]
ASCII_NOT_ALLOW_NON_PRINT_UNIX = [chr(0)]
ASCII_NOT_ALLOW_NON_PRINT_WIN = [chr(x) for x in range(32)]
REVERSED_FILE_NAMES_UNIX = []
REVERSED_FILE_NAMES_WIN = [
    "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2",
    "LPT3, LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
]


def is_windows():
    return os.name == "nt"


def is_linux():
    return os.name == "posix"


# create folder
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return os.path.exists(folder_path)


# create file
def create_file(file_path, mode="w+", content=""):
    if not os.path.exists(file_path):
        with open(file_path, mode) as f:
            if content != "":
                f.write(content)


# check word is valid for create folder
def check_folder_name(name):
    if is_windows():
        ASCII_NOT_ALLOW = ASCII_NOT_ALLOW_WIN
        ASCII_NOT_ALLOW_NON_PRINT = ASCII_NOT_ALLOW_NON_PRINT_WIN
        REVERSED_FILE_NAMES = REVERSED_FILE_NAMES_WIN

    else:
        if is_linux():
            ASCII_NOT_ALLOW = ASCII_NOT_ALLOW_UNIX
            ASCII_NOT_ALLOW_NON_PRINT = ASCII_NOT_ALLOW_NON_PRINT_UNIX
            REVERSED_FILE_NAMES = REVERSED_FILE_NAMES_UNIX

        else:
            raise Exception("Unable to identify os type")

    for x in ASCII_NOT_ALLOW:
        if x in name:
            return False

    for x in ASCII_NOT_ALLOW_NON_PRINT:
        if x in name:
            return False

    for x in REVERSED_FILE_NAMES:
        if x == name:
            return False
    return True
