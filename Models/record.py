from datetime import datetime
from Models.birthday import Birthday
from Models.name import Name
from Models.phone import Phone


class Record:
    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                break

    def find_phone(self, phone):
        return next((p for p in self.phones if p.value == phone), None)

    def add_birthday(self, birthday):
        try:
            datetime.strptime(birthday, "%d.%m.%Y")
            self.birthday = Birthday(birthday)
        except ValueError:
            raise ValueError("Birthday must be in DD.MM.YYYY format.")
