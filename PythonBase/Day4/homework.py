"""
Day5 10.15
作业：定义5个不同的类并实例化
"""

# 1. book类
# 属性：书名、作者、分类、价格、库存
# 方法：展示信息、更新价格、增加库存、减少库存
class Books:
    def __init__(self, name, author, type, price, stock):
        self.name = name
        self.author = author
        self.type = type
        self.price = price
        self.stock = stock

    def print_info(self):
        print(f"书名：{self.name}")
        print(f"作者：{self.author}")
        print(f"类型：{self.type}")
        print(f"价格：{self.price}")

    def set_price(self, price):
        self.price = price
        print(f"更新价格成功！《{self.name}》的价格为：{self.price}")

    def add_stock(self, num):
        self.stock += num
        print(f"增加库存成功！《{self.name}》现有{self.stock}本")

    def sub_stock(self,num):
        self.stock -= num
        print(f"减少库存成功！《{self.name}》剩余{self.stock}本")

# 2. BankAccount类（银行账户类）
# 属性：账号、持有人、余额
# 方法：显示账户信息、存款、取款
class BankAccounts:
    def __init__(self, account, name):
        self.name = name
        self.account = account
        self.balance = 0.0
    # 打印账户信息
    def print_info(self):
        print(f"账号：{self.account}")
        print(f"持有人：{self.name}")
        print(f"余额：{self.balance}")
    # 存款
    def add_balance(self, num):
        self.balance += num
        print(f"存款{num}元，账户余额{self.balance}元")
    # 取款
    def sub_balance(self, num):
        if num > self.balance:
            print("余额不足！")
        else:
            self.balance -= num
        print(f"取款{num}元，账户余额{self.balance}元")

# 3. Employees类（员工类）
# 属性：ID、姓名、职位、工资、奖金
# 方法：显示员工信息、更新职位、计算工资
class Employees:
    def __init__(self, id, name, position, salary, bonus=0):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.bonus = bonus
    # 展示员工信息
    def print_info(self):
        print(f"员工ID：{self.id}")
        print(f"员工姓名：{self.name}")
        print(f"员工职位：{self.position}")
    # 更新职位
    def set_position(self, position):
        self.position = position
        print(f"员工【{self.name}】调至{self.position}岗位")
    # 计算工资
    def sum_salary(self):
        sum = self.salary + self.bonus
        print(f"【{self.name}】本月工资合计{sum}元")

# 4. Students类
# 属性：ID、姓名、性别、班级、成绩(字典)
# 方法：显示信息、更新成绩、计算平均成绩
class Students:
    def __init__(self, id, name, gender,grade, clbum):
        self.id = id
        self.name = name
        self.gender = gender
        self.grade = grade
        self.clbum = clbum
        self.score = {}

    def print_info(self):
        print(f"学号：{self.id}")
        print(f"姓名：{self.name}")
        print(f"性别：{self.gender}")
        print(f"年级：{self.grade}")
        print(f"班级：{self.clbum}班")

    def show_scores(self):
        for course, score in self.score.items():
            print(f"{course}: {score}")

    def set_score(self, **scores):
        for i, j in scores.items():
            self.score[i] = j
        print(f"已更新【{self.name}】的成绩!")

    def avg_score(self):
        sum = 0
        for score in self.score.values():
            sum += float(score)
        avg = sum / len(self.score)
        print(f"【{self.name}】的平均成绩为{avg}分")

# 5. Clbum类(班级类)
# 属性：ID、人数、学生列表
# 方法：查看学生列表、ID查找学生、姓名查找学生
class Clbum:
    def __init__(self, id, num, *stus):
        self.id = id
        self.num = num
        self.stus = stus

    def print_stus(self):
        print("学生列表：")
        for i in self.stus:
            print(i.id, i.name, i.gender, i.grade, i.clbum)

    def find_id(self, id):
        flag = False
        for i in range(len(self.stus)):
            if self.stus[i].id == id:
                print(f"查询学号【{id}】信息如下：")
                self.stus[i].print_info()
                flag = True
        if flag == False:
            print(f"找不到此学生")

    def find_name(self, name):
        flag = False
        for i in self.stus:
            if i.name == name:
                print(f"查询姓名【{name}】信息如下：")
                i.print_info()
                flag = True
        if flag == False:
            print("未找到此学生")

if __name__ == '__main__':
    # 1. book类
    # book1 = Books("青铜葵花","曹文轩","文学小说",35.00, 100)
    # book2 = Books("三体Ⅱ-黑暗森林","刘慈欣","科幻小说",40.00, 150)
    # book3 = Books("活着", "余华", "文学小说", "29.0", "20")
    # book1.print_info()
    # book1.set_price(30.00)
    # book1.add_stock(40)
    # book1.sub_stock(10)
    # book2.print_info()
    # book2.set_price(35.00)
    # book2.add_stock(50)
    # book2.sub_stock(5)
    # book3.print_info()
    # book3.set_price(35.00)
    # book3.add_stock(50)
    # book3.sub_stock(5)

    # 2. 银行账户bankaccount类
    # account1 = BankAccounts("1870001","张三")
    # account2 = BankAccounts("1870002","李四")
    # account2 = BankAccounts("1870003", "宇飞")
    # account1.print_info()
    # account1.add_balance(1500)
    # account1.sub_balance(200)
    # account2.print_info()
    # account2.add_balance(100)
    # account2.sub_balance(200)
    # account3.print_info()
    # account3.add_balance(900)
    # account3.sub_balance(700)

    # 3. 员工Employee类
    # emp1 = Employees(1, "朱棣", "销售", 3500.0, 800.0)
    # emp2 = Employees("2", "李林", "前台", 2900.0)
    # emp1.print_info()
    # emp1.set_position("销售组长")
    # emp1.sum_salary()
    # emp2.print_info()
    # emp2.set_position("人事")
    # emp2.sum_salary()

    # 4. Student类
    stu1 = Students(1, "李华", "男", "九年级", 1)
    stu1.print_info()
    stu1.show_scores()
    stu1.set_score(语文=89.5, 数学=80, 英语=90)
    stu1.show_scores()
    stu1.avg_score()
    stu2 = Students(2, "刘军", "男", "九年级", 1)
    stu3 = Students(3, "李琳", "女", "九年级", 1)
    # 5. Clbum类
    clbum1 = Clbum(1, 1, stu1, stu2, stu3)
    clbum1.print_stus()
    clbum1.find_id(1)
    clbum1.find_name("刘军")