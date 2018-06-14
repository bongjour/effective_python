numbers = [1, 2, 3, 4, 5, 6]
it = iter(numbers)
print(type(it))
if iter(numbers) is iter(numbers):
    print("if")
else:
    print("else")