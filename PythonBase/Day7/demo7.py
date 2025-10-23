"""
Day7 10.17
面向对象：类编程
    类的特性：
        3. 多态：
                将不同类的对象调用相同的方法，产生不同的结果(如加法、len()方法)
                继承类的重写就是类继承的多态：在所有子类将继承的父类方法进行重写，再进行实例化，则不同的实例化对象调用相同方法会得出不同结果，即为多态

文件操作：数据持久化保存
    1. 打开文件：open("文件路径", "操作参数", encoding="编码")
            文件路径：   绝对路径  D:/CODEs/Python/xqd24/Day7/demo7.py
                        相对路径    ./Day7/demo7.py
            操作参数：    'r'       open for reading (default)      打开文件用于读取，默认是只读
                        'w'       open for writing, truncating the file first   覆盖原文件
                        'x'       create a new file and open it for writing, failing if the file already exists   创建新文件，如果文件已存在则打开失败
                        'a'       open for writing, appending to the end of the file if it exists    追加模式打开文件，写入的内容追加到文件末尾，不覆盖原内容
                        'b'       binary mode    二进制模式
                        't'       text mode (default)    文本模式
                        '+'       open a disk file for updating (reading and writing)    打开一个文件用于读写，默认是只读。需要与其他模式结合使用，如'r+'、'w+'或'a+'
                    * Python里面默认的模式是：'rt'。
                    * 只要有'+'，就变成了可读可写的；可以与w，r，a等进行组合。
                    * 当使用 'a+' 模式打开文件时：文件指针初始位置在文件末尾，而读取操作从当前指针位置开始，所以读取不到任何内容。可以使用f.seek(0)将文件指针移动到开头
            文件编码格式： utf-8
                         gbk
            返回值：一个文件对象
    2. 读取文件：
            1. 一次性读取整个文件：filename.read()
            2. 按行读取文件：filename.readline()
            3. 循环读取文件：for line in filename:
                 print(line)

    3. 写入文件：
            1. 一次性写入：filename.write("要写入的内容")
            2. 追加写入：filename.write("要写入的内容")
    4. 文件指针：
            1. 获取当前位置：filename.tell()
            2. 设置当前位置：filename.seek(偏移量, 起始位置)
    5. 关闭文件： filename.close()
    6. 上下文管理器：可自动关闭文件
        with open("文件路径", "操作参数", encoding="编码") as f:
            pass

异常处理：try-except
    异常： 代码运行时发生逻辑错误，导致程序报错并结束运行
        常见异常：Exception: 所有异常的基类
                ZeroDivisionError: 除数为0
                NameError: 变量未定义
                IndexError: 索引超出范围
                FileNotFoundError: 找不到文件
                ValueError: 传入的参数类型不正确
                TypeError: 传入的参数类型不正确
                SyntaxError: 语法错误
                IndentationError: 缩进错误
                KeyError: 字典中没有这个key
                ImportError: 导入模块失败
                ModuleNotFoundError: 找不到模块
                AttributeError: 属性错误
                AssertionError: 断言错误
                RuntimeError: 运行时错误
                NotImplementedError: 尚未实现
                OSError: 系统错误
                ConnectionError: 连接错误
                TimeoutError: 超时错误
                MemoryError: 内存不足
                OverflowError: 溢出错误
                PermissionError: 权限错误
                KeyboardInterrupt: 用户中断执行
                EOFError: 文件结尾
                ConnectionAbortedError: 连接终止
                ConnectionRefusedError: 连接被拒绝
                ConnectionResetError: 连接重置
                BlockingIOError: 阻塞IO错误
                BrokenBarrierError: 障碍错误
                BrokenPipeError: 管道破裂
                ChildProcessError: 子进程错误
                BufferError: 缓冲区错误
                ArithmeticError: 算术错误
                FloatingPointError: 浮点运算错误
                OverflowError: 溢出错误
                RecursionError: 递归

    异常处理：对异常进行处理，让代码不终止，继续向后执行
        结构：
            try:
                可能出现异常的代码块
            except Exception as e:
                捕获到的异常处理逻辑
            else:
                没有异常时的逻辑
            finally:
                无论是否有异常都会执行的逻辑
        抛出异常：raise Exception("异常信息")    # 显示自定义错误信息
                raise Exception     # 不显示错误信息

模块：后缀是py的文件，可以进行导入
    导入方式： import 模块名    - 导入整个文件/模块
             from 模块名 import 函数名    - 导入文件/模块中的某个函数
"""

# 1. 类继承的多态
class Hreo:
    def __init__(self, hp=1000, mp=1000):
        self.hp = hp
        self.mp = mp
    def print_info(self):
        print(f"英雄名：{self.name}, 红：{self.hp}, 蓝{self.mp}")
    def skill1(self):
        print("1技能")
    def skill2(self):
        print("2技能")
    def skill3(self):
        print("3技能")
# 辅助：妲己
class Support(Hreo):
    def __init__(self, name: str, hp1: int=1000, mp1: int=1000) -> None:
        super().__init__(hp1, mp1)
        self.name = name

    def skill1(self):
        print("技能1：灵魂冲击")
        self.hp -= 60
        self.mp -= 10
    # 技能2：偶像魅力 消耗90
    def skill2(self):
        print("技能2：偶像魅力")
        self.hp -= 90
        self.mp -= 15
    # 技能3：女王崇拜 消耗120
    def skill3(self):
        print("技能3：女王崇拜")
        self.hp -= 120
        self.mp -= 20
# 法师:王昭君
class Master(Hreo):
    def __init__(self, name, hp2=1000, mp2=1000):
        super().__init__(hp2, mp2)
        self.name = name
    # 技能1：凋零冰晶 消耗50
    def skill1(self):
        print("技能1：凋零冰晶")
        self.hp -= 50
        self.mp -= 5
    def skill2(self):
        print("技能2：禁锢寒霜")
        self.hp -= 80
        self.mp -= 10
    # 技能3：凛冬已至 消耗120
    def skill3(self):
        print("技能3：凛冬已至")
        self.hp -= 120
        self.mp -= 20
# 战士：亚瑟
class Warrior(Hreo):
    def __init__(self, name, hp3=1000, mp3=1000):
        super().__init__(hp3, mp3)
        self.name = name

    # 技能1：誓约之盾 消耗0
    def skill1(self):
        print("技能1：誓约之盾")
        self.hp -= 0
        self.mp -= 0
    # 技能2：回旋打击 消耗0
    def skill2(self):
        print("技能2：回旋打击")
        self.hp -= 0
        self.mp -= 0
    def skill3(self):
        print("技能3：圣剑裁决")
        self.hp -= 0
        self.mp -= 0
def fun1():
# 多态
    # daji = Support("妲己", 2000, 3000)
    # wzj = Warrior("王昭君", 2000, 3000)
    # yase = Warrior("亚瑟", 2000, 3000)
    # hero = yase
    # hero.print_info()
    # hero.skill1()
    # hero.skill2()
    # hero.skill3()
    pass

# 2. 文件
def fun2():
    # 创建文件，若文件已存在则删除并创建新文件
    with open("./file_test/test1.txt", "a+", encoding="utf-8") as f:
        # 写入
        # f.write("hello!")
        # name = "张三"
        # phone = "13800138000"
        # f.writelines([name, "\t", phone, "\n"])

        # 读取
        f.seek(0)
        # w1 = f.read()       # 使用 'a+' 模式打开文件时：文件指针初始位置在文件末尾，而读取操作从当前指针位置开始，所以读取不到任何内容
        # print(w1)
        w2 = f.readlines()
        for i in w2:
            print(i.split("\t"))
        # w3 = f.readline()
        # print(w3)
        # 代码块执行结束自动关闭文件

# 3. 异常处理
def fun3():
    try:
        # a = 1 / 0       # 除数为零
        # print(yy)       # 变量未定义
        # li = [1, 2, 3]
        # print(li[3])    # 索引超出范围
        # with open("./111.txt", "r") as f:   # 找不到文件
        #     pass
        fun2(1)  # 传入参数类型不正确

    except Exception as e:
        print("fun3 有异常")
        print(f"异常信息：{e}")
        raise IOError("文件打开失败")
    else:
        print("fun3 没有异常")
    finally:
        print("fun3 已经执行")





if __name__ == '__main__':
    # 多态
    # fun1()
    # 文件
    # fun2()
    # 异常处理
    # try:
    #     fun3()
    # except Exception as e:
    #     print(f"{e}")
    # 模块
    from Day7.train1 import Duck, Dog, animal_sound
    animal = Dog("小八", 14)
    animal.info()
    animal_sound(animal)
    animal2 = Duck("小九", 14)
    animal2.info()
    animal_sound(animal2)
    pass