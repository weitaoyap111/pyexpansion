# common calender
common_day_name = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", ]


def get_short_name(day_name_lists: list):
    new_day_name_list = []
    for day_name in day_name_lists:
        new_day_name_list.append(day_name[0])
    return new_day_name_list


test = True
if test:
    print(get_short_name(common_day_name))
