import sys


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e


def none_return_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        return None


class CommonError(Exception):
    def __init__(self, error_no, msg):
        self.args = (error_no, msg)
        self.error_no = error_no
        self.msg = msg


class SpecificError(CommonError):
    pass


class SpecificErrorV2(CommonError):
    pass


try:
    result = divide(100, 2)
except ValueError as e:
    print("Error!!")
else:
    print("Succeed %d" % result)
finally:
    print("End!!")

res = none_return_divide(1, 1)
if res is None:
    print("Fail...")

res1 = sys.exc_info()
print(res1)