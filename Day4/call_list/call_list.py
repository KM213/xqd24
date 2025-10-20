"""
通讯录：文件存储
    存储：./list.txt
    格式：
        姓名1,电话1    如：kenny,19019880213
"""
import os
import time

# 展示通讯录列表
def show_list(faddr):
    f = open(faddr, 'r', encoding="utf-8")
    lines = f.readlines()
    print(" -------------------------------------------------")
    print("|                      通讯录                      |")
    print(" -------------------------------------------------")
    if not lines:
        print("通讯录为空，即将返回首页...")
        time.sleep(0.5)
        return
    else:
        print(f"| {"编号":^6} | {"姓名":^10} | {"电话号":^20} |")
        print(" -------------------------------------------------")
        for i, line in zip(range(1, len(lines)+1), lines):
            kw = list(line.split(','))
            # print(kw)
            print(f"| {i:^7} | {kw[0]:^12} | {kw[1].strip('\n'):^22} |")
        print(" -------------------------------------------------")
        flag = input("按任意键返回首页：")
        if flag:
            f.close()
            return
        pass

# 添加联系人
def add_list(faddr):
    f = open(faddr, 'a+', encoding="utf-8")
    while True:
        name = input("请输入姓名：")
        phone = input("请输入手机号：")
        if name and len(phone) == 11:
            # f.writelines(f"{name},{phone}\n")
            f.write(f"{name},{phone}\n")
            print("添加成功！")
        else:
            print("输入错误，请检查：")
            print(f"输入的姓名：{name}")
            print(f"输入的电话号：{phone}")
        flag = input("是否继续添加？(y/n)：")
        if flag == "y":
            continue
        else:
            break
    f.close()
    return

# 查找联系人
def search_list(faddr):
    f = open(faddr, 'r', encoding="utf-8")
    while True:
        word = input("请输入要搜索的内容（姓名or号码）：")
        flag = 0
        for num, line in enumerate(f, 1):
            # print(line)
            kw = line.strip('\n').split(',')
            # print(kw, type(kw))
            if word in kw:
                print(f"姓名：{kw[0]}\n电话号码：{kw[1].strip('\n')}")
                flag = 1
            else:
                pass
        if flag == 0:
            print(f"未找到此信息【{word}】！")
        flag = input("是否继续查找？(y/n)：")
        if flag == "y":
            f.seek(0)
            continue
        else:
            f.close()
            break
    return


if __name__ == '__main__':
    file_addr = "./list.txt"
    while 1:
        print(" ------------------------------------------------- ")
        print("|                      通讯录                      |")
        print(" ------------------------------------------------- ")
        print(f"|\t{"1. 查看通讯录列表":<41}|")
        print(f"|\t{"2. 添加联系人信息":<41}|")
        print(f"|\t{"3. 查找联系人信息":<41}|")
        print(f"|\t{"4. 修改联系人信息":<41}|")
        print(f"|\t{"5. 删除联系人信息":<41}|")
        print(f"|\t{"0. 退出通讯录":<42}|")
        print(" ------------------------------------------------- ")
        op = input("输入选项(0-5)：")
        match op:
            case "0":
                print("退出通讯录...")
                time.sleep(0.5)
                break
                pass
            case "1":
                show_list(file_addr)
                pass
            case "2":
                add_list(file_addr)
                pass
            case "3":
                search_list(file_addr)
                pass
            case "4":
                pass
            case "5":
                pass
        os.system("cls")