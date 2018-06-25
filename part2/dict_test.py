default = {
    'name': 'dante',
    'age': 43,
    'education': [],
    'son': 'jour',
}

u = {'name': 'inomy'}
# default.update(u)

print(default)

u.update(default)

print(u)

d = dict()

print(d)


class TmpCls(object):
    def __init__(self, topic):
        self._topic = topic

    def __get_tp(self):
        return self._topic


v = TmpCls('my')
print(v._topic)
print(v._TmpCls__get_tp())