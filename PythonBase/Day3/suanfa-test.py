def fun1():
    l1 = [1, 2, 3, 0, 0, 0]
    l2 = [2, 5, 6]
    m = 3
    n = 3

    i = 0
    j = 0
    while i < len(l1) and j < n:
        if l1[i] < l2[j] and l1[i] != 0:
            print("1")
            i = i+1
            print(i, j)
        elif l1[i] == l2[j]:
            print("2")
            l1[i+2:] = l1[i+1:-1]
            l1[i+1] = l2[j]
            print(i, j, l1, l2, sep="\t")
            j = j+1
            i = i+1
            print(i, j)
        elif l1[i] == 0:
            print("3")
            l1[i:] = l2[j:]
            print(i, j, l1, l2, sep="\t")
            break


if __name__ == '__main__':
    fun1()