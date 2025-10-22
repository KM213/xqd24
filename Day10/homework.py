"""
Day10
练习
"""
# Part 1
# 1. 找出1000以内所有能同时被3和7整除的数字并存入列表
def fun1():
    print("1. 找出1000以内所有能同时被3和7整除的数字并存入列表")
    list1 = [i for i in range(1000) if i % 3 ==0 and i % 7 == 0]
    print(list1)

# 2. 找出1000以内的水仙花数 （水仙花数：N位数（n≥3），它的每个位上的数字的n次幂之和等于它本身）
def fun2():
    print("2. 找出1000以内的水仙花数")
    list2 = [i for i in range(100, 1000) if sum(int(j) ** len(str(i)) for j in str(i)) == i and len(str(i))]
    print(list2)

# Part 2
# 1. 简单累加器
# 题目：编写一个闭包函数make_accumulator(init)，其中：
#           外层函数make_accumulator接收初始值init。
#           内层函数add(n)每次被调用时，将n累加到初始值上，并返回当前总和。
# 示例：运行
# acc = make_accumulator(10)
# print(acc(5))   # 输出：15（10+5）
# print(acc(3))   # 输出：18（15+3）
# print(acc(2))   # 输出：20（18+2）
def make_accumulator(n):
    print("1. 简单累加器")
    def add(m):
        nonlocal n
        return n + m
    return add

# 2. 带前缀的打印器
# 题目：编写闭包函数make_printer(prefix)，实现：
#           外层函数接收一个字符串prefix（如 "[日志]"）。
#           内层函数print_msg(msg)被调用时，打印prefix + msg（如print_msg("操作成功")输出 "[日志] 操作成功"）。
# 示例：   运行
# log_printer = make_printer("[日志]")
# log_printer("程序启动")  # 输出：[日志]程序启动
# log_printer("数据加载完成")  # 输出：[日志]数据加载完成
# warn_printer = make_printer("[警告]")
# warn_printer("内存不足")  # 输出：[警告]内存不足
def make_printer(log):
    def print_msg(msg):
        print(log + msg)
    return print_msg

# 3. 计算幂的函数生成器
# 题目：编写闭包函数make_power(exponent)，功能是：
#           外层函数接收一个整数exponent（指数）。
#           内层函数calc(base)被调用时，返回base的exponent次方（即base**exponent）。
# 示例：   运行
# square = make_power(2)  # 生成计算平方的函数
# print(square(3))  # 输出：9（3²）
# print(square(5))  # 输出：25（5²）
def make_power(exp):
    print(f"计算{exp}次幂")
    def calc(base):
        return base ** exp
    return calc

# 4. 计数器（记录调用次数）
# 题目：编写闭包函数make_counter()，实现一个计数器：
#           外层函数无需参数，内部维护一个初始值为 0 的变量count。
#           内层函数count_once()每次被调用时，count加 1，并返回当前count。
# 示例：运行
# counter = make_counter()
# print(counter())  # 输出：1
# print(counter())  # 输出：2
# print(counter())  # 输出：3
def make_counter():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

# 5. 带条件的过滤器
# 题目：编写闭包函数make_filter(threshold)，功能是：
#               外层函数接收一个阈值threshold（整数）。
#               内层函数filter_numbers(numbers)接收一个列表numbers，返回列表中大于threshold的所有元素。
# 示例：运行
# filter_gt5 = make_filter(5)  # 生成过滤出大于5的元素的函数
# print(filter_gt5([3, 7, 2, 9, 5]))  # 输出：[7, 9]
# filter_gt10 = make_filter(10)
# print(filter_gt10([12, 5, 15, 8]))  # 输出：[12, 15]
def make_filter(threshold):
    def filter_numbers(numbers):
        return [i for i in numbers if i > threshold]
    return filter_numbers

if __name__ == '__main__':
    # Part 1
    # fun1()
    # fun2()

    # Part 2
    print("--------------------")
    # 1. 简单累加器
    # print("1. 简单累加器")
    # myadd = make_accumulator(5)
    # print(myadd(4))
    # print(myadd(6))
    # print(myadd(9))
    # 2. 带前缀的打印器
    # print("2. 带前缀的打印器")
    # log_printer = make_printer("【日志】")
    # log_printer("程序启动")
    # log_printer("数据加载完成")
    # warn_printer = make_printer("【警告！】")
    # warn_printer("内存不足！")
    # 3. 计算幂的函数生成器
    # print("3. 计算幂的函数生成器")
    # square = make_power(2)
    # print(square(3))
    # print(square(8))
    # cube = make_power(3)
    # print(cube(3))
    # print(cube(6))
    # 4. 计数器（记录调用次数）
    # print("4. 计数器（记录调用次数）")
    # counter = make_counter()
    # print(counter())
    # print(counter())
    # print(counter())
    # 5. 带条件的过滤器
    print("5. 带条件的过滤器")
    gt15 = make_filter(15)
    print(gt15([3, 18, 2, 15, 99]))
    gt5 = make_filter(8)
    print(gt5([4, 8, 2, 10, 9, 33, 1, 6]))