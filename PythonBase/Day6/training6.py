"""
Day6 10.16
练习
"""

# Part 1
# 以下是10道针对Python类中属性变量、类变量、实例方法、类方法和静态方法的练习题，涵盖核心概念和使用场景：
# 1. **基础类变量与实例变量**
#    定义一个`Student`类，包含类变量`school = "阳光中学"`，以及实例变量`name`和`age`（通过`__init__`初始化）。创建两个学生对象，打印他们的姓名、年龄和所属学校，然后修改类变量`school`的值为"星光中学"，再打印两个学生的学校，观察变化。
# class Student:
#     school = "阳光中学"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(f"姓名：{self.name}    年龄：{self.age}")
# 2. **实例方法的基本使用**
#    定义一个`Circle`类，实例变量为`radius`（半径）。编写实例方法`area(self)`计算圆的面积（π取3.14），`circumference(self)`计算周长。创建半径为5的圆对象，调用两个方法并输出结果。
# class Circle:
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         print(f"面积为：{Circle.pi * (self.radius ** 2)}")
#     def circumference(self):
#         print(f"周长为：{2 * Circle.pi * self.radius}")


# 3. **类方法操作类变量**
#    定义`Book`类，类变量`total_books = 0`记录总书本数。通过`__init__`方法初始化每本书的`title`，并在初始化时让`total_books`加1。编写类方法`get_total(cls)`返回`total_books`。创建3个Book对象后，调用类方法打印总书本数。
# class Book:
#     total_books = 0
#     def __init__(self, title):
#         self.title = title
#         Book.total_books += 1
#     @classmethod
#     def get_total(cls):
#         return Book.total_books

# 4. **静态方法的独立功能**
#    定义`MathUtils`类，编写静态方法`is_prime(n)`判断一个数是否为质数。在类外部直接通过类名调用该方法，分别判断7、12、17是否为质数并输出结果。
# class MathUtils:
#     @staticmethod
#     def is_prime(n):
#         if n < 2:
#             print("是质数")
#         else:
#             flag = True
#             for i in range(2, n):
#                 if n % i == 0:
#                     flag = False
#             if flag:
#                 print("是质数")
#             else:
#                 print("不是质数")

# 5. **类变量与实例变量的优先级**
#    定义`Dog`类，类变量`color = "白色"`，实例变量`color`在`__init__`中初始化为参数值。创建对象时传入`"黑色"`，打印对象的`color`属性，再打印`Dog.color`，观察两者的区别。
# class Dog:
#     color = "白色"
#     def __init__(self, color):
#         self.color = color

# 6. **类方法修改类变量**
#    定义`Counter`类，类变量`count = 0`。编写类方法`increment(cls)`使`count`加1，`reset(cls)`使`count`重置为0。调用`increment`3次后打印`count`，再调用`reset`后打印`count`。
# class Counter:
#     count = 0
#     @classmethod
#     def increment(cls):
#         Counter.count += 1
#     @classmethod
#     def reset(cls):
#         Counter.count = 0

# 7. **实例方法、类方法、静态方法混合**
#    定义`Car`类：
#    - 类变量`total_cars = 0`
#    - 实例变量`brand`（品牌）通过`__init__`初始化，初始化时`total_cars`加1
#    - 实例方法`start(self)`返回`"[品牌]汽车启动"`
#    - 类方法`get_total(cls)`返回总车辆数
#    - 静态方法`is_electric(brand)`：若品牌为"特斯拉"或"蔚来"，返回`True`，否则返回`False`
#    创建2个Car对象（分别为"特斯拉"和"大众"），测试所有方法。
# class Car:
#     total_cars = 0
#     def __init__(self, brand):
#         self.brand = brand
#         Car.total_cars += 1
#     def start(self):
#         print(f"【{self.brand}】汽车启动")
#     @classmethod
#     def get_total(cls):
#         print(f"车辆总数：{Car.total_cars}")
#     @staticmethod
#     def is_electric(brand):
#         if brand == "特斯拉" or brand == "蔚来":
#             return True
#         else:
#             return False


# 8. **静态方法处理类相关逻辑**
#    定义`Date`类，编写静态方法`is_valid(year, month, day)`判断给定的年月日是否为有效日期（考虑月份天数、闰年2月特殊情况）。调用该方法判断`2024-2-29`、`2023-2-29`、`2023-13-5`是否有效。
# class Date:
#     @staticmethod
#     def is_valid(year, month, day):
#         if 1 <= month <= 12:
#             if month == 2:
#                 if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#                     if day <= 28:
#                         return True
#                     else:
#                         return False
#                 else:
#                     if day <= 29:
#                         return True
#                     else:
#                         return False
#             elif month % 2 !=  0 and 0 < day <= 31:
#                 return True
#             elif month % 2 == 0 and day <= 30:
#                 return True
#             else:
#                 return False
#         else:
#             return False

# 9. **类变量在继承中的表现**
#    定义父类`Animal`，类变量`category = "动物"`；子类`Dog(Animal)`，类变量`category = "哺乳动物"`。创建`Animal`对象和`Dog`对象，分别打印它们的`category`属性，观察类变量的继承与重写。
# class Animal:
#     category = "动物"
# class Dog(Animal):
#     category = "哺乳动物"

# 10. **综合案例：学生管理**
#     定义`StudentManager`类：
#     - 类变量`students = []`（存储所有学生对象）
#     - 实例方法`add_student(self, name, score)`：将学生信息（字典）添加到`students`
#     - 类方法`get_average_score(cls)`：计算所有学生的平均分
#     - 静态方法`is_passed(score)`：若分数≥60返回"及格"，否则返回"不及格"
#     使用该类添加3名学生（分数分别为85、59、72），打印平均分，并分别判断每个学生是否及格。
# class StudentManager:
#     students = []
#     def add_student(self, name, score):
#         self.students.append([name, score])
#     @classmethod
#     def get_average_score(cls):
#         sum = 0
#         for student in cls.students:
#             sum += student[1]
#         print(f"所有学生平均分：{sum / len(cls.students)}")
#     @staticmethod
#     def is_passed(score):
#         if score >= 60:
#             print("及格")
#         else:
#             print("不及格")

# 这些题目覆盖了类变量与实例变量的区别、三种方法（实例/类/静态）的定义与调用场景，以及它们在实际业务逻辑中的应用，帮助理解面向对象中变量和方法的作用域与设计思路。

# Part 2
# 题目：
#    定义一个父类：Hero
#       hp 血量 初始值1000， mp 蓝量 初始值：1000， name：英雄
        # 1.skill1〇  输出“技能1”
        # 2.skill2〇  输出“技能1”
        # 3.skill3〇 输出“技能1”
#    3个子类；
        # 姐己 2000 3000
        # 王昭君 1900 3300
        # 亚瑟 4000 0
class Hreo:
    def __init__(self, hp=1000, mp=1000):
        self.hp = hp
        self.mp = mp
    def skill1(self):
        print("1技能")
    def skill2(self):
        print("2技能")
    def skill3(self):
        print("3技能")
# 辅助：妲己
class Support(Hreo):
    def __init__(self, name, hp1=1000, mp1=1000):
        super().__init__(hp1, mp1)
        self.name = name
    def skill1(self):
        print("技能1：灵魂冲击")
        self.hp -= 60
        self.mp -= 10
    # 技能2：偶像魅力 消耗90
    # 技能3：女王崇拜 消耗120
# 法师:王昭君
class Master(Hreo):
    def __init__(self, name, hp2=1000, mp2=1000):
        super().__init__(hp2, mp2)
        self.name = name
    def skill2(self):
        print("技能2：禁锢寒霜")
        self.hp -= 80
        self.mp -= 5
    # 技能1：凋零冰晶 消耗50
    # 技能3：凛冬已至 消耗120
# 战士：亚瑟
class Warrior(Hreo):
    def __init__(self, name, hp3=1000, mp3=1000):
        super().__init__(hp3, mp3)
        self.name = name
    def skill3(self):
        print("技能3：圣剑裁决")
        self.hp -= 0
        self.mp -= 0
    # 技能1：誓约之盾 消耗0
    # 技能2：回旋打击 消耗0
if __name__ == '__main__':
    # 1.
    # print(Student.school)
    # stu1 = Student("李华", 18)
    # stu2 = Student("张三", 22)
    # print(stu1.school)
    # stu1.print_info()
    # Student.school = "星光中学"
    # print(stu2.school)
    # stu2.print_info()

    # 2.
    # c1 = Circle(5)
    # c1.area()
    # c1.circumference()

    # 3.
    # book1 = Book("《青铜葵花》")
    # book2 = Book("《活着》")
    # book3 = Book("《第七天》")
    # num = Book.get_total()
    # print(f"书本总数：{num}")

    # 4.
    # MathUtils.is_prime(7)
    # MathUtils.is_prime(12)
    # MathUtils.is_prime(17)
    # MathUtils.is_prime(27)

    # 5.
    # dog1 = Dog("黑色")
    # print(dog1.color)
    # print(Dog.color)

    # 6.
    # Counter.increment()
    # Counter.increment()
    # Counter.increment()
    # print(Counter.count)
    # Counter.reset()
    # print(Counter.count)

    # 7.
    # car1 = Car("大众")
    # car1.start()
    # Car.get_total()
    # print(Car.is_electric("大众"))
    # car2 = Car("特斯拉")
    # car2.start()
    # Car.get_total()
    # print(Car.is_electric("特斯拉"))

    # 8.
    # print(Date.is_valid(2024, 2, 29))
    # print(Date.is_valid(2023, 2, 29))
    # print(Date.is_valid(2023, 13, 5))

    # 9.
    # animal = Animal()
    # print(Animal.category)
    # dog = Dog()
    # print(Animal.category)
    # print(Dog.category)

    # 10.
    # stus = StudentManager()
    # stus.add_student("张三", 85)
    # stus.add_student("李华", 59)
    # stus.add_student("小明", 72)
    # StudentManager.get_average_score()
    # StudentManager.is_passed(85)
    # StudentManager.is_passed(59)
    # StudentManager.is_passed(72)

    daji = Support("daji", 2000, 3000)
    wzj = Master("wzj", 1900, 3300)
    yase = Warrior("yase", 4000, 0)
    print(daji.name, daji.hp, daji.mp)
    daji.skill1()
    print(daji.name, daji.hp, daji.mp)
    daji.skill2()
    daji.skill3()
    wzj.skill1()
    print(wzj.name, wzj.hp, wzj.mp)
    wzj.skill2()
    print(wzj.name, wzj.hp, wzj.mp)
    wzj.skill3()
    print(yase.name, yase.hp, yase.mp)
    yase.skill1()
    # print(yase.name, yase.hp, yase.mp)
    yase.skill2()
    yase.skill3()
    print(yase.name, yase.hp, yase.mp)

    pass