from PyExpansion.common import version_history


class PyExpansionVersionHistory(version_history.VersionHistoryBase):

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

    def version_4(self):
        return self.default_setup(
            application_name="PyMorseCode",
            version="0.0.1a20230626",
        )

    def version_5(self):
        return self.default_setup(
            application_name="common",
            version="0.0.1a20230628"
        )

    def version_6(self):
        return self.default_setup(
            application_name="PyDeadFish",
            version="0.0.1a20230630"
        )

    def version_7(self):
        return self.default_setup(
            application_name="common",
            version="0.0.1a20240225"
        )


c = PyExpansionVersionHistory()
test = False
if test:
    print("How many version:", c.total_version())
    print("Version list:", c.get_version_list())
    print("Latest version: ", c.get_latest_version())
    print("Last version information: ", c.get_version_info(c.get_latest_version()))

version = c.get_latest_version()
