'''
Day1 python入门：变量、输出、数据运算、函数定义及调用
'''

# 变量定义和输出
def var_def():
    # 变量
    stu1 = "name"
    stu2 = 12
    stu3 = 5.4
    stu4 = True
    # 输出结果
    print(stu1, stu2, stu3, stu4)

# 语法糖
def sugar():
    a, b, c = 1, 3.5, "李四"
    print(a, b, c)

# 数据运算
def operation():
    # 1.算术运算：+  -   *   /   //  %   **
    num = 789
    hundred = 789 // 100
    remainder = 789 % 100
    decade = remainder // 10
    unit = remainder % 10
    print(num, hundred, decade, unit)
    # f表达式
    print(f"{num}的百位是{hundred}，十位是{decade}，个位是{unit}")
    # %占位符
    print("%d的百位是%d，十位是%d，个位是%d" % (num, hundred, decade, unit))
    # format
    print("{num}的百位是{hundred}，十位是{decade}，个位是{unit}".format(num=num, hundred=hundred,decade=decade, unit=unit))


# 练习：以下是10道适合初学者的Python编程练习题，只涉及变量定义、算术运算和输出语句：
#
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




if __name__ == '__main__':
    # var_def()
    # sugar()
    # operation()
    # age_sum()
    # rectangle()
    # avg()
    # balance()
    # turn_degree()
    # price()
    # circle_area()
    # sum_even()
    # height_sub()
    digit()