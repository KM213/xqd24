"""
Day2 10.11
"""
# 1. 转义字符:
#     n   换行
#     t   缩进
#     ”   定界符
#     ‘   定界符
#     \ 转义符号
# 2. 运算符
#     5. 身份运算符：is   is not
#     6. 成员运算符: in   not in
# 3. 数据类型转换
#   int()[仅转换符合数字格式的内容，否则报错]
#   float()[仅转换符合数字格式的内容，否则报错]
#   str()
#   bool()
# 4. 分支语句：if
#   if-else
#   if-elif-elif-else
# 5. 循环语句：while
#   循环变量
#   while 循环条件:
#       循环执行语句
#       循环变量值更新

def fun1():
    x = "\nis\\nisnis"
    y = "\"nin\"anoso"
    z = 'abcdefg'
    print(x)
    print(y)
    print(z)

def fun2():
    aa = 100
    bb = 100
    print(aa, bb)  # 100 100
    print(aa is bb)  # True
    print(id(aa), id(bb))
    aa = 200
    print(aa, bb)  # 200 100
    print(aa is bb)  # False
    print(id(aa), id(bb))

def fun3():
    x = 1.5
    print(x, int(x), type(int(x)), sep="\t")
    print(x, float(x), type(float(x)), sep="\t")
    x = "2.5"
    print(x, str(x), type(str(x)), sep="\t")
    print(x, bool(x), type(bool(x)), sep="\t")

def fun4():
    num = int(input("输入一个整数："))
    if num % 2 == 0:
        print(f"{num}是偶数")
    else:
        print(f"{num}是奇数")

def fun5():
    n = 0
    while n <= 100:
        if n % 3 == 0 and n % 5 == 0:
            print(n)
        n = n + 1

    mt = 8848
    p = 0.1
    count = 0
    while p <= (mt*1000):
        count += 1
        p = p * 2
        print(p, count)
    print(count)


if __name__ == '__main__':
    fun5()