"""
Day2 10.11
练习
"""
# Part 1
# 编写程序，让用户输入一个数字（可能是整数或小数），使用int()和float()进行类型转换后，分别输出转换后的结果及它们的数据类型。
def fun1():
    num = input("输入一个数字：")
    if "." in num:      # 输入的是小数的字符串
        y = float(num)
        print(y, type(y))
        z = int(y)
        print(z, type(z))
    else:               # # 输入的是整数的字符串
        x = int(num)
        print(x, type(x))
        y = float(num)
        print(y, type(y))

# 接收用户输入的两个值（例如 "5" 和 5），先用==判断是否相等，再用is判断是否为同一个对象，输出两次判断的结果并观察区别。
def fun2():
    # 浮点数
    val1 = float(input("请输入第一个值：") )   # 输入2.5
    val2 = float(input("请输入第二个值：") )   # 输入2.5
    print(f"val1 == val2  : {val1 == val2}")    # 输出True
    print(f"val1 is val2  : {val1 is val2}")    # 输出False
    val1 = 2.5
    val2 = 2.5
    print(f"val1 == val2  : {val1 == val2}")    # 输出True
    print(f"val1 is val2  : {val1 is val2}")    # 输出True

# 让用户输入一个字符串和一个字符，判断该字符是否在字符串中（使用in），并输出 "字符存在" 或 "字符不存在"。
def fun3():
    str1 = input("输入一个字符：")
    str2 = input("输入一个字符串：")
    if str1 in str2:
        print(f"字符 {str1} 在字符串 {str2} 中")
    else:
        print(f"字符 {str1} 不在字符串 {str2} 中")

# 编写程序，输入一个整数，将其转换为布尔值bool()后，判断结果是否为True，并解释为什么 0 转换为布尔值是False。
def fun4():
    num = int(input("请输入一个整数："))
    num_bool = bool(num)
    print(num_bool, type(num_bool))

# 接收用户输入的两个字符串，判断第一个字符串是否不包含第二个字符串（使用not in），输出判断结果。
def fun5():
    str1 = input("输入第一个字符串：")
    str2 = input("输入第二个字符串：")
    if str2 not in str1:
        print(f"字符串 {str2} 不在 {str1}中")
    else:
        print(f"字符串 {str2} 在 {str1}中")

# 让用户输入一个数字字符串（如 "123.45"），先转换为float类型，再转换为int类型，最后转换为str类型，依次输出每次转换的结果和类型。
def fun6():
    str1 = input("请输入一个内容为数字的字符串：")
    x = float(str1)
    print(x, type(x))
    y = int(x)
    print(y, type(y))
    z1 = str(y)
    print(z1, type(z1))
    z2 = str(x)
    print(z2, type(z2))

# 定义变量a = 100、b = 100、c = 200，使用is运算符比较a与b、a与c是否为同一个对象，输出结果并观察整数缓存机制的现象。
def fun7():
    a = 1000
    b = 1000
    c = 200
    print(f"a is b: {a is b}")
    print(f"id(a) = {id(a)}   id(b) = {id(b)}")
    print(f"a is c: {a is c}")
    print(f"id(a) = {id(a)}   id(c) = {id(a)}")

# 输入一个年份字符串（如 "2024"），将其转换为整数后，判断是否为闰年（结合之前学的闰年判断逻辑），输出判断结果。
def fun8():
    str1 = input("请输入一个年份：")
    year = int(str1)
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}年是闰年")
    else:
        print(f"{year}不是闰年")

# 让用户输入一个字符串，判断该字符串是否不是空字符串（结合not和bool()转换），输出 "非空字符串" 或 "空字符串"。
def fun9():
    str1 = input("输入一个字符串：")
    if not bool(str1):
        print("空字符串")
    else:
        print("非空字符串")

# 定义列表fruits = ["apple", "banana", "orange"]，让用户输入一个水果名称，判断该名称（转换为小写后）是否在列表中，输出对应的判断结果。
def fun10():
    fruits = ["apple", "banana", "orange"]
    name = input("输入一个水果名称的英文：")
    if (name).lower() in fruits:
        print(f"{name}在列表中")
    else:
        print(f"{name}不在列表中")


# Part 2
# 1.用户输入一个月份，判断是上半年还是下半年（1-12）
def fun11():
    m = int(input("请输入一个月份："))
    if 0<m<=6:
        print("上半年")
    elif m<=12:
        print("下半年")
    else:
        print("不是月份")
# 2.输入一个数字判断他是奇数还是偶数
def fun12():
    num = int(input("输入一个整数："))
    if num % 2 == 0:
        print("是偶数")
    else:
        print("是奇数")
# 3.输入两个数字 34,22 ,打印较大的那个比较大的数字
def fun13():
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    if num1 > num2:
        print(num1)
    elif num1 < num2:
        print(num2)
    else:
        print("两数相等")
# 4.用户输入一个年份，判断是闰年还是平年
#     普通闰年：公历年份是4的倍数，且不是100的倍数的，为闰年（如2004年、2020年等就是闰年）。
#     世纪闰年：公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是闰年，2000年是闰年）。
def fun14():
    year = int(input("输入一个年份："))
    if year % 400 == 0:
        print(f"{year}是世纪润年")
    elif year % 4 ==0 and year % 100 != 0:
        print(f"{year}是普通闰年")
    else:
        print(f"{year}是平年")

# Part 3
# # 编写程序，让用户输入一个整数，判断它是正数、负数还是零，并用 print 输出对应的结果。
def fun15():
    num = int(input("输入一个整数："))
    if num == 0:
        print("零")
    elif num > 0:
        print("正数")
    else:
        print("负数")
# # 接收用户输入的考试分数（0-100），如果分数≥90 输出 “优秀”，70-89 输出 “良好”，60-69 输出 “及格”，<60 输出 “不及格”（注意处理无效分数的情况）。
def fun16():
    score = float(input("输入成绩："))
    if score > 100 or score < 0:
        print("无效")
    elif score >= 90:
        print("优秀！")
    elif 70<=score<90:
        print("良好~")
    elif 60<=score<70:
        print("及格。")
    else:
        print("不及格")
# # 让用户输入两个整数 a 和 b，若 a 能被 b 整除，则输出 “a 是 b 的倍数”，否则输出 “a 不是 b 的倍数”（提示：使用取余运算符 %）。
def fun17():
    a = int(input("输入整数a："))
    b = int(input("输入整数b："))
    if a % b == 0:
        print("a是b的倍数")
    else:
        print("a不是b的倍数")
# # 输入一个年份，判断它是否为闰年（能被 4 整除且不能被 100 整除，或者能被 400 整除），输出 “是闰年” 或 “不是闰年”。
def fun18():
    year = int(input("输入年份："))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("闰年")
    else:
        print("不是闰年")
# # 编写程序，让用户输入一个字符，判断它是大写字母、小写字母、数字还是其他字符，并输出对应的类型。
def fun19():
    val1 = input("输入一个字符：")
    if "a" <= val1 <= "z":
        print("小写字母")
    elif "A" <= val1 <= "Z":
        print("大写字母")
    elif "0" <= val1 <= "9":
        print("数字")
    else:
        print("其他字符")
# # 接收用户输入的三个整数，找出其中的最大值并输出（使用分支语句实现，不使用 max () 函数）。
def fun20():
    num1 = int(input("输入第一个数："))
    num2 = int(input("输入第二个数："))
    num3 = int(input("输入第三个数："))
    if num1 > num2:
        if num1 > num3:
            print(num1)
        else:
            print(num3)
    else:
        if num2 > num3:
            print(num2)
        else:
            print(num3)
# # 让用户输入自己的年龄和性别（男 / 女），如果是女性且年龄≥55，或者男性且年龄≥60，输出 “已退休”，否则输出 “未退休”。
def fun21():
    age = int(input("输入年龄："))
    sex = input("输入性别（男/女）：")
    if age < 0 or age > 200:
        print("非法年龄")
    elif sex == "男":
        if age >= 60:
            print("已退休")
        else:
            print("未退休")
    elif sex == "女":
        if age >= 55:
            print("已退休")
        else:
            print("未退休")
    else:
        print("非法性别")
# # 输入一个整数，判断它是否是 3 的倍数但不是 5 的倍数，若是则输出 “符合条件”，否则输出 “不符合条件”。
def fun22():
    num = int(input("输入一个整数："))
    if num % 3 == 0 and num % 5 != 0:
        print("符合条件")
    else:
        print("不符合条件")
# # 编写程序模拟简易计算器：让用户输入两个数字和一个运算符（+、-、*、/），根据不同的运算符进行相应的计算并输出结果（注意处理除法中除数为 0 的情况）。
def fun23():
    num1 = input("输入num1：")
    sign = input("输入运算符(+、-、*、/)：")
    num2 = input("输入num2：")
    if "." in num1 and "." in num2:
        num1 = float(num1)
        num2 = float(num2)
    elif "." in num1:
        num1 = float(num1)
        num2 = int(num2)
    elif "." in num2:
        num1 = int(num1)
        num2 = float(num2)
    else:
        num1 = int(num1)
        num2 = int(num2)

    if sign == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif sign == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif sign == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif sign == "/":
        if num2 == 0:
            print("除数不能为零！")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
# # 让用户输入一个月份（1-12），输出该月份对应的季节（3-5 月为春季，6-8 月为夏季，9-11 月为秋季，12、1、2 月为冬季），若输入的月份无效则输出 “请输入正确的月份”。
def fun24():
    m = int(input("输入月份(1-12)："))
    if m <= 0 or m > 12:
        print("不是月份")
    elif 3 <= m <= 5:
        print("春")
    elif 6 <= m <= 8:
        print("夏")
    elif 9 <= m <= 11:
        print("秋")
    else:
        print("冬")


# Part 4
# 1.编写程序，使用 while 循环计算 1 到 100 之间所有整数的和，并输出结果。
def fun25():
    i = 1
    sum = 0
    while i <= 100:
        sum = sum + i
        i = i + 1
    print(sum)
# 2.让用户输入一个正整数 n，用 while 循环计算 n 的阶乘（n! = 1×2×3×…×n）并输出。
def fun26():
    n = int(input("输入一个正整数："))
    i = 1
    fact = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print(fact)
# 3.使用 while 循环打印出 1 到 20 之间所有能被 3 整除的数，每个数占一行。
def fun27():
    i = 1
    while i <= 20:
        if i % 3 == 0:
            print(i)
        i = i + 1
# 4.编写程序，用 while 循环实现：让用户反复输入整数，直到输入 0 为止，然后计算所有输入数字的平均值并输出。
def fun28():
    sum = 0
    count = 0
    i = 1
    while i:
        num = int(input("请输入一个整数："))
        sum = sum + num
        count = count + 1
        if num == 0:
            print(f"avg = {sum/count}")
            i = 0


if __name__ == '__main__':
    fun24()