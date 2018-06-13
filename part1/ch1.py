from urllib.parse import parse_qs
import logging

logging.basicConfig(filename='./ test.log', level=logging.DEBUG)
log = logging.getLogger(__name__)

my_values = parse_qs('red=5&blue=0&green=', keep_blank_values=True)

print(repr(my_values))

print('Red :       ', my_values.get('red'))
print('Green:      ', my_values.get('green'))
print('Opacity:    ', my_values.get('opacity'))

red = my_values.get('red', [''])[0] or 0
green = my_values.get('green', [''])[0] or 0
opacity = my_values.get('opacity', [''])[0] or 0

print('Red :       %r' % red)
print('Green:      %r' % green)
print('Opacity:    %r' % opacity)

# 5. 시퀀스를 슬라이스하는 방법을 알자.

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

first_twenty_items = a[:20]
last_twenty_items = a[-20:]

print(first_twenty_items)
print(last_twenty_items)

b = a[-0:]
print(b)  # n이 0이면 -일 경우 원본의 복사본을 만든다.

b = a[4:]
print('Before:     ', b)
b[1] = 99
print('After       ', b)
print('No Change   ', a)  # 원본에는 영향을 미치지 않는다.

b = a[:]
assert b == a and b is not a
print(b)  # 복사본을 얻는다.

b = a
print('Before ', a)
a[:] = [101, 102, 103]
assert a is b
print('After ', a)
print('b', b)
b[:] = [1, 2, 3]
print('b', b)
print('a', a)
