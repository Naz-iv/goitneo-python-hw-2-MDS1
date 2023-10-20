def input_error(func: type) -> type:
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except UserNotFoundError:
            return f"Contact with name {args[0][0]} not in contact list"
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Name was not provided. Please enter valid name!"
    return inner


@input_error
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: tuple, contacts: dict) -> str:
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."


@input_error
def change_phone(args: tuple, contacts: dict) -> str:
    name, phone = args
    if not contacts.get(name):
        raise UserNotFoundError
    contacts[name.capitalize()] = phone
    return "Contact updated."


@input_error
def get_phone(args: tuple, contacts: dict) -> int | str:
    name = args
    if not contacts.get(name[0]):
        raise UserNotFoundError
    return contacts.get(name[0].capitalize())


def get_all_contacts(contacts: dict) -> str:
    return "\n".join([f"{name} {phone}" for name, phone in contacts.items()])


class UserNotFoundError(Exception):
    pass
