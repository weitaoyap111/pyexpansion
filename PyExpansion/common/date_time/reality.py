from PyExpansion.common.date_time import utils as datetime_utils


# TODO undone


class ActualDateTimeInEarth(object):
    """
    source: https://airandspace.si.edu/stories/editorial/science-leap-year#:~:text=Over%20time%2C%20these%20extra%2044,400%2C%20leap%20year%20is%20skipped.
    """
    day_in_a_year = 365.2425
    four_year_between_sidereal_year_calender_year = 23.262222

    def convert_day_to_readable_date(self):
        days, hours, minutes, seconds = datetime_utils.convert_day_to_readable_date(self.day_in_a_year)
        return {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds,
        }


print(ActualDateTimeInEarth().convert_day_to_readable_date())
