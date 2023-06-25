from datetime import datetime
import json

from PyExpansion.common import basic_function


class VersionHistoryBase(object):
    """
    version format: {{major version}}.{{minor version}}.{{patch version}}{{version|a}}{{date|yyyymmdd}}
    example: 0.0.1a20230618
    major version, minor version and patch version: must be in number (>=0)
    version: either alpha(a) or stable(s)
    date: last update
    """
    _length_of_date = 8

    _list_version = []

    def __init__(self):
        self._update_all()
        self.write_or_update_version_file()

    def default_setup(self, application_name, version, description="1st Version"):
        return {
            "application_name": application_name,
            "version": version,
            "description": description,
        }

    def _update_all(self):
        search_names = "version_"
        function_found_lists_v = list()
        list_functions = dir(self)

        for function_name in list_functions:
            if function_name.startswith(search_names):
                function_found_lists_v.append(function_name)

        for x in function_found_lists_v:
            if basic_function.check_function_exist(self, x):
                self._list_version.append(getattr(self, x)())

    def total_version(self):
        return len(self._list_version)

    def get_latest_version(self):
        return self._list_version[-1]["version"]

    def get_version_list(self):
        return self._list_version

    def get_version_info(self, version=None):
        if not version:
            version = self.get_latest_version()
        get_version = version.split(".")
        if len(get_version) != 3:
            raise Exception("Version pattern error")
        else:
            [major_version, minor_version, patch] = get_version
            patch_version = patch[:len(patch)-self._length_of_date-1]
            stable_alpha = patch[len(patch)-self._length_of_date-1:len(patch)-self._length_of_date]
            update_date = patch[len(patch)-self._length_of_date:len(patch)]

            return_data = dict()
            return_data.update({"major_version": major_version})
            return_data.update({"minor_version": minor_version})
            return_data.update({"patch_version": patch_version})
            return_data.update({"stable_alpha": "Stable" if stable_alpha == "s" else "Alpha"})
            return_data.update({"update_date": datetime.strptime(update_date, "%Y%m%d").date()})
            return return_data

    def write_or_update_version_file(self):
        with open("version.json", "w") as outfile:
            json.dump(self._list_version, outfile)
