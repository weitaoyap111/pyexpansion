from datetime import datetime

from PyExpansion.common import basic_function


class VersionHistoryBase(object):
    """
    version format: {{major version}}.{{minor version}}.{{patch version}}{{version|a}}{{date|yyyymmdd}}
    example: 0.0.1a20230618
    major version, minor version and patch version: must be in number (>=0)
    version: either alpha(a) or stable(s)
    date: last update
    """
    application_name = ""
    list_version = []
    list_description = []
    length_of_date = 8

    def __init__(self):
        self._update_all()

    def _update_all(self):
        list_functions = dir(self)
        search_names1 = "version_"
        search_names2 = "description_for_version_"
        function_found_lists_v = list()
        function_found_lists_d = list()
        for function_name in list_functions:
            if function_name.startswith(search_names1):
                function_found_lists_v.append(function_name)
            if function_name.startswith(search_names2):
                function_found_lists_d.append(function_name)
        for x in function_found_lists_v:
            if basic_function.check_function_exist(self, x):
                self.list_version.append(getattr(self, x)())
        for x in function_found_lists_d:
            if basic_function.check_function_exist(self, x):
                self.list_description.append(getattr(self, x)())

    def total_version(self):
        return len(self.list_version)

    def get_latest_version(self):
        return self.list_version[-1]

    def get_version_info(self, version):
        get_version = version.split(".")
        if len(get_version) != 3:
            raise Exception("Version pattern error")
        else:
            [major_version, minor_version, patch] = get_version
            patch_version = patch[:len(patch)-self.length_of_date-1]
            stable_alpha = patch[len(patch)-self.length_of_date-1:len(patch)-self.length_of_date]
            update_date = patch[len(patch)-self.length_of_date:len(patch)]

            return_data = dict()
            return_data.update({"major_version": major_version})
            return_data.update({"minor_version": minor_version})
            return_data.update({"patch_version": patch_version})
            return_data.update({"stable_alpha": "Stable" if stable_alpha == "s" else "Alpha"})
            return_data.update({"update_date": datetime.strptime(update_date, "%Y%m%d").date()})
            return return_data
