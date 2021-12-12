import dataclasses
from collections import namedtuple


#  1
class Laptop:
    def __init__(self):
        battery = Battery('This battery belongs to this laptop')
        self.battery = battery


class Battery:
    def __init__(self, volt):
        self.volt = volt


# laptop = Laptop()
# print(laptop.battery.volt)

#  2
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString
guitar = Guitar(guitar_string)


#  3
class Calc:
    def add_nums(self, x, y, z):
        return x + y + z


Calc.add_nums = staticmethod(Calc.add_nums)
print(Calc.add_nums)


#  4
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pasta contains ({self.ingredients})'

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_carbonara = Pasta.carbonara()
pasta_bolognaise = Pasta.bolognaise()
print(pasta_carbonara)
print(pasta_bolognaise)


#  5
class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)


#  6
@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


#  7
address_book_data_class = namedtuple('data',
                                     ['key',
                                      'name',
                                      'phone_number',
                                      'address',
                                      'email',
                                      'birthday',
                                      'age'])


# data = address_book_data_class(1,
#                                'Alex,',
#                                'two five',
#                                'Sky',
#                                'sasha@gmail.com',
#                                'today',
#                                21)


#  8
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.mail = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'addresbook {self.key,}, {self.name}, {self.phone_number},' \
               f' {self.address}, {self.mail}, {self.birthday}, {self.age} '


addressbook = AddressBook(key=1,
                          name='Alex',
                          phone_number='two five',
                          address='Sky',
                          email='sasha@gmail.com',
                          birthday='today',
                          age=21)
print(addressbook)


#  9
class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def person_age(self):
        return self.age

    @person_age.setter
    def person_age(self, value):
        self.age = value


john = Person('John', 36, 'USA')
john.person_age = 25


#  10
class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


student = Student(0, 'Alex')
setattr(student, 'email', 'alex@gmail.com')
print(getattr(student, 'email'))


# #  11
# class Celsius:
#     def __init__(self, temperature=0):
#         self.temperature = temperature
#
#     def __repr__(self):
#         return repr(self.temperature)
#
#     @property
#     def temp_convert(self):
#         return self.temperature
#
#     @temp_convert.setter
#     def temp_convert(self, value):
#         self.temperature = value
#
#
# celsius = Celsius()
# fahrenheit = (celsius.temperature * 1.8) + 32
# print(fahrenheit)