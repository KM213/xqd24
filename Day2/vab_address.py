"""
Day2 10.11
关于python的intern机制在不同情况下的效果，如整数，浮点数，字符串，input输入值等
"""

# 浮点数
print("================= 浮点数的存储 ==================")        # ================= 浮点数的存储 ==================
val1 = float(input("请输入第一个浮点数值：") )                     # 请输入第一个浮点数值：4.5
val2 = float(input("请输入第二个浮点数值：") )                     # 请输入第二个浮点数值：4.5
print(f"val1 == val2  : {val1 == val2}")                        # val1 == val2  : True
print(f"val1 is val2  : {val1 is val2}")                        # val1 is val2  : False
print(f"id(val1)={id(val1)}  id(val2)={id(val2)}")              # id(val1)=2119998213584  id(val2)=2119998214544
print("浮点数常量赋值：")                                         # 浮点数常量赋值：
val3 = 4.5                                                      #
val4 = 4.5                                                      #
print(f"val3 == val4  : {val3 == val4}")                        # val3 == val4  : True
print(f"val3 is val4  : {val3 is val4}")                        # val3 is val4  : True
print(f"id(val3)={id(val3)}  id(val4)={id(val4)}")              # id(val3)=2119998220848  id(val4)=2119998220848
print("------------------------------------------------")       # ------------------------------------------------

# 整数
print("================== 整数的存储 ===================")        # ================== 整数的存储 ===================
val1 = int(input("请输入第一个整数数值：") )                       # 请输入第一个整数数值：123
val2 = int(input("请输入第二个整数数值：") )                       # 请输入第二个整数数值：123
print(f"val1 == val2  : {val1 == val2}")                        # val1 == val2  : True
print(f"val1 is val2  : {val1 is val2}")                        # val1 is val2  : True
print(f"id(val1)={id(val1)}  id(val2)={id(val2)}")              # id(val1)=140721836529912  id(val2)=140721836529912
print("整数常量赋值：")                                           # 整数常量赋值：
val3 = 123                                                      #
val4 = 123                                                      #
print(f"val3 == val4  : {val3 == val4}")                        # val3 == val4  : True
print(f"val3 is val4  : {val3 is val4}")                        # val3 is val4  : True
print(f"id(val3)={id(val3)}  id(val4)={id(val4)}")              # id(val3)=140721836529912  id(val4)=140721836529912
print("------------------------------------------------")       # ------------------------------------------------


# 字符串
print("================= 字符串的存储 ===================")       # ================= 字符串的存储 ===================
val1 = input("请输入第一个字符串值：")                             # 请输入第一个字符串值：abc
val2 = input("请输入第二个字符串值：")                             # 请输入第二个字符串值：abc
print(f"val1 == val2  : {val1 == val2}")                        # val1 == val2  : True
print(f"val1 is val2  : {val1 is val2}")                        # val1 is val2  : False
print(f"id(val1)={id(val1)}  id(val2)={id(val2)}")              # id(val1)=2120025761680  id(val2)=2120025761728
print("字符串常量赋值：")                                         # 字符串常量赋值：
val3 = "abc"                                                    #
val4 = "abc"                                                    #
print(f"val3 == val4  : {val3 == val4}")                        # val3 == val4  : True
print(f"val3 is val4  : {val3 is val4}")                        # val3 is val4  : True
print(f"id(val3)={id(val3)}  id(val4)={id(val4)}")              # id(val3)=140721835438920  id(val4)=140721835438920
print("------------------------------------------------")       # ------------------------------------------------