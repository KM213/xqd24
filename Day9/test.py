import sys

for line in sys.stdin:
    a = line.split()
    flag = int(a[0])
    for i in a[1:]:
        print(a)
        if int(i) < flag:
            flag = int(i)
    print(flag)