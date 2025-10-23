"""
Day11 10.22  练习

"""

# 1. 基础计时装饰器
# 题目：编写一个装饰器timer，用于计算被装饰函数的执行时间（精确到毫秒），并在函数执行结束后打印 “函数 xxx 执行时间：xxx 毫秒”。
# 示例：运行
# @timer
# def test():
#     for i in range(1000000):
#         pass
# test()  # 输出类似：函数test执行时间：23毫秒

import time
def timer(func):
    def inner():
        print("开始计时")
        time1 = time.time()
        func()
        time2 = time.time()
        print("结束计时")
        print(f"函数执行时间为：{time2-time1}")
    return inner
@timer
def fun1():
    print("hello")
    time.sleep(2)

# 2. 日志装饰器（打印参数和返回值）
# 题目：编写装饰器log，使被装饰的函数在调用时：
# 先打印 “调用函数 xxx，参数：xxx”（参数以元组形式展示）
# 函数执行后打印 “函数 xxx 返回值：xxx”
# 示例：运行
# @log
# def add(a, b):
#     return a + b
# add(3, 5)
# # 输出：
# # 调用函数add，参数：(3, 5)
# # 函数add返回值：8
def log(func):
    def inner(*args):
        print(f"调用函数 {func.__name__}, 参数：{args}")
        result= func(*args)
        print(f"函数{func.__name__}返回值：{result}")
    return inner
@log
def fun2(name, age):
    print(f"姓名为{name}, 年龄为{age}")
    return name

# 3. 权限验证装饰器
# 题目：编写装饰器check_permission，要求：
# 装饰器接收一个参数required_role（如 "admin"）。
# 被装饰的函数调用时，先检查全局变量current_role是否等于required_role：
# 若相等，正常执行函数；
# 若不等，打印 “权限不足，无法执行 xxx” 并返回None。
# 示例：运行
# current_role = "user"  # 全局变量：当前用户角色
# @check_permission("admin")
# def delete_data():
#     print("数据删除成功")
# delete_data()  # 输出：权限不足，无法执行delete_data
current_role = "user"
def check_permission(required_role):
    def check(func):
        def wrapper(*args, **kwargs):
            if current_role == required_role:
                return func(*args, **kwargs)
            else:
                print(f"权限不足，无法执行{func.__name__}")
                return None
        return wrapper
    return check
@check_permission("admin")
def fun3():
    print("函数fun3执行")

# 4. 缓存装饰器（记忆化）
# 题目：编写装饰器cache，为被装饰的函数添加缓存功能：
# 第一次调用函数时，计算结果并缓存（用字典存储 “参数→结果”）。
# 后续调用若参数相同，直接返回缓存的结果，不再重新计算。
# 示例：运行
# @cache
# def slow_add(a, b):
#     print("正在计算...")  # 仅第一次调用时打印
#     return a + b
# print(slow_add(2, 3))  # 输出：正在计算...  5
# print(slow_add(2, 3))  # 输出：5（直接用缓存，不打印“正在计算”）
def cache(func):
    cache = {}
    def inner(*args, **kwargs):
        if args in cache:
            print(f"参数已缓存，直接取用结果")
            print(f"args:{args}, 结果：{cache[args]}")
            return cache[args]
        else:
            print("正在计算...")
            result = func(*args, **kwargs)
            cache[args] = result
            return result
    return inner
@cache
def fun4(a, b):
    print(f"{a} + {b} = {a+b}")
    return a+b

# 5. 函数调用次数统计装饰器
# 题目：编写装饰器count_calls，统计被装饰函数被调用的次数，并在函数每次执行后打印 “函数 xxx 已被调用 xxx 次”。
# 示例：运行
# @count_calls
# def greet(name):
#     print(f"Hello, {name}!")
#
# greet("Alice")  # 输出：Hello, Alice!  函数greet已被调用1次
# greet("Bob")    # 输出：Hello, Bob!  函数greet已被调用2次
def count_calls(func):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        func(*args, **kwargs)
        counter += 1
        print(f"函数{func.__name__}已被调用{counter}次")
    return inner
@count_calls
def fun5(account, money):
    print(f"账号【{account}】取款金额：{money}")




if __name__ == '__main__':
    # 1. 基础计时装饰器
    # fun1()
    # 2. 日志装饰器（打印参数和返回值）
    # fun2("kenny", "37")
    # 3. 权限验证装饰器
    # current_role = "user"
    # fun3()
    # current_role = "admin"
    # fun3()
    # 4. 缓存装饰器（记忆化）
    # fun4(3, 5)
    # fun4(4, 5)
    # fun4(3, 5)
    # 5. 函数调用次数统计装饰器
    fun5("123456", 1000)
    fun5("123456", 100)
    pass