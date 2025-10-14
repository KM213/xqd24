"""
Day3 10.13
1. 循环控制语句：break（退出）、continue（跳过）
2. for循环:
        range()函数：生成一个序列
3. 字符串
        ASCII码
        字符串访问（下标）
        字符串切片
        字符串运算：+ 拼接    * 重复   in 存在   not in 不存在
        处理函数：
            len() ,
            find() ,
            count() ,
            replace() ,
            split() ,
            strip(),
            index()
"""
def fun1():
    i = 1
    while i:
        if i == 5:      # 跳过5
            i = i + 1
            continue
        elif i > 10:    # 只打印到10
            break
        else:
            print(i)
            i = i + 1

def fun2():
    # for aa in range(51):
    #     for bb in range(51):
    #         for cc in range(21):
    #             if (aa + bb + cc == 50) and (aa*1 + bb*2 + cc*5 == 100):
    #                 print(aa, bb, cc, aa*1 + bb*2 + cc*5)

    for i in range(6):
        print("*", end=" ")

    for i in range(6):
        print("*")

    for i in range(6):
        for j in range(i):
            print("*", end=" ")
        print("\n", end="")

    for i in range(2, 9, 3):
        print(i)

def fun31():
    x = input("输入一个字符：")
    if 48 <= ord(x) <= 57:
        print(f"{x}是数字")
    elif 65 <= ord(x) <= 90:
        print(f"{x}是大写字母")
    elif 97 <= ord(x) <= 122:
        print(f"{x}是小写字母")
    else:
        print(f"{x}是其他字符")
def fun32():
    str1 = "nouwdjao02h49sns9729dh39b33"
    # 查看字符串第15个元素的值：
    print(str1[14])
    # 查看字符串最后一个字符：
    print(str1[-1])
    # 查看字符串倒数第二个字符
    print(str1[-2])
def fun33():
    str1 = "j20an49sjs3l8fn49ss04n"
    # 查看字符串下标第15到20的内容：
    print(str1[15:21])
    # 查看字符串最后两个字符（倒数第二个和倒数第一个）
    print(str1[-2:])
    print(str1[2:15:2])
    print(str1[15:2:-1])

def fun34():
    num = input("输入一个手机号：")
    print(num[:3] + "****" + num[-4:])


if __name__ == '__main__':
    fun33()