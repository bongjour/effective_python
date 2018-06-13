from itertools import zip_longest

names = ['dante', 'beerang', 'sonic']

letters = [len(each) for each in names]

longest_name = None
max_letter = 0

# for i, name in enumerate(names):
#     count = letters[i]
#
#     if count > max_letter:
#         longest_name = name
#         max_letter = count


for name, count in zip(names, letters):
    if count > max_letter:
        longest_name = name
        max_letter = count

print(max_letter)
print(longest_name)

names.append('billy')  # zip은 크기가 틀리면 이상하게 동작한다.
for name, count in zip(names, letters):
    print(name)

for name, count in zip_longest(names, letters):
    print(name, count)
