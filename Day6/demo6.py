"""
Day6 10.16
面向对象：类编程
    变量：
        类变量：可以被该类的所有实例共享的变量
                定义在__init__(self)外，或定义在类的方法外
                引用：
                    类方法中引用：类名.变量名 【一般用在类的系统方法中，如__init__()方法中】 如：Pig.num = 1
                                cls.变量名 【一般用在普通类方法中，即自定义方法中】   如：cls.num = 2
        属性变量：仅为每个实例私有的变量 (实例变量)
                定义在__init__(self)初始化方法中【self变量，存放实例的内存空间地址，系统自动赋值。类实例化的每一个对象的所有变量都存储在self指向的内存空间】
                引用：
                    类方法中引用：self.变量名     如：self.vab1 = 10
                    实例对象引用：实例名.变量名    如：print(pig.color)
                可以在整个类的任意方法中使用
    方法：
        类方法： 使用@classmethod进行声明
                def fun(cls, ...)   cls存放类本身的的空间地址，系统自动赋值
                类方法中只能使用类变量和局部变量，不能使用属性变量。
                调用：类名.类方法()
        属性方法：def fun(self, ...)
                只有属性方法可以使用属性变量
                调用：
                    类方法中调用：self.方法名()
                    实例对象调用：实例名.方法名()
        静态方法：使用@staticmethod进行声明
                定义：def fun(...)  不包含cls和self变量
                静态方法不能使用类变量和属性变量。只能使用局部和全局变量
                调用：类名.方法名(...)
                静态方法使用时，系统不会为其开辟空间，而是直接使用【？】
    例：
        class Book:
            num = 0         # 类变量
            def __init__(self, vab1):   # vab1：形参
                self.vab1 = vab1        # self.vab1：属性变量
                vab2 = 2                # vab2：局部变量
                cls.fun()

            def show():                 # 属性方法
                print(self.vab1)
            @classmethod
            def fun(cls):               # 类方法
                cls.num += 1
            @staticmethod               # 静态方法
            def sum(num1, num2):
                print(num1+num2)
    类的特性：封装、集成、多态
    1. 封装性：将类中的信息对外隐藏
            属性或变量名前加__符号成为私有属性，外部无法直接访问和修改此属性，如self.__color = "yellow"、cls.__num = 0
    2. 继承性：子类可以继承父类的属性和方法。
              但私有属性不会被继承，但可以调用父类中针对私有属性的get、set等方法进行调用。
              父类包含__init__()方法时，子类需要用super()调用父类的初始化，才能进一步使用父类的属性及变量。并且子类初始化方法的参数列表要包含调用父类初始化时需要的参数。
              python支持多重继承

        * 继承多个父类时：Python 多继承冲突解决与 super() 精要总结
        *     一、多继承冲突解决方案
        *       1. 方法解析顺序（MRO）：Python 使用 C3 线性化算法 自动确定方法调用顺序
        *             通过 类名.__mro__ 或 类名.mro() 查看解析顺序
        *             基本原则：深度优先，从左到右
        *       2. 冲突解决策略
        *           方法	                适用场景	            示例
        *           调整父类顺序	        简单优先级控制	    class C(A, B): ← A 优先于 B
        *           直接调用父类	        精确控制调用	        A.method(self)
        *           super() 链式调用	    协作式多继承	        super().method()、super(A, self).method()
        *           混入类设计	        功能组合	            class MyClass(Base, Mixin1, Mixin2)
        *       3. 设计原则
        *             避免菱形继承：减少复杂度
        *             多用组合，少用继承：降低耦合
        *             混入类单一职责：每个混入类只负责一个功能
        *
        *     二、super(A, self) 特殊用法详解
        *       1. 核心概念：super(A, self).method()
        *             A：起始查找点（在 MRO 中跳过 A 及之前的类）
        *             self：当前实例对象
        *             method：要调用的方法
        *       2. 工作原理
        *             获取 self 的 MRO 列表
        *             在 MRO 中找到类 A 的位置
        *             返回 A 之后第一个类的代理
        *             调用该代理的指定方法

"""

class Book:
    num = 0     # 类变量
    def __init__(self, name, auther, price):
        self.name = name        # 属性变量
        self.auther = auther
        self.price = price
        Book.num += 1
    # 类方法
    @classmethod
    def book_num(cls):
        print(cls.num)
    # 属性方法
    def show(self):
        print(f"书名：{self.name}")
        print(f"作者：{self.auther}")
        print(f"价格：{self.price}")
    # 静态方法
    @staticmethod
    def cube(num1):
        mi = 3      # 局部变量
        print(num1 ** mi)


# 5.设计一个函数order_food(main_dish, *sides, drink="可乐", **extras)，
# 参数说明：
# -main_dish：主菜（必传位置参数，如 "汉堡"），
# -*sides：可变参数，接收任意数量的配菜（如 "薯条"、"鸡翅"），
# -drink：饮品（默认值 "可乐"），
# -** extras：关键字可变参数，接收额外要求（如 "少冰 = True"、"加辣 = False"）。
# 函数需返回订单详情字符串，
# 例如：order_food("牛排", "沙拉", "面包", drink="果汁", 少盐=True)应返回："主菜：牛排，配菜：[' 沙拉 ', ' 面包 ']，
# 饮品：果汁，额外要求：{' 少盐 ': True}"。
class KFC:
    @staticmethod
    def order_food(main_dish, *sider, drink="可乐", **extras):
        print(f"主食：{main_dish}")
        print(f"副食：{list(sider)}")
        # for i in sider:
        #     print(f"{i}", end=" ")
        print(f"饮料：{drink}")
        print(f"备注：")
        for i,j in extras.items():
            print(f"{i}, {j}")

    def calculate_total(self, price, quantity=1, *discounts):
        print(f"商品价格：{price}  购买数量：{quantity}")
        print(f"折扣：")
        sum = 0
        for discount in discounts:
            print(f"-{discount}")
            sum += float(discount)
        print(f"折扣总计：-{sum}")
        total = price * quantity - sum
        print(f"最终价格：{total}")


# 封装
# class Stus:
#     __num = 0
#     def __init__(self, id, name, score):
#         self.__id = id
#         self.name = name
#         self.score = score
#         Stus.__num += 1
#     @classmethod
#     def show_num(cls):
#         print(cls.__num)
#
#     def show_id(self):
#         print(f"【{self.name}】的学号为【{self.__id}】")
#     def set_id(self, id):
#         self.__id = id
#         print(f"{self.name}的学号修改为：【{self.__id}】")

# 继承
# class A:
#     def __init__(self):
#         self.__a = 1
#     def funa(self):
#         print("funa")
# class B:
#     def __init__(self):
#         self.__b = 2
#     def getb(self):
#         print(f"getb:{self.__b}")
#         print(self.__b)
#     def funb(self):
#         print("funb")
# class C(A, B):
#     def __init__(self):
#         super().__init__()
#         super(A, self).__init__()    # 解决多个父类时的查找顺序问题。super(A, self)返回一个代理，表示在MRO中跳过A从之后继续查找顺序，即不会因A更近而忽略掉B的查找
#         self.c = 3
#         pass
#     def func(self):
#         print("func")
#     def getb(self):
#         super().getb()

# 继承 2
class Animal:
    def __init__(self, age, color):
        self.__age = age
        self.color = color
    def get_age(self):
        print(f"age: {self.__age}")
    def eat(self):
        print("吃东西")
    def shot(self):
        print("动物叫")
class Cat(Animal):
    def __init__(self, type, age, color):
        super().__init__(age, color)
        self.type = type
    def eat(self, food):
        print(f"【{self.type}】吃了一份【{food}】")
    def shot_cat(self):
        print("猫叫：喵喵喵")


if __name__ == '__main__':
    # Book.book_num()
    # book1 = Book("活着", "余华", "35.0")
    # book1.show()
    # print(book1.num)
    # book2 = Book("第七天", "余华", "41.0")
    # book2.show()
    # print(Book.num)
    # book3 = Book("红楼梦", "曹雪芹", "55.0")
    # book3.show()
    # Book.book_num()
    # Book.cube(5)

    # KFC.order_food("鸡腿堡","鸡米花","薯条", 番茄酱=True)
    # x = KFC()
    # x.calculate_total(55,2,1.5, 0.88)

    # 封装
    # stu1 = Stus("007", "郝苏", "99")
    # stu1.show_id()
    # stu1.show_num()
    # stu2 = Stus("005", "罗辑", "79")
    # stu2.show_id()
    # Stus.show_num()
    # stu2.set_id("009")
    # stu2.show_id()

    # 继承
    # c1 = C()
    # c1.funa()
    # c1.funb()
    # c1.func()
    # c1.getb()

    # animal1 = Animal(3, "灰色")
    cat1 = Cat("布偶", 2, "灰色")
    # 继承属性
    print(f"颜色：{cat1.color}")

    cat1.eat("鱼")   # 覆盖方法
    # cat1.eat()      # 继承方法，此处子类已重写eat()方法，所以父类的eat()方法无法再使用
    cat1.get_age()  # 继承方法
    cat1.shot()     # 继承方法
    cat1.shot_cat() # 自有方法

    pass
