'''
Day1 10.10
python入门：变量、输出、数据运算、函数定义及调用
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
# 1.算术运算：+  -   *   /   //  %   **
def operation1():
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

# 2. 比较运算：> <   >=  <=  ==
def operation2():
    print(2>5)
    print(8<9)
    print(5>=2)
    print(3<=3)
    print(10==10)

# 3. 逻辑运算：and   or  not
def operation3():
    print(4 and 6)
    print(4 or 6)
    print(True and False)
    print(True or False)
    print(not 6)
    print(not False)

# 4. 赋值运算：+=    -=  *=  /=  //= %=  **=
def operation4():
    num = 4
    num += 12
    print(num)


# 数据输入：input
def myinput():
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    height = float(input("请输入身高："))
    print(name, type(name))
    print(age, type(age))
    print(height, type(height))

# 数据输出
def myoutput():
    name = "孙悟空"
    age = 600
    height = 1.6
    print(name, age, height)
    print(f"姓名：{name}\t年龄：{age}\t身高：{height}")


if __name__ == '__main__':
    # var_def()
    # sugar()
    # operation1()
    # operation2()
    # operation3()
    # operation4()
    # myinput()
    myoutput()
    pass