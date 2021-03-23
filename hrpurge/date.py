import arrow

from hrpurge.const import DATA_FORMAT


class Date:
    def __init__(self) -> None:
        self._data_format = DATA_FORMAT

    def get_date_now(self):
        return arrow.utcnow().format(self._data_format)

    def get_date_now_shift_days(self, days=-15):
        return arrow.utcnow().shift(days=days).format(self._data_format)

    @staticmethod
    def one_date_is_greater_than_another(date_one, date_another):
        return date_one > date_another
