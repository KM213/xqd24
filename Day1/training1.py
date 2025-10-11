"""
Day1 10.10
练习题
"""


# 上午练习：以下是10道适合初学者的Python编程练习题，只涉及变量定义、算术运算和输出语句：
# 1. 编写程序，定义两个变量分别存储你的年龄和你朋友的年龄，计算并输出你们的年龄之和。
def age_sum():
    age1 = 22
    age2 = 19
    # 计算年龄的和
    sum = age1 + age2
    print(sum)

# 2. 定义一个变量存储长方形的长度（5），另一个变量存储宽度（3），计算并输出长方形的周长和面积。
def rectangle():
    length = 8
    width = 6
    # 计算周长
    perimeter = (length + width) * 2
    # 计算面积
    area = length * width
    print(perimeter, area)

# 3. 定义三个变量分别存储三个不同的整数，计算并输出它们的平均值（结果保留整数即可）。
def avg():
    num1 = 6
    num2 = 18
    num3 = 9
    # 计算平均值
    avg_num = (num1 + num2 + num3) // 3
    print(avg_num)

# 4. 小明有50元零花钱，买了一个18元的文具袋和一个9元的笔记本，编写程序计算并输出他还剩多少钱。
def balance():
    total = 50
    com1 = 18
    com2 = 9
    # 计算余额
    balance = total - com1 - com2
    print(balance)

# 5. 定义两个变量分别存储华氏温度（例如77），将其转换为摄氏温度并输出（转换公式：摄氏温度 = (华氏温度 - 32) × 5/9）。
def turn_degree():
    fdegree1 = 72
    fdegree2 = 90
    # 计算摄氏温度
    cdegree1 = (fdegree1 - 32) * 5 / 9
    cdegree2 = (fdegree2 - 32) * 5 / 9
    print(cdegree1, cdegree2)

# 6. 一个苹果3元，一个香蕉2元，编写程序计算购买4个苹果和5个香蕉一共需要多少钱，并输出结果。
def price():
    apple_price = 3
    banana_price = 2
    apple_num = 4
    banana_num = 5
    # 计算总价
    sum_price = apple_price * apple_num + banana_price * banana_num
    print(sum_price)

# 7. 定义一个变量存储圆的半径（例如5），计算并输出圆的面积（π取3.14）。
def circle_area():
    r = 5
    pi = 3.14
    # 计算面积
    area = pi * (r ** 2)
    print(area)

# 8. 编写程序，计算并输出1到10之间所有偶数的和（使用变量存储中间结果）。
def sum_even():
    init = 1
    end = 10
    sum = 0
    # 计算偶数的和
    for num in range(init, end):    # 不包含10
        if num % 2 == 0:
            sum += num
    print(sum)

# 9. 小红的身高是1.65米，小李的身高是1.75米，计算并输出两人身高的差距（以厘米为单位）。
def height_sub():
    height1 = 1.65
    height2 = 1.75
    # 计算差值并换算单位
    sub = (int(abs(height1 - height2)* 100))
    print(sub)

# 10. 定义两个变量分别存储一个三位数的百位和个位数字（例如百位是3，个位是5），计算并输出将这两个数字交换位置后形成的新两位数（例如3和5交换后是53）。
def digit():
    num = 829
    # 计算百位和个位
    hundred = num // 100
    unit = num % 10
    # 计算新数
    new_num = unit * 10 + hundred
    print(num, hundred, unit, new_num)

# 下午练习：以下是 10 道结合了输入语句（input）、比较运算和逻辑运算的编程练习题，适合巩固新学习的知识点：
# 1.编写程序，让用户输入两个整数，比较这两个数的大小，并输出 “第一个数更大”、“第二个数更大” 或 “两个数相等”。
def fun1():
    num1 = int(input("请输入第一个整数："))
    num2 = int(input("请输入第二个整数："))
    if num1 > num2:
        print("第一个数更大")
    elif num1 < num2:
        print("第二个数更大")
    else:
        print("两个数相等")

# 2.让用户输入一个整数，判断这个数是否同时是 2 和 3 的倍数（即能被 6 整除），并输出判断结果。
def fun2():
    num = int(input("请输入一个整数："))
    if num % 6 == 0:
        print(f"{num}是2和3的倍数")
    elif num % 2 == 0:
        print(f"{num}是2的倍数")
    elif num % 3 == 0:
        print(f"{num}是3的倍数")
    else:
        print(f"{num}既不是2的倍数也不是3的倍数")

# 3.编写程序，接收用户输入的三个整数，判断其中是否有至少两个数是偶数，输出 “满足条件” 或 “不满足条件”。
def fun3():
    nums = []
    # print(type(num))
    for i in range(3):
        num = int(input(f"请输入第{i+1}个整数："))
        nums.append(num)
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    if count >= 2:
        print("满足条件")
    else:
        print("不满足条件")

# 4.让用户输入自己的年龄，判断是否满足 “大于等于 18 岁且小于 60 岁” 的条件，如果满足则输出 “成年且非老年”，否则输出 “不满足条件”。
def fun4():
    age = int(input("请输入年龄："))
    if age >= 18 and age < 60:
        print("成年且非老年")
    else:
        print("不满足条件")

# 5.接收用户输入的两个数（a 和 b），判断 “a 大于 10 且 b 小于 20” 或者 “a 加 b 等于 30” 这两个条件是否成立，输出判断结果。
def fun5():
    a = int(input("请输入第一个数："))
    b = int(input("请输入第二个数："))
    if (a > 10 and b < 20) or (a + b == 30):
        print(f"条件成立")
    else:
        print(f"条件不成立")

# 6.让用户输入一个整数，判断这个数是否是奇数并且大于 100，输出相应的判断结论。
def fun6():
    num = int(input("请输入一个整数："))
    if num % 2 != 0 and num > 100:
        print(f"{num}是奇数且大于100")
    else:
        print("不满足条件")

# 7.编写程序，输入三个不同的整数，判断其中最大的数是否大于另外两个数的和，输出 “是” 或 “否”。
def fun7():
    nums = [0, 0, 0]
    for i in range(3):
        nums[i] = int(input(f"请输入第{i+1}个整数："))
    m1 = max(nums[0], nums[1], nums[2])
    if m1 > (nums[0] + nums[1] + nums[2] - m1):
        print("是")
    else:
        print("否")

# 8.接收用户输入的语文和数学成绩（0-100 之间），判断两门成绩是否都在 60 分及以上，或者其中一门在 90 分及以上，输出对应的判断结果。
def fun8():
    ch = int(input("请输入语文成绩(0-100分)："))
    math = int(input("请输入数学成绩(0-100分)："))
    if ch >= 90 and math >= 90:
        print("两门都在90分及以上")
    elif ch >= 90:
        print("语文成绩在90及以上")
    elif math >= 90:
        print("数学成绩在90及以上")
    elif ch >= 60 and math >= 60:
        print("两门均在60分及以上")

# 9.让用户输入一个年份，判断这个年份是否是闰年（能被 4 整除但不能被 100 整除，或者能被 400 整除），并输出判断结果。
def fun9():
    year = int(input("请输入一个年份："))
    if year < 400:
        print(f"{year}不是闰年")
    elif (year %4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year}是闰年")
    else:
        print(f"{year}不是闰年")

# 10.编写程序，输入一个整数，判断它是否满足 “大于 50 且是偶数” 或者 “小于 20 且是奇数” 这两个条件中的任意一个，输出判断结论。
def fun10():
    num = int(input("请输入一个整数："))
    if (num > 50 and num % 2 == 0) or (num < 20 and num % 2 != 0):
        print("满足条件")
    else:
        print("不满足条件")


if __name__ == '__main__':
    # 上午
    # age_sum()
    # rectangle()
    # avg()
    # balance()
    # turn_degree()
    # price()
    # circle_area()
    # sum_even()
    # height_sub()
    # digit()
    # 下午
    fun10()
    pass