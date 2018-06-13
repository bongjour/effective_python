"""
file읽고 공백이 있는 index를 generator로 반환한다.
list대신 generator를 반환하자.
"""


def index_file(handle):
    offset = 0
    for line in handle:
        if line:
            yield offset
        for each in line:
            offset += 1
            if each == ' ':
                yield offset


def extract_pop_from(file_path):
    with open(file_path) as f:
        for line in f:
            yield int(line)


def nomalize_func(iter_func):
    total = sum(iter_func())
    result = []
    for val in iter_func():
        percent = 100 * val / total
        result.append(percent)
    return result


white_space_indexes = index_file(open("./gen_tmp.txt"))
print(list(white_space_indexes))

pops = extract_pop_from("./city_pop.txt")
# print(sum(pops))

total = 0
for each in pops:
    if each:
        total += each
print(total)

result = nomalize_func(lambda: extract_pop_from("./city_pop.txt"))
print(result)
