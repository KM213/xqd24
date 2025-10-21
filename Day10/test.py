import sys

n = int(input())
a = {}
for line in sys.stdin:
    key, value = map(int, line.split())
    if key in a.keys():
        a[key] += value
    else:
        a[key] = value
for k, v in sorted(a.items()):
    print(k, v)
