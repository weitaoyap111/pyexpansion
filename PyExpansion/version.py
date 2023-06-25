from PyExpansion.common import version_history


class PyICVersionHistory(version_history.VersionHistoryBase):

    def version_1(self):
        return self.default_setup(
            application_name="PyIC",
            version="0.0.1a20230618",
        )

    def version_2(self):
        return self.default_setup(
            application_name="PyIC",
            version="0.0.1a20230622",
            description="Singapore added"
        )

    def version_3(self):
        return self.default_setup(
            application_name="PyBrainFuck",
            version="0.0.1a20230624",
        )


c = PyICVersionHistory()
test = True
if test:
    print("How many version:", c.total_version())
    print("Version list:", c.get_version_list())
    print("Latest version: ", c.get_latest_version())
    print("Last version information: ", c.get_version_info(c.get_latest_version()))

version = c.get_latest_version()
