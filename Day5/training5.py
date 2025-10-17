"""
Day5 10.15
练习
"""
from typing import Optional

# Part 1
# 1. 编写程序，定义一个全局变量count = 0，再定义函数increment()，函数内部使用global关键字修改count的值（每次加 1）。调用函数 3 次后，打印count的结果。
count = 0
def increment():
    global count
    count += 1
# 2. 定义函数add_num(a, b)，函数内部计算a + b并返回结果。在函数外部调用该函数（传入两个整数），并打印返回的和。
def add_num(a, b):
    return a + b
# 3. 定义全局变量message = "Hello"，再定义函数print_message()，函数内部创建同名局部变量message = "Hi"，并打印该局部变量。调用函数后，再打印全局变量message，观察两者的区别。
message = "Hello"
def print_message():
    message = "Hi"
    print(message)
# 4. 编写程序，定义函数calculate(n)，函数内部定义局部变量square = n **2和cube = n** 3，返回这两个值。在外部调用函数，接收返回值并打印 “n 的平方是 x，立方是 y”。
def calculate(n):
    square = n ** 2
    cube = n ** 3
    return square, cube
# 5. 定义全局变量total = 0，编写函数sum_numbers(numbers)，函数内部使用global声明total，并将列表numbers中所有元素累加到total中。调用函数两次（传入不同列表），打印最终的total。
total = 0
def sum_numbers(numbers:Optional[list]):
    global total
    for i in numbers:
        total += i

# 6. 定义函数show_info()，函数内部未使用global声明，直接尝试修改全局变量name = "Alice"（全局变量初始值为 "Bob"），观察是否会报错，并解释原因。
name = "Bob"
def show_info():
    name = "Alice"  # 不报错，在函数内部不使用global而直接修改全局变量，会视为在函数内部创建一个同名的局部变量并赋值

# 7. 编写两个函数set_value(x)和get_value()，set_value内部定义局部变量value = x，get_value尝试访问value。运行程序，观察是否能成功获取，并说明理由。
def set_val(x):
    value = x
def get_val():
    # print(value)    # 报错：NameError: name 'value' is not defined. Did you mean: 'False'?
                        # 原因：value是在set_value()函数中定义的局部变量，只在该函数内部有效，而在get_value()函数中无效，会被视为未定义的变量
    pass
# 8. 定义全局变量PI = 3.14，编写函数circle_area(radius)，函数内部使用全局变量PI计算圆的面积并返回。调用函数计算半径为 5 的圆面积并输出。
PI = 3.14
def circle_area(radius):
    global PI
    return PI * radius ** 2
# 9. 定义函数outer()，函数内部定义局部变量x = 10，再定义嵌套函数inner()，inner函数使用nonlocal关键字修改x的值为 20。调用outer()后，打印x的结果。
def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    print(x)
# 10. 编写程序，全局变量list_data = [1, 2, 3]，定义函数modify_list()，函数内部不使用global，直接向list_data中添加元素 4。调用函数后，打印list_data，观察列表是否被修改，并解释原因。
list_data = [1, 2, 3]
def modify_list1():
    list_data.append(4)     # 成功添加，
def modify_list2():
    list_data = [1, 2, 3, 4, 5]     # 不会被修改，而是在modify_list2内部创建一个局部变量 list_data
    print(f"in modify_list2: {list_data}")

# Part 2
# 1.编写一个函数greet(name, greeting="Hello")，其中name是位置参数，greeting是默认值为 "Hello" 的参数。
# 函数功能是返回拼接后的问候语（如greet("Alice")返回 "Hello, Alice!"，greet("Bob", "Hi")返回 "Hi, Bob!"）。
# 调用函数测试两种情况并输出结果。
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")
# 2.定义函数sum_numbers(*args)，使用可变参数接收任意数量的整数，返回这些整数的总和。
# 调用函数时分别传入 2 个、3 个、5 个数字进行测试，并打印结果（例如传入 1,2,3 返回 6，传入 5,10 返回 15）。
def sum_numbers(*args):
    sum = 0
    for i in args:
        sum += int(i)
    return sum
# 3.编写函数calculate_total(price, quantity=1, *discounts)，其中：
# price是商品单价（位置参数），
# quantity是购买数量（默认值 1），
# *discounts是可变参数，接收任意数量的折扣金额（如优惠券金额）。
# 函数需计算：总金额 = 单价 × 数量 - 所有折扣总和（折扣总和不超过总金额，最低为 0）。
# 测试案例：calculate_total(100, 2, 10, 20)应返回 170（100×2 - 30 = 170）。
def calculate_total(price, quantity=1, *discounts):
    print(f"商品价格：{price}  购买数量：{quantity}")
    print(f"折扣：")
    sum = 0
    for discount in discounts:
        print(f"-{discount}")
        sum += float(discount)
    print(f"折扣总计：{sum}")
    total = price * quantity - sum
    print(f"最终价格：{total}")

# 4.定义函数print_user_info(name, age, **kwargs)，其中：-name和age是位置参数，-** kwargs接收用户的其他信息
# （如 "gender"、"hobby" 等键值对）。函数功能：先打印 "姓名：xxx，年龄：xxx"，
# 再遍历kwargs打印所有额外信息（如 "性别：男"、"爱好：阅读"）。
# 调用函数时传入print_user_info("小明", 18, gender="男", hobby="篮球")并观察输出。
def print_user_info(name, age, **kwargs):
    print(f"姓名：{name}")
    print(f"年龄：{age}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# 5.设计一个函数order_food(main_dish, *sides, drink="可乐", **extras)，
# 参数说明：
# -main_dish：主菜（必传位置参数，如 "汉堡"），
# -*sides：可变参数，接收任意数量的配菜（如 "薯条"、"鸡翅"），
# -drink：饮品（默认值 "可乐"），
# -** extras：关键字可变参数，接收额外要求（如 "少冰 = True"、"加辣 = False"）。
# 函数需返回订单详情字符串，
# 例如：order_food("牛排", "沙拉", "面包", drink="果汁", 少盐=True)应返回："主菜：牛排，配菜：[' 沙拉 ', ' 面包 ']，
# 饮品：果汁，额外要求：{' 少盐 ': True}"。
def order_food(main_dish, *sider, drink="可乐", **extras):
    print(f"主食：{main_dish}")
    print(f"副食：{list(sider)}")
    # for i in sider:
    #     print(f"{i}", end=" ")
    print(f"饮料：{drink}")
    print(f"备注：")
    for i,j in extras.items():
        print(f"{i}, {j}")


if __name__ == '__main__':
    # 1
    # increment()
    # increment()
    # increment()
    # print(count)
    # 2
    # sum = add_num(1, 2)
    # print(sum)
    # 3
    # print(message)
    # print_message()
    # print(message)
    # 4
    # n = 5
    # x, y = calculate(n)
    # print(f"{n}的平方是{x}，立方是{y}")
    # 5
    # list1 = [1, 2, 3, 4, 5]
    # list2 = [2, 4, 6, 8, 1]
    # sum_numbers(list1)
    # print(total)
    # sum_numbers(list2)
    # print(total)
    # 6
    # show_info()
    # print(name)
    # 7
    # set_val(5)
    # get_val()
    # 8
    # area = circle_area(6)
    # print(area)
    # 9
    # outer()
    # 10
    # modify_list1()
    # print(list_data)
    # modify_list2()
    # print(list_data)
    pass
    # Part 2
    # 1.
    # greet("Kenny", "Hi")
    # 2.
    # sum = sum_numbers(2, 3, 4)
    # print(sum)
    # 3.
    # calculate_total(10, 5, 1.8, 4.5)
    # 4.
    # print_user_info("kenny", 37, sex="男",身高=1.86, hobby="读书" )
    # 5.
    # order_food("鸡腿堡", "鸡米花", "薯条", drink="冰咖啡", 少辣=False, 番茄酱=True)