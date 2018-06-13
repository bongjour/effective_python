words_count = [len(word) for word in open("./tmp/words.txt")]

print(words_count)

it = (len(word) for word in open("./tmp/words.txt"))

# for each in it:
#     print(each)
#
# print("done")
# for each in it:  # 에러는 나지 않지만 it는 이미 소비 되었다.
#     print(each)

roots = ((x, x ** 0.5) for x in it)

print(type(roots))
print(type(next(roots)))

# for root in roots:
#     print(root)
