"""
通讯录
"""
import os
import time

def pshow(p, n):
    os.system("cls")
    if not p and not n:
        print("通讯录为空！")
        time.sleep(1)
    else:
        print(" -------------------------------------------------")
        print("|                     联系人列表                    |")
        print(" -------------------------------------------------")
        print(f"| {"编号":^6} | {"姓名":^10} | {"电话号":^20} |")
        print(" -------------------------------------------------")
        for i, p, n in zip(range(0, len(plist)), plist, nlist):
            print(f"| {i+1:^7} | {n:^12} | {p:^22} |")
        print(" -------------------------------------------------")
    flag = input("按任意键返回首页：")
    if flag:
        return


def padd(p, n):
    os.system("cls")
    while True:
        name = input("请输入姓名：")
        phone = input("请输入手机号：")
        if name and len(phone) == 11:
            n.append(name)
            p.append(phone)
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

def pfind(p, n):
    os.system("cls")
    while True:
        name = input("请输入要查找的联系人姓名：")
        if name in n:
            i = n.index(name)
            print(f"{n[i]}的电话号码是：{p[i]}")
        else:
            print(f"联系人【{name}】不存在！")
        flag = input("是否继续查找？(y/n)：")
        if flag == "y":
            continue
        else:
            break

def pedit(p, n):
    os.system("cls")
    while True:
        name = input("请输入要修改的联系人姓名：")
        if name in n:
            i = n.index(name)
            phone = input("请输入修改后电话号码：")
            if len(phone) == 11:
                p[i] = phone
                print(f"修改成功！")
                print(f"姓名：{n[i]}\t电话号：{p[i]}")
        else:
            print(f"联系人【{name}】不存在！")

        flag = input("是否继续修改？(y/n)：")
        if flag == "y":
            continue
        else:
            break


def pdel(p, n):
    os.system("cls")
    while True:
        name = input("请输入要删除的联系人姓名：")
        if name in n:
            i = n.index(name)
            del n[i]
            del p[i]
            print(f"联系人【{name}】删除成功！")
        else:
            print(f"联系人【{name}】不存在！")
        flag = input("是否继续删除？(y/n)：")
        if flag == "y":
            continue
        else:
            break

if __name__ == '__main__':
    plist = ["19019880213"]
    nlist = ["kenny"]
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
            case "1":
                pshow(plist, nlist)
            case "2":
                padd(plist, nlist)
            case "3":
                pfind(plist, nlist)
            case "4":
                pedit(plist, nlist)
            case "5":
                pdel(plist, nlist)
        os.system("cls")