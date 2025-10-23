"""
Day12 10.23
web自动化测试
"""

import time
# 导入selenium模块的页面驱动
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 元素操作
def fun1():
    # 打开浏览器
    driver = webdriver.Chrome()
    # 访问网页
    driver.get("https://www.baidu.com/")
    # 定位元素
    # id 定位
    input = driver.find_element(By.ID, "chat-textarea")
    # 获取属性
    attr1 = input.get_attribute("placeholder")
    print(attr1)
    # 判断元素是否可见
    print(input.is_displayed())
    # 判断元素是否被选中
    print(input.is_selected())
    input.click()
    time.sleep(2)
    print(input.is_selected())
    # 获取元素大小
    print(input.size)
    # 获取元素位置
    print(input.location)
    # 输入文字
    input.send_keys("python")

    time.sleep(2)
    sbutten = driver.find_element(By.TAG_NAME, "button")
    # 获取文字
    print(sbutten.text)
    text = sbutten.text
    print(text)
    # 点击元素
    sbutten.click()
    time.sleep(2)
    # 关闭浏览器
    driver.quit()

# 浏览器操作
def fun2():
    driver = webdriver.Edge()
    driver.get("https://www.baidu.com")
    # 最大化窗口
    driver.maximize_window()
    # 最小化窗口
    # driver.minimize_window()
    time.sleep(1)
    ele = driver.find_element(By.TAG_NAME, "button")
    ele.click()
    time.sleep(1)
    # 页面后退，返回上一个页面
    driver.back()
    time.sleep(1)
    # 页面前进，进入下一个页面
    driver.forward()
    time.sleep(1)
    # 刷新页面
    driver.refresh()
    time.sleep(1)
    # 获取当前网页标题
    print(driver.title)
    # 获取当前网页地址
    print(driver.current_url)
    time.sleep(1)
    # 获取所有窗口句柄
    print(driver.window_handles)
    # 获取当前页面句柄
    print(driver.current_window_handle)
    # 截图
    driver.get_screenshot_as_file("./aaa.png")
    sh_png = driver.get_screenshot_as_png()
    print(len(sh_png), type(sh_png))
    sh_base64 = driver.get_screenshot_as_base64()
    print(len(sh_base64), type(sh_base64))
    time.sleep(5)
    driver.close()

if __name__ == '__main__':
    # id 定位
    fun2()
