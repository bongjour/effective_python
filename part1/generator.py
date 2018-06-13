def countdown(n):
    print("Counting down!")
    while n > 0:
        yield n
        n -= 1


c = countdown(5)

print(type(c))

print(next(c))

a = [1, 2, 3]
a_1 = iter(a)

print(type(a))
print(type(a_1))
