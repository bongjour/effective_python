c = type('Foo', (), {'bar': True})

d = c()

print(type(c))
print(str(d))
