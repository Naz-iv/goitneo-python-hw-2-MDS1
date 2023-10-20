from collections import UserDict


class Field:
    def __init__(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other: str) -> bool:
        return self.value == other

    def __hash__(self) -> int:
        return super().__hash__()


class Name(Field):
    def __init__(self, value: str) -> None:
        if not value:
            raise ValueError("Name can't be empty")
        super().__init__(value)


class Phone(Field):
    def __init__(self, value: str) -> None:
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number should have 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        try:
            phone = Phone(phone)
            self.phones.append(phone)
        except ValueError as e:
            print(e)

    def remove_phone(self, phone: str) -> bool:
        if phone in self.phones:
            self.phones.remove(phone)
            return True
        print("Phone number is not in contact book.")
        return False

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        if old_phone in self.phones:
            self.phones[self.phones.index(old_phone)] = Phone(new_phone)
        else:
            print("Old phone number is not in contact book.")

    def find_phone(self, phone: str) -> str | None:
        if phone in self.phones:
            return self.phones[self.phones.index(phone)].value
        return None

    def __str__(self):
        return (f"Contact name: {self.name}, phones: "
                f"{'; '.join(phone.value for phone in self.phones)}")


class AddressBook(UserDict):

    def add_record(self, record: Record) -> None:
        self.data[record.name] = record

    def find(self, name: str) -> Record | None:
        for key in self.data.keys():
            if key.value == name:
                return self.data[key]
        print(f"{name} not in address book.")

    def delete(self, name: str) -> None:
        for key in self.data.keys():
            if key.value == name:
                self.data.pop(key)
                return
        print(f"{name} not in address book.")
