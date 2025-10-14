"""
Day4 10.14
1. 字符串处理函数：
        len()
        find()
        count()
        replace()
        split()
        strip()
2. 列表
        定义      []
        访问使用    下标
            增   append、extend、insert
            删   pop、del、remove
            改   指定下标赋值
            查   下标、for循环遍历（for i in list: print i）
        操作函数
            len()   求长度，即列表元素个数
            sort()  排序，默认升序；设定参数reverse=True为降序
            index() 查找指定列表元素的索引
            reverse()   将列表翻转
3. 元组
        定义  ()
            定义单个元素的元组时，需要与int类型数据的运算括号区分开，在元组唯一元素后面加个逗号。表示为元组类型    (1,)
        访问使用    下标
            增   元组元素不可修改，故不能新增元素
            删   del tuple1     只能删除整个元组变量，不能删除某个元素或清除所有元素
            改   可以修改元组变量，即为元组变量赋予新的元组值。但不能修改元组内的元素值
            查   tuple1[index]
                遍历  for i in tuple1:    print(i)
        元组嵌套
            嵌套列表：tuple2 = (1, 2, 3, [4, 5, 6])
                元组元素不可修改，但其内部嵌套的列表等可变序列的值可修改,如：
                tuple2[3] = [3, 2, 1]   # TypeError: 'tuple' object does not support item assignment
                tuple2[3][1] = 0        # 正常修改

4. 字典
    定义  {}
    访问使用
        增   dict1['newkey'] = 'newval'
        删   del dict1['key']
        改   dict1['key'] = 'val'
        查   print(dict1['key'])     查看指定键的值
            for i in dict1.keys()   遍历键
            for j in dict1.values() 遍历值
            for i ,j in dict1.items()   遍历键值对
    相关函数：
        keys()      列表形式返回字典中所有的键：dict_keys(['key1', 'key2', 'key3'])
        values()    列表形式返回字典中所有的值：dict_values(['value1', 'value2', 'value3'])
        items()     列表嵌套元组形式返回字典中所有的键值对：dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])


"""
def fun1():
    str1 = "b123 456abc defgab"
    print(len(str1))

    print(str1.count("a"))
    print(str1.count("a", 10, ))

    print(str1.find("a"))
    print(str1.find("a", 0, 10))

    print(str1.split("a"))
    print(str1.split("a", 1))

    print(str1.strip("b"))

    print(str1.replace("b", "B"))
    print(str1)

def fun2():
#     定义：
    list1 = []      # 定义空列表
    list2 = [123, "a", 4.5, False, 0]   #定义并初始化列表值
#     访问值
    print(f"list1: {list1}  list2: {list2}")     # 直接输出列表
    print(f"list2: {list2[3]}")         # 下标输出列表
    print(f"list2: {list2[3:]}")        # 切片输出列表
#     修改值
    list2[4] = "kenny"
    print(f"list2: {list2}")
#     删除值
    del list2[3]
    print(f"list2: {list2}")
    list2.pop(2)
    print(f"list2: {list2}")
    list2.remove("a")
    print(f"list2: {list2}")
#     增加值
    list1.append("123")
    print(f"list1: {list1}")
    list1.extend(["111", "lin"])
    print(f"list1: {list1}")
    list2.insert(2, "222")
    print(f"list2: {list2}")


    list2.reverse()
    print(f"list2: {list2}")

def fun3():
    tup1 = (1, 2, 3, [4, 5, 6])
    print(f"tup1: {tup1}")
    print(tup1[3])
    # tup1[3] = [3, 2, 1]     # TypeError: 'tuple' object does not support item assignment
    tup1[3][1] = 0
    print(f"tup1: {tup1}")
    # del tup1[2]             # TypeError: 'tuple' object doesn't support item deletion
    # print(f"tup1: {tup1}")
    tup1 = (6, 5, 4, 3, 2, 1)
    print(f"tup1: {tup1}")

    del tup1
    # print(f"tup1: {tup1}")


def fun4():
    dict1 = {'name':'kenny', 'sex':'man','phone':'19991389278'}
    print(f"dict1: {dict1}")
    # 增
    dict1['job'] = 'actor'
    print(f"dict1: {dict1}")
    # 删
    del dict1['sex']
    print(f"dict1: {dict1}")
    # 改
    dict1['job'] = 'artist'
    print(f"dict1: {dict1}")
    # 查
    print(f"dict1.keys: {dict1.keys()}")
    print(f"dict1.values: {dict1.values()}")
    print(f"dict1.items: {dict1.items()}")

    for i in dict1.keys():
        print(i)
    for j in dict1.values():
        print(j)
    for i, j in dict1.items():
        print(i, j)
    for i in dict1.items():
        print(i)


if __name__ == '__main__':
    fun4()