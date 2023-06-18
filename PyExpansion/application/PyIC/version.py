from PyExpansion.common import version_history


class PyICVersionHistory(version_history.VersionHistoryBase):

    @staticmethod
    def version_1():
        return "0.0.1a20230618"

    @staticmethod
    def description_for_version_1():
        description = """
        1st Version 
        """
        return description


c = PyICVersionHistory()
print(c.total_version())
print(c.get_latest_version())
print(c.get_version_info(c.list_version[0]))
