import pickle

from Models.address_book import AddressBook
from Models.phone import Phone
from Models.record import Record


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "No such contact found."
        except ValueError:
            return "Give me the correct name and phone please."
        except IndexError:
            return "Input is missing some arguments."
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


@input_error
def add_contact(args, address_book):
    name, phone = args
    record = Record(name)
    record.add_phone(phone)
    address_book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, address_book):
    name, new_phone = args
    record = address_book.data[name]
    record.phones = [Phone(new_phone)]
    return "Contact updated."


@input_error
def show_phone(args, address_book):
    name = args[0]
    phones = [phone.value for phone in address_book.data[name].phones]
    return ", ".join(phones)


@input_error
def show_all(address_book):
    for name, record in address_book.items():
        phones = ', '.join([phone.value for phone in record.phones])
        print(f"{name}: {phones}, Birthday: {record.birthday.value if record.birthday else 'Not set'}")


@input_error
def add_birthday(args, address_book):
    name, birthday = args
    address_book[name].add_birthday(birthday)
    return f"Birthday added for {name}."


@input_error
def show_birthday(args, address_book):
    name = args[0]
    contact = address_book.get(name, None)
    if contact and contact.birthday:
        return f"{name}'s birthday is on {contact.birthday.value}."
    return "Birthday not set or contact not found."


@input_error
def save_address_book(book, filename="addressbook.data"):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


@input_error
def load_address_book(filename="addressbook.data"):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return AddressBook()


def main():
    address_book = load_address_book()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        match command:
            case "close" | "exit":
                print("Good bye!")
                save_address_book(address_book)
                break
            case "hello":
                print("How can I help you?")
            case "add":
                print(add_contact(args, address_book))
            case "change":
                print(change_contact(args, address_book))
            case "phone":
                print(show_phone(args, address_book))
            case "all":
                show_all(address_book)
            case "add-birthday":
                print(add_birthday(args, address_book))
            case "show-birthday":
                print(show_birthday(args, address_book))
            case "birthdays":
                address_book.get_birthdays_per_week()
            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
