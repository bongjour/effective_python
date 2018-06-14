from collections import defaultdict

current = {'green': 12, 'blue': 3}

increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9)
]

result = defaultdict(lambda: 0, current)

print('Before:', dict(result))

for key, amount in increments:
    result[key] += amount

print('After:', dict(result))
