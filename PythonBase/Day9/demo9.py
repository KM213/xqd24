"""
# Day9 10.20
# 正则表达式：字符串操作，从指定的字符串中查找符合规则的子串
#     规则： 1. 由数字和基本字母以及元字符构成
#             2. 元字符：具有不同于正常含义的字符，便于实现复杂的操作
#             3. 正则表达式是用来描述一类字符串的，而不是直接表示一个具体的字符串
#             4. 正则表达式是预定义的，不是自定义的
#             5. 正则表达式是区分大小写的
#     常用字符：
#             \d   任意数字                 \D   非数字
#             \s   任意空白字符             \S   非空白字符
#             \w   任意字母或数字或下划线    \W   非字母或数字或下划线
#             \n   换行   \r   回车   \t   制表    \v   垂直制表
#             \xhh  十六进制字符       \uhhhh  十六进制unicode字符      \o777  八进制字符
#             \Q   忽略正则表达式中的特殊字符
#             \E   结束忽略           \cx  控制字符
#             \g<0>  匹配     \g<name>  匹配组      \num  匹配第num个组      \gnum  匹配第num个组
#             \p{name}  匹配Unicode某种语言的字符
#             \A   字符串开头          \Z   字符串结尾
#             \G   当前搜索到的上一次匹配后的位置
#             \z   字符串末尾       \b   单词边界      \B   非单词边界
#             \n   n为1-9的数字，表示第n个子组的内容
#             \1   匹配第1个子组的内容
#             []   匹配[]中任意一个字符
#             [^]   匹配不在[]中的任意一个字符
#             [:]   匹配[]中范围内的任意一个字符
#             [=]   匹配[]中范围外的任意一个字符
#             [&]   匹配[]中范围内的任意一个字符
#             [|]   匹配[]中范围外的任意一个字符
#             [~]   匹配[]中范围外的任意一个字符
#             [.]   匹配除了\n之外的任意一个字符
#             [_]   匹配\_
#             [+]   匹配至少一个
#             [*]   匹配0到多个
#             [?]   匹配0或者1次
#             [{}]   匹配{}中任意一个字符
#             [()]   匹配()中任意一个字符
#             [**]   匹配**次
#
# 正则查找常用方法：import re
#         re.findall()      从字符串中查找所有符合规则的子串，返回列表     re.findall(规则,字符串)
#         re.search()       从字符串中查找第一个符合规则的子串，返回对象
#         re.match()        从字符串开始位置查找第一个符合规则的子串，返回对象     re.match(规则,字符串)
#         re.split()        根据规则拆分字符串，返回列表
#         re.sub()          根据规则替换字符串中的内容，返回新的字符串
#         re.compile()      将正则表达式的字符串形式编译成正则表达式对象
#         re.fullmatch()    判断整个字符串是否符合规则，返回布尔值
#         re.escape()       对字符串进行转义，返回新的字符串
#         re.purge()       清除缓存
#         re.I/re.IGNORECASE              忽略大小写
#         re.S              让 . 可以匹配换行符
#         re.X              忽略空白字符
#         re.A              只匹配ascii码
#         re.M              多行模式
#         re.U/re.UNICODE             unicode匹配
#         re.L/re.LOCALE             locale匹配
#         re.DOTALL         点可以匹配任何字符
#         re.VERBOSE        忽略正则表达式中的注释
#         re.DEBUG         显示调试信息
#         re.ASCII          只匹配ascii码
"""




import re
# 1.正则表达式常用符号
# 2. 正则查找常用方法：import re
def fun2():
    str1 = "hello, my name is kenny!Nice to see you!"
    str2 = re.findall("name", str1)
    print(str2, type(str2))                         # ['name'] <class 'list'>

    str3 = re.match("h(e)ll(o)", str1)
    print(str3 ,type(str3))                         # <re.Match object; span=(0, 5), match='hello'> <class 're.Match'>
    print(str3.group(0))                            # hello
    print(str3.group(1))                            # e
    print(str3.group(2))                            # o

    str4 = re.search("name (is)", str1)
    print(str4, type(str4))                         # <re.Match object; span=(10, 17), match='name is'> <class 're.Match'>
    print(str4.group(0))                            # name is
    print(str4.group(1))                            # is

    # 1. 正则规则
    str5 = re.search("name is (.*?)!", str1)
    print(str5, type(str5))                         # <re.Match object; span=(10, 24), match='name is kenny!'> <class 're.Match'>
    print(str5.group(0))                            # name is kenny！
    print(str5.group(1))                            # kenny


if __name__ == '__main__':
    fun2()