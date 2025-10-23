"""
Day10 10.21     Python进阶
1. 迭代器：一个由类生成的对象，表示一个数据流
        迭代器类必备两个方法：
            1） __iter__()方法：支持迭代访问，返回迭代器自身
                    迭代器调用iter()方法，类中自动调用__iter__()方法，返回迭代器自身
            2） __next__()方法：获取数据流中的下一个值，返回迭代器元素，当没有下一个值时抛出StopIteration异常
                    迭代器调用next()方法，类中自动调用__next__()方法，返回迭代器元素
2. 生成器；特殊迭代器，调用时由函数返回序列中的一个迭代元素
        用yeild代替函数中的return来返回数据。（每次yeild返回时将返回值进行缓存，下次再调用函数时从yeild语句后继续执行下一句）
        调用生成器返回的是一个迭代对象，需要使用next()方法来访问迭代元素值
        生成器表达式：(表达式 for 变量 in 可迭代对象)
            例：print(i for i in range(10))
3. 推导表达式（语法糖）：列表推导式、字典推导式、集合推导式
        列表推导式：[表达式 for 变量1 in 可迭代对象1 if 条件1
                        for 变量2 in 可迭代对象2 if 条件2]
        字典推导式：{key:value for key1,value1 in zip(可迭代对象1,可迭代对象2) if 条件1
                            for key2,value2 in zip(可迭代对象3,可迭代对象4) if 条件2}
        集合推导式：{表达式 for 变量1 in 可迭代对象1 if 条件1
                         for 变量2 in 可迭代对象2 if 条件2}
    ** for循环的本质就是不断调用next()方法，直到抛出StopIteration异常 **
    ** 多个循环生成结果去笛卡尔乘积 **
4. 匿名函数（语法糖）：一行代码实现一个函数
    作用：对单行代码函数的一种优化
    关键字：lambda
    格式：
          1） 无参数无返回值：  定义 - 变量 = lambda : 表达式           运行 - 变量()       如：l1 = lambda : print("hello")
          2） 有参数无返回值：  定义 - 变量 = lambda 参数列表: 表达式    运行 - 变量(参数)    如：l2 = lambda x: print(x ** 2)
          3） 无参数有返回值：  定义 - 变量 = lambda : 表达式           运行 - 变量()       如：l3 = lambda : [i * 2 for i in range(10) if i % 3 == 0]
          4） 有参数有返回值：  定义 - 变量 = lambda 参数列表: 表达式    运行 - 变量(参数)    如：l4 = lambda x,y: x + y

5. for _ in range(10):
    pass
    当仅需要控制循环次数而不需要引用循环变量值时，可使用_代替循环变量，从而省去变量赋值过程提高效率

6. 闭包函数
    1） 函数嵌套：在函数中定义函数，内层函数可以使用外层函数定义的局部变量
    2） 函数名：存储函数体在内存中存放的首地址
                故将函数名赋值给某变量，用该变量也可以调用函数  即 var1 = fun1  =>  var1() == fun1()
    3） 闭包函数：在函数内部定义函数，并返回该函数名，外层函数的变量可以被内层函数引用
            def outer_fun2(num1):
                print(f"我是outer_fun2(): num1={num1}")
                def inner_fun2(num2):
                    print(f"我是inner_fun2(): num2={num2}")
                    print(f"num1 + num2 = {num1 + num2}")
                return inner_fun2
            x = outer_fun2(3)       # 输出：我是outer_fun2(): num1=3
            x(1)                   # 输出：我是inner_fun2(): num2=1  num1 + num2 = 4
        在嵌套函数中将内层函数名作为外层函数的返回值进行return，就可以在函数外部间接调用内层函数
"""


# 迭代器
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self     # 返回自身

    def __next__(self):     # 返回下一个值或抛出异常
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
class MyRange:
    def __init__(self, *args):
        self.start = 0
        self.step = 1
        if len(args) == 1:
            self.end = args[0]
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
        else:
            raise ValueError('MyRange takes at most 3 arguments')

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            num = self.start
            self.start += self.step
            return num
        else:
            raise StopIteration

# 生成器
def my_generator(start, end):
    num = start
    while num < end:
        yield num
        num += 1

# 闭包函数
def outer_fun():
    print("我是outer_fun()")
    name = 'kenny'
    def inner_fun():
        print("我是inner_fun()")
        print(f"我是{name}")
    inner_fun()


if __name__ == '__main__':
    # 1. 迭代器1
    # data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # my_iterator = MyIterator(data)
    # print(my_iterator.__iter__())
    # print(my_iterator.__next__())
    # print(my_iterator.__next__())
    # print(my_iterator.__next__())
    # print("--------------------")
    # for i in my_iterator:
    #     print(i)

    # 迭代器2
    # print("--------------------迭代器：自定义range()")
    # myrange = MyRange(10)
    # myiter = iter(myrange)
    # print(myiter)
    # print(next(myiter))
    # print("--------------------")
    # for i in myrange:
    #     print(i)
    # print("--------------------")
    # for i in MyRange(10, 20):
    #     print(i)
    # print("--------------------")
    # for i in MyRange(1, 20, 3):
    #     print(i)

    # 2. 生成器
    # print("--------生成器-------")
    # n1 = my_generator(1, 10)
    # print(n1)           # <generator object my_generator at 0x0000019FFC672810>
    # print(next(n1))     # 1
    # print(next(n1))     # 2
    # print(next(n1))     # 3
    # print("--------------------")
    # for i in n1:        # 遍历
    #     print(i)
    # # print(next(n1))     # StopIteration
    # print("-----生成器表达式-----")
    # print(i*2 for i in range(8))
    # print(list(i*2 for i in range(8)))

    # 3. 推导表达式
    # print("------推导表达式-----")
    # print("------1） 列表推导式-----")
    # list1 = [i * j for i in range(10) if i % 2 != 0     # 1, 3, 5, 7, 9
    #                 for j in range(10) if j % 3 == 0]   # 0, 3, 6, 9
    # print(list1)
    # print("------2） 字典推导式-----")
    # dict1 = {i: i**2 for i in range(10)}
    # print(dict1)
    # dict2 = {"name" + str(i): "phone" + str(i) for i in range(1,6)}
    # print(dict2)
    # print("------3） 集合推导式-----")
    # set1 = {i**2 for i in range(10)}
    # print(set1)

    # 4. 匿名函数
    # print("------匿名函数-----")
    # # 1） 无参数无返回值
    # l1 = lambda : print("这是一个匿名函数")
    # l1()
    # # 2） 有参数无返回值
    # l2 = lambda x: print(x ** 2)
    # l2(3)
    # # 3） 无参数有返回值
    # l3 = lambda: [i ** 2 for i in range(15) if i % 3 == 0]
    # print(l3())
    # # 4） 有参数有返回值
    # l4 = lambda x, y: x ** y
    # print(l4(3, 3))

    # 5. for 循环简化：
    # print("-----for循环简化-----")
    # print(time.time())
    # for _ in range(100):
    #     print("hello")
    # print(time.time())
    # for i in range(100):
    #     print("kenny")
    # print(time.time())
    pass
    # 6. 闭包函数
    # 1） 函数嵌套
    # outer_fun()
    # # 2) 函数名赋值
    # var1 = outer_fun
    # var1()
    # 3) 闭包函数
    # def outer_fun2(num1):
    #     print(f"我是outer_fun2(): num1={num1}")
    #     def inner_fun2(num2):
    #         print(f"我是inner_fun2(): num2={num2}")
    #         print(f"num1 + num2 = {num1 + num2}")
    #     return inner_fun2
    # x = outer_fun2(3)
    # x(1)
    pass
    # 闭包计数器
    def mycounter():
        count = 0
        def counter():
            nonlocal count
            count += 1
            return count
        return counter
    c = mycounter()
    print(c())
    print(c())
    print(c())
    print(c())
    print(c())
    print(c())