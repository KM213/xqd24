#1. 计算 1 到 n 的累加和
# 题目：编写递归函数sum_recursive(n)，计算 1+2+3+…+n 的和。提示：
# 终止条件：当 n=1 时，和为 1
# 递归关系：sum (n) = n + sum (n-1)
# 示例：sum_recursive(5) 应返回 15（1+2+3+4+5）
def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n-1)

# 2. 计算 n 的阶乘
# 题目：编写递归函数factorial(n)，计算 n 的阶乘（n! = n×(n-1)×…×1）。提示：
# 终止条件：n=0 或 n=1 时，阶乘为 1
# 递归关系：n! = n × (n-1)!
# 示例：factorial(4) 应返回 24（4×3×2×1）
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

# 3. 计算幂运算（a 的 b 次方）
# 题目：编写递归函数power(a, b)，计算a^b（a 的 b 次方，b 为非负整数）。提示：
# 终止条件：b=0 时，结果为 1（任何数的 0 次方为 1）
# 递归关系：a^b = a × a^(b-1)
# 示例：power(2, 3) 应返回 8（2×2×2）；power(5, 0) 应返回 1
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b-1)

# 4. 计算列表元素的和
# 题目：编写递归函数list_sum(lst)，计算列表lst中所有整数的和（列表元素均为整数）。提示：
# 终止条件：空列表的和为 0
# 递归关系：列表和 = 第一个元素 + 剩余元素组成的子列表的和
# 示例：list_sum([1, 2, 3, 4]) 应返回 10（1+2+3+4）
def list_sum(list1):
    if not list1:
        return 0
    else:
        return list1[0] + list_sum(list1[1:])

# 5. 反转字符串
# 题目：编写递归函数reverse_str(s)，返回字符串s的反转结果（如s="abc"，返回"cba"）。提示：
# 终止条件：空字符串或单字符，反转结果为自身
# 递归关系：反转字符串 = 最后一个字符 + 反转剩余子串
# 示例：reverse_str("hello") 应返回 "olleh"
def reverse_str(str0):
    if len(str0) == 2:
        return str0[::-1]
    else:
        str0 = str0[-1] + reverse_str(str0[:-1])
        return str0


if __name__ == '__main__':
    # 1. 累加和
    # print(sum_n(5))
    # 2. 阶乘
    # print(factorial(5))
    # 3. 幂运算
    # print(power(2, 3))
    # print(power(6, 0))
    # 4. 列表求和
    # print(list_sum([3, 2, 7, 6, 8]))
    # 5. 反转字符串
    print(reverse_str('hello'))