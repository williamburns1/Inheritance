class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone)


class Customer(Person):
    def __init__(self, name, address, phone, pnumber, mlist):
        Person.__init__(self, name, address, phone)
        self.__pnumber = pnumber
        self.__mlist = mlist

    def print_person(self):
        print(self.__name)
        print(self.__address)
        print(self.__phone)
        print(self.__pnumber)
        print(self.__mlist)
