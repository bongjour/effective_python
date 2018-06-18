import collections
import pickle

TestObj = collections.namedtuple("TestObj", ('name', 'value'))

testobj = TestObj(name="dante", value=92)
path = "./test.bin"

with open(path, 'wb') as f:
    pickle.dump(testobj, f)

with open(path, 'rb') as f:
    data = pickle.load(f)

print(type(data))

serialized = pickle.dumps(testobj)
data = pickle.loads(serialized)
print(data)
