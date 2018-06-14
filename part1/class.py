import random
import time


class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def sum(self):
        return self.first + self.second


class MoreCalculator(Calculator):
    def sum(self):
        print("sum!!!!!")
        return self.first + self.second


cal1 = Calculator(1, 2)
print(cal1.sum())

cal2 = MoreCalculator(1, 3)
print(cal2.sum())

print(type(cal1))
print(type(cal1).__name__)
print(type(cal2).__bases__)

if isinstance(cal1, Calculator):
    print("Calculator!!")


class Account(object):
    num_account = 0
    name = None
    balance = None

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1

    def deposit(self, amt):
        self.balance = self.balance + amt

    def withdraw(self, amt):
        self.balance = self.balance - amt

    def inquiry(self):
        return self.balance


class EvilAccount(Account):
    def deposit(self, amt):
        super().withdraw(5)
        super().deposit(amt)

    def inquiry(self):
        if random.randint(1, 4) == 1:
            return self.balance * 1.10
        else:
            return self.balance


account1 = Account("dante's account", 1000)
print(account1.balance)

account2 = Account("sonic's account", 500)

print(account2.balance)

print(account2.num_account)
print(Account.num_account)

print(Account.balance)

print(account2.inquiry())

evil = EvilAccount("dante", 1000)
evil.deposit(100)
print(evil.inquiry())

for each in EvilAccount.__mro__:
    if each.__name__ == 'Account':
        print("It's a child of Account")


class X(object):
    pass


class Y(X):
    pass


# class Z(X, Y):
#     pass


class Duck(object):
    name = "dock"

    def print_name(self):
        print("dock!! dock!!")


class Dog(object):
    name = "dog"

    def print_name(self):
        print("dog!! dog!!")


def print_anything(animal):
    animal.print_name()


duck = Duck()
dog = Dog()

print_anything(dog)
print_anything(duck)


class NowDate(object):
    def __init__(self, year, month, day):
        print("created by __init__")
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def now():
        print("created by NowDate now")
        t = time.localtime()
        return NowDate(t.tm_year, t.tm_mon, t.tm_mday)

    @staticmethod
    def tomorrow():
        print("created by NowDate tomorrow")
        t = time.localtime(time.time() + 86400)
        return NowDate(t.tm_year, t.tm_mon, t.tm_mday)


class EuroNowDate(NowDate):
    ver = 1

    @classmethod
    def now(cls):
        print("created by EuroNowDate now")
        t = time.localtime()
        print(cls.mro())
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    @classmethod
    def change_version(cls):
        cls.ver = 2


# a = NowDate(2018, 4, 13)
# b = NowDate.now()
# c = NowDate.tomorrow()
# print(a.month)
# print(b.month)
# print(c.month)


d1 = EuroNowDate.now()
d2 = EuroNowDate.now()

print(d1.ver)
print(d2.ver)

EuroNowDate.change_version()

print(d1.ver)
print(d2.ver)
print(EuroNowDate.ver)


class Foo(object):
    def __init__(self, name):
        self.__name = name

    @property
    def special_name(self):
        return self.__name + "!! you're the best in the world"

    @special_name.setter
    def special_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string!")
        self.__name = value


foo = Foo('dante')
foo.special_name = "Dante"
# foo.special_name = 4
print(foo.special_name)
print(Foo.special_name)


class TypedProperty(object):
    def __init__(self, name, type, default=None):
        self.name = "_" + name
        self.type = type
        self.default = type() if default is None else default

    def __get__(self, instance, cls):
        return getattr(instance, self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, self.type):
            raise TypeError("Must be a %s" % self.type)
        setattr(instance, self.name, value)

    def __delete__(self, instance):
        raise AttributeError("Can't delete attribute")

    def __extract_name(self):
        return self.name

    def extract_name(self):
        return self.name


class Var(object):
    name = TypedProperty("dante", str)
    num = TypedProperty("dante", int)


