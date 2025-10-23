"""
Day5 10.15
1. 函数：代码的容器
        定义： def function(参数)：
                函数体
                return 返回值： 1. 返回函数结果   2. 结束函数   3. 不跟返回值，默认返回 None
        参数：
                形式参数：定义函数时产生的只用于函数内部的临时变量
                实际参数：调用函数时传入的值

                位置参数：定义函数时就将参数的位置及名称固定，实参必须按照形参的固定顺序进行传递
                关键字参数：传参数时采用 形参名=实参值 的形式进行传递，则传参顺序可任意调整
                        关键字参数必须在位置参数之后。以便位置参数能以固定顺序传递，关键字参数任意顺序传递
                默认值参数：创建形参时给形参设置默认值，如过调用函数时没有传该参数值，则使用默认值。
                        默认值参数必须放在参数列表末尾
                收集参数：
                    打包参数：用于形参上。定义形参时在参数名前加*号，在传参时传入的多个参数会以元组形式打包存储(当加两个星号**时，则可传入多个关键字参数并打包为字典)，两者可以混合使用
                    解包参数：用于实参上。当将要传入的多个参数用元组打包后一次性传入函数时，参数前加上*星号，会被解包为收集参数（传入字典时，就加两个星号**，将字典解包为关键字参数）
                            如果函数在收集参数后还存在其它参数，则在传参时需要使用关键字参数来传入后面参数的值，否则参数值都会被纳入收集参数之中。
                混合使用时的顺序应该是：位置参数 *收集参数 关键字参数 **收集参数  [默认值参数在混合参数列表中可以使用关键字传参]

2. 变量与作用域：
        全局变量：在函数外部定义的变量
                在整个程序中都可用（除非被局部变量覆盖）
                生命周期从定义开始到程序结束
        局部变量：在函数内部定义的变量（包括参数）
                只在定义它的函数内部可用
                生命周期从函数调用开始到函数结束
        作用域：
            局部作用域：
                在函数内部，局部变量优先于全局变量。
            全局作用域：
                在函数外部，只能访问全局变量。
            在函数内部访问全局变量：
                可以直接读取全局变量的值，但是如果要修改全局变量，必须使用global关键字声明。
                如果不使用global关键字，而在函数内部对与全局变量同名的变量进行赋值，将会创建一个新的局部变量，并不会改变全局变量的值
            嵌套函数中：
                内部函数可以访问外部函数的变量（非全局变量）。如果要修改外部函数的变量，需要使用nonlocal关键字

        例题：# 编写程序，全局变量list_data = [1, 2, 3]，定义函数modify_list()，函数内部不使用global，直接向list_data中添加元素 4。调用函数后，打印list_data，观察列表是否被修改，并解释原因。
            list_data = [1, 2, 3]  # 创建列表对象，list_data 引用该对象
            def modify_list():
                # 这里没有对 list_data 重新赋值，只是调用了它的方法
            list_data.append(4)  # 修改列表对象的内容，不改变 list_data 的引用
            list_data = [1, 2, 3, 4]  # 创建了局部变量list_data,原本的全局变量值依旧不变

3. 类：面向对象
        面向过程：函数编程
        面向对象：类编程

        定义：Python中使用CapWords约定（也称为驼峰命名法）来命名类。具体来说，每个单词的首字母大写，且不使用下划线分隔单词。
                属性：设定属性
                方法：设定行为

"""

def fun1(num, power):
    num3 = num ** power
    return num3

def fun2():
    aa = 123
    print(aa)
    print(bb)
    print(cc)   # NameError: name 'cc' is not defined

# print(aa)   # NameError: name 'aa' is not defined

# 位置参数、关键字参数、默认参数、收集参数
def myarg(a,b,*n, c, x=0, **nums):
    print(f"位置参数：{a},{b}")
    print(f"关键字参数：{c}")
    print(f"默认值参数：{x}")
    print(f"收集元组参数：{n}， {type(n)}")
    print(f"收集列表参数{nums}， {type(nums)}")


# 3. 定义一个狗的模板：
# 属性：颜色、品种、性别
# 行为：叫、跑、吃饭、睡觉
class Dog:
    # 属性：
    def __init__(self, color, variety, sex):
        self.color = color
        self.variety = variety
        self.sex = sex

    # 行为
    # 叫
    def shot(self, sing):
        print(sing)
    # 跑
    def run(self, sing):
        print(sing)
    # 吃饭
    def eat(self, food):
        print(f"吃掉一个{food}")
    # 睡觉
    def sleep(self):
        print("zZZ")

# 变量作用域
global_var = "I'm global"  # 全局变量
def test_scope():
    local_var = "I'm local"  # 局部变量
    print(global_var)  # 可以访问全局变量
    print(local_var)   # 可以访问局部变量
def edit():
    local_var = "I'm local after edit"
    global_var = "I'm global after edit by fun"
    print(local_var)
    print(global_var)
test_scope()
edit()
# print(local_var)  # 错误！局部变量在外部不可访问

# bb = 111
# if __name__ == '__main__':
#     # 传参
#     # num4 = fun1(5, 2)
#     # print(num4)
#
#     # 变量与作用域
#     # fun2()
#
#     # 参数
#     # myarg(1,2, 3,4,5, c=6, x=8, n1=1,n2=2,n3=3)
#
#     # 类：
#     # ba = Dog("yellow", "金毛", "男")
#     # pipi = Dog("gray", "雪纳瑞", "男")
#     # print(ba.color)
#     # print(ba.variety)
#     # print(ba.sex)
#     # ba.shot("汪汪！")
#     # ba.run("咚咚咚")
#     # ba.eat("骨头")
#     # ba.sleep()
#     # print(pipi.color)
#     # print(pipi.variety)
#     # print(pipi.sex)
#     # pipi.shot("呜呜呜")
#     # pipi.run("噔噔噔")
#     # pipi.eat("饼干")
#     # pipi.sleep()
#     pass
# cc = 222
