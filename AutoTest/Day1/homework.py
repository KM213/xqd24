"""
Day12 10.23
练习：测试然知网站登录及创建员工流程
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

if __name__ == '__main__':
    # 打开浏览器
    driver = webdriver.Edge()
    driver.maximize_window()
    # 访问网页
    driver.get("http://localhost/ranzhi/www")
    time.sleep(2)

# 登录流程
    # 1. 输入账号
    account = driver.find_element(By.ID, "account")
    account.click()
    time.sleep(1)
    account.send_keys("admin")
    time.sleep(1)

    # 2. 输入密码
    passwd = driver.find_element(By.ID, "password")
    passwd.click()
    time.sleep(1)
    passwd.send_keys("123456")
    time.sleep(1)

    # 3. 点击登录按钮
    btn = driver.find_element(By.ID, "submit")
    btn.click()
    time.sleep(2)

# 创建员工流程
    # 1. 点击后台管理
    htbtn = driver.find_element(By.XPATH, '//*[@id="s-menu-superadmin"]/button')
    htbtn.click()
    time.sleep(2)

    # 2. 添加成员
    # 检查是否有iframe
    iframes = driver.find_elements(By.TAG_NAME, "iframe")
    if iframes:
        # 切换到iframe
        driver.switch_to.frame(iframes[0])
        # 然后再定位元素
    # 点击添加成员
    userBtn = driver.find_element(By.CSS_SELECTOR, '#shortcutBox > div > div:nth-child(1) > div > a')
    userBtn.click()
    # time.sleep(2)

    # 3. 写入成员信息
    # 3.1 准备数据
    rint = random.randint(0, 20)
    info = {"username":"test"+str(rint), "realname":"kenny", "pwd":"123456", "email":"test"+str(rint)+"@test.com"}

    username = driver.find_element(By.ID, "account")    # 用户名
    username.send_keys(info["username"])
    time.sleep(1)

    realname = driver.find_element(By.NAME, "realname")   # 真实姓名
    realname.send_keys(info["realname"])
    time.sleep(1)

    genderf = driver.find_element(By.ID, "genderm")      # 性别男
    genderm = driver.find_element(By.ID, "genderf")
    gender = random.choice([genderf, genderm])
    gender.click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="dept"]').click()    # 点击部门下拉框
    time.sleep(1)
    department = driver.find_elements(By.XPATH, '//*[@id="dept"]/option')  # 部门
    depts = random.randint(0, len(department)-1)  # 随机选择一个部门
    department[depts].click()
    time.sleep(1)

    driver.find_element(By.XPATH, '//*/select[@id="role"]').click()  # 点击角色下拉框
    time.sleep(1)
    role_opt = driver.find_elements(By.XPATH, '//*[@id="role"]/option')  # 随机选择一个角色
    roles = random.randint(0, len(role_opt)-1)      # 随机选择一个角色
    role_opt[roles].click()
    time.sleep(1)

    pwd = driver.find_element(By.ID, "password1")   # 密码
    pwd.send_keys(info['pwd'])
    time.sleep(1)

    pwd2 = driver.find_element(By.ID, "password2")  # 确认密码
    pwd2.send_keys(info['pwd'])
    time.sleep(1)

    email = driver.find_element(By.NAME, "email")   # 邮箱
    email.send_keys(info['email'])
    time.sleep(1)

    # 4. 点击保存
    saveBtn = driver.find_element(By.ID, "submit")  # 保存
    saveBtn.click()
    time.sleep(5)

# 签退
    driver.switch_to.default_content()
    driver.find_element(By.PARTIAL_LINK_TEXT, "签退").click()
    time.sleep(3)

# 关闭浏览器
    driver.close()