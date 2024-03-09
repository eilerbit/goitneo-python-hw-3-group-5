from collections import UserDict, defaultdict
from datetime import datetime


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("No such contact found.")

    def get_birthdays_per_week(self):
        today = datetime.today().date()
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        weekend = ['Saturday', 'Sunday']

        birthdays_by_weekday = defaultdict(list)

        for user in self.data.values():
            if user.birthday:
                name = user.name.value
                birthday = datetime.strptime(user.birthday.value, "%d.%m.%Y").date()

                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                delta_days = (birthday_this_year - today).days

                if 0 <= delta_days < 7:
                    weekday = weekdays[(today.weekday() + delta_days) % 7]

                    if weekday in weekend:
                        weekday = 'Monday'

                    birthdays_by_weekday[weekday].append(name)

        for weekday, names in birthdays_by_weekday.items():
            print(f"{weekday}: {', '.join(names)}")
