from datetime import datetime

from Models.field import Field


class Birthday(Field):
    def __init__(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format.")
        super().__init__(value)
