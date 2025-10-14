"""
Day3 10.13
练习
"""

# Part 1
def fun1():
    # 99乘法表
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j} × {i} = {i * j}", end="\t|\t")
        print()

# Part 2
# 求字符串"adafbe12aaa44324dafb"的长度。
def fun2():
    str1 = "adafbe12aaa44324dafb"
    l = len(str1)
    i = 0
    for s in str1:
        i = i + 1
    print(l, i)
# 求字符串"adafbe12aaa44324dafb"中字母 'a',出现的次数。
def fun3():
    str1 = "adafbe12aaa44324dafb"
    count = 0
    for i in str1:
        if i == 'a' and ord(i) == 97:
            count += 1
    print(count)
# 输出字符串"adafbe12aaa44324dafb"中，下标从5开始到 10的字符。
def fun4():
    str1 = "adafbe12aaa44324dafb"
    for i in range(5, 11):
        print(i, str1[i])





if __name__ == '__main__':
    fun4()