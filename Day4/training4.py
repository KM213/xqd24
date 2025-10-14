"""
Day4 10.14
练习
"""

# Part 1
# 编写程序，让用户输入一个字符串，使用len()函数计算并输出该字符串的长度（包含空格和符号）。
def fun1():
    str1 = input("输入一个字符串：")
    l = len(str1)
    print(l)
# 让用户输入一个主字符串和一个子字符串，使用find()函数判断子字符串是否在主字符串中。如果存在，输出其首次出现的位置；如果不存在，输出 “子字符串未找到”。
def fun2():
    str1 = input("输入主串：")
    str2 = input("输入子串：")
    if len(str2) > len(str1):
        print("子串太长")
    else:
        x = str1.find(str2)
        if x != -1:
            print(f"首次出现位置：{x}")
        else:
            print("子字符串未找到")

# 定义字符串s = "abracadabra"，使用count()函数分别计算字母 "a" 和 "abra" 在字符串中出现的次数，并输出结果。
def fun3():
    s = "abracadabra"
    print(f"主串：{s}")
    print(f"字母 a 出现次数：{s.count('a')}")
    print(f"子串 abra 出现次数：{s.count('abra')}")
# 编写程序，接收用户输入的一句话（包含多个 "bad"），使用replace()函数将所有 "bad" 替换为 "good"，并输出替换后的句子。
def fun4():
    words = input("请输入一句话（包含多个'bad'）：")
    new = words.replace('bad', 'good')
    print(f"替换后：{new}")
# 让用户输入一个用逗号分隔的水果名称字符串（例如 "apple,banana,orange"），使用split()函数将其拆分为列表，然后输出列表中的每个水果名称（每行一个）。
def fun5():
    str1 = input("输入一个水果列表（逗号分隔）:")
    l1 = str1.split(',')
    print(l1)
    for i in l1:
        print(i)
# 定义字符串s = " Hello World! "，使用strip()函数去除首尾空格后，再输出处理后的字符串及其长度（对比处理前后的变化）。
def fun6():
    s = " Hello World! "
    print(f"原始字符串：{s}")
    print(f"原始长度：{len(s)}")
    x = s.strip()
    print(f"去除首尾空格：{x}")
    print(f"处理后长度：{len(x)}")
# 编写程序，让用户输入一个包含数字的字符串（例如 "a1b2c3d4"），使用count()函数计算其中数字字符（0-9）的总个数并输出。
def fun7():
    str1 = input("输入一个包含数字的字符串：")
    sum = 0
    for i in range(10):
        sum += str1.count(str(i))
    print(f"数字总个数：{sum}")
# 接收用户输入的邮箱地址（例如 "user.name@example.com"），先用strip()去除首尾空格，再用find()判断是否包含 "@" 符号。如果包含，输出 "邮箱格式有效"；否则输出 "邮箱格式无效"。
def fun8():
    email = input("输入邮箱地址：")
    str1 = email.strip()
    if str1.find('@'):
        print(f"邮箱 {str1} 格式有效")
    else:
        print(f"邮箱 {str1} 格式无效")
# 定义字符串s = "python is fun, python is powerful"，使用replace()函数仅将第一个 "python" 替换为 "Python"，并输出修改后的字符串。
def fun9():
    s = "python is fun, python is powerful"
    print(f"替换前：{s}")
    x = s.replace('python', 'Python', 1)
    print(f"替换后：{x}")
# 让用户输入一句可能包含多余空格的话（例如 "I love programming"），先用strip()去除首尾空格，再用split()和join()将中间的多个空格替换为单个空格，最后输出处理后的句子。
def fun10():
    str1 = input("输入一个英文句子（包含多余空格）：")
    x = str1.strip()
    y = x.split()
    z = " ".join(y)
    print(f"处理后：{z}")


# Part 2
# 定义一个包含 5 个整数的列表，编写程序计算列表中所有元素的和与平均值，并输出结果。
def fun11():
    l1 = [4, 7, 2, 10, 9]
    sum = 0
    count = 0
    for i in l1:
        sum += i
        count += 1
    print(f"和：{sum}")
    print(f"平均值：{sum/count}")
# 让用户输入 3 个喜欢的水果名称，将它们存入列表后，打印列表的长度，再用索引访问并输出第二个水果名称。
def fun12():
    l1 = []
    for i in range(3):
        fruit = input("输入水果名称：")
        l1.append(fruit)
    print(f"长度：{len(l1)}")
    print(f"第二个水果：{l1[1]}")
# 定义字典student = {"name": "小明", "age": 15, "score": 92}，修改 "score" 的值为 95，添加 "gender" 键值对（值为 "男"），然后打印修改后的完整字典。
def fun13():
    student = {"name": "小明", "age": 15, "score": 92}
    print(f"初始信息：{student}")
    student['score'] = 95
    student['gender'] = '男'
    print(f"修改后：{student}")
# 编写程序，创建一个包含 10 个数字的列表，使用循环遍历列表，将所有偶数存入新列表并输出。
def fun14():
    l1 = [3, 10, 33, 17, 4, 28, 9, 60, 11, 2]
    l2 = []
    for i in l1:
        if i % 2 == 0:
           l2.append(i)
    print(f"l1: {l1}")
    print(f"l2: {l2}")
# 让用户输入 5 个整数，存入列表后，对列表进行降序排序并输出排序后的结果。
def fun15():
    l1 = []
    for i in range(5):
        num = int(input("输入5个数字："))
        l1.append(num)
    l1.sort(reverse=True)
    print(f"倒序排序：{l1}")
# 定义字典scores = {"语文": 85, "数学": 92, "英语": 78}，计算所有科目分数的总和，并用items()方法遍历字典，打印每个科目的分数。
def fun16():
    scores = {"语文": 85, "数学": 92, "英语": 78}
    sum = 0
    for i, j in scores.items():
        print(f"科目：{i}    得分：{j}")
        sum += j
    print(f"总分：{sum}")

# 编写程序，将两个列表list1 = [1, 2, 3]和list2 = ["a", "b", "c"]合并成一个字典，其中 list1 的元素为键，list2 的元素为值。
def fun17():
    list1 = [1, 2, 3]
    list2 = ["a", "b", "c"]
    dict1 = {}
    for i, j in zip(list1, list2):
        dict1[i] = j
    print(f"合并字典：{dict1}")
# 创建一个列表，包含重复元素（如[2, 5, 2, 7, 5, 9]），编写程序去除列表中的重复元素，保留首次出现的元素（结果如[2, 5, 7, 9]）。
def fun18():
    l1 = [2, 5, 2, 7, 5, 9]
    l2 = []
    for i in l1:
        if i in l2:
            l1.remove(i)
        else:
            l2.append(i)
    print(f"处理后：{l1}")
# 让用户输入一个句子，将句子按空格拆分成单词列表，统计列表中单词的数量，并输出最长的单词（若有多个同长单词，输出第一个）。
def fun19():
    words = input("输入一个句子（包含空格）：")
    l1 = words.split()
    len1 = 0
    index1 = 0
    for i in l1:
        if len(i) > len1:
            len1 = len(i)
            index1 = l1.index(i)
    print(f"单词数：{len(l1)}")
    print(f"最长单词：{l1[index1]}")

# 定义字典products = {"苹果": 5.9, "香蕉": 3.5, "橙子": 4.2}，让用户输入水果名称，若存在则输出其价格；若不存在则输出 "该水果未上架"。
def fun20():
    products = {"苹果": 5.9, "香蕉": 3.5, "橙子": 4.2}
    fruit = input("输入水果名称：")
    if fruit in products:
        print(f"{fruit}的价格：{products[fruit]}")
    else:
        print(f"{fruit}未上架")



if __name__ == '__main__':
    fun20()
    pass