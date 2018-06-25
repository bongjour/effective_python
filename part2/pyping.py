from typing import NamedTuple


class Student(NamedTuple):
    name: str = None
    age: int = 42


student = Student("dante")

print(student)
print(*student)
print(type(student))


class NamedTupleObject(NamedTuple):
    pass


class TargetUrlHolder(NamedTupleObject):
    url: str = None
    visit_period: int = 86400


targetUrl = TargetUrlHolder("http://google.co.kr")
print(targetUrl)


