from ...common import os_stuff


class PypiDirectoryCreator(object):
    folder_lists = ["docs", "scripts", "src", "tests"]
    file_lists = ["LICENSE.txt", "CHANGES.txt", "MANIFEST.in", "README.txt", "pyproject.toml", "setup.py", "setup.cfg"]

    def __init__(self, folder_name=""):
        self.folder_name = folder_name

    def _create_multi_folder(self, lists):
        for x in lists:
            os_stuff.create_folder(self.folder_name + "/" + x)

    def _create_multi_file(self, lists):
        for x in lists:
            os_stuff.create_file(self.folder_name + "/" + x)

    def _create_package_name(self):
        folder_name = input("Your package name: ")

        if os_stuff.check_folder_name(folder_name):
            self.folder_name = folder_name
        else:
            print("Package name is not valid, please choose other")

    def main(self):
        while self.folder_name == "":
            self._create_package_name()

        os_stuff.create_folder(self.folder_name)
        self._create_multi_folder(self.folder_lists)
        self._create_multi_file(self.file_lists)
        print("file settings can refer to this urls: https://www.freecodecamp.org/news/how-to-create-and-upload-your"
              "-first-python-package-to-pypi/")
        print("Create Done")


if __name__ == "__main__":
    PypiDirectoryCreator().main()
