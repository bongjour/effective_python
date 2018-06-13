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
