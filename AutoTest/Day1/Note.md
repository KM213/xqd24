自动化测试：使用工具或者编程实现测试工作。解放测试人员的工作，提高测试效率。
* Web自动化测试：python(pyTest) + selenium
* 接口自动化测试

# 1. 自动化模块
* 导入模块：from selenium import webdriver

# 2. 配置驱动
1. 如果使用win11自带Edge浏览器，则不用配置驱动
2. 如果使用chrome浏览器，有两种方法：
   1. 需要配置对应浏览器版本的驱动："D:\DevelopmentTools\Drivers\chromedriver_140.0.7339.207_win64\chromedriver.exe"
   > 导入模块    from selenium.webdriver.chrome.server import Service 
   > 加载驱动    service = Service(r'D:\DevelopmentTools\Drivers\chromedriver_140.0.7339.207_win64\chromedriver.exe')
   > 使用驱动打开浏览器   driver = webdriver.Chrome(service=service)
   2. 将存储驱动的目录添加到系统环境变量path中，则不需要再在代码中配置驱动位置，系统可以自动在环境变量中查找驱动
   > 直接打开浏览器     driver = webdriver.Chrome()

# 3. 打开浏览器
   * 打开浏览器：driver = webdriver.Chrome()
   * 关闭浏览器：driver.quit()

# 4. 元素定位
* 通过某种方式精确找到网页中的特定元素（如按钮、输入框、链接等）。
* 需要导入元素定位方法模块：
    `from selenium.webdriver.common.by import By`
* 定位方法：`driver.find_element(By.XX, "xxxx")`
### 1) id-name 定位
* 通过元素的 id 属性定位：`ele = driver.find_element(By.ID, "id-name")`
### 2) class-name 定位
* 通过元素的 class 属性定位：`ele = driver.find_element(By.CLASS_NAME, "class-name")`
### 3) name属性 定位
* 通过元素的 name 属性定位：`ele = driver.find_element(By.NAME, "name")`
### 4) tag-name 定位
* 通过元素的标签名定位：`ele = driver.find_element(By.TAG_NAME, "tag-name")`
### 5) link-text 定位
* 通过链接的文本内容定位：`ele = driver.find_element(By.LINK_TEXT, "link-text")`
* 完整链接文本定位，精确匹配链接文本，不包含前后空格等。
* 适用于`<a>`标签
### 6) partial link text 定位
* 通过链接的部分文本内容定位：`ele = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")`
### 7) css selector 定位
* 通过 CSS 选择器定位：`ele = driver.find_element(By.CSS_SELECTOR, ".css-selector")`
### 8) xpath 定位
* 通过 XPath 表达式定位元素：`ele = driver.find_element(By.XPATH, "/xpath/xxx")`

# 5. 元素操作
* `.click()`    点击
* `.clear()`    清空输入框
* `.send_keys("xxxx")`    输入值
* `.submit()`    提交表单
* `.get_attribute("属性名")` 获取元素的DOM属性值，例如：`ele.get_dom_attribute('value')`
* `.get_property("属性名")` 获取元素的属性值，例如：`ele.get_property('value')`
* `.tag_name`    获取元素标签名
* `.text`    获取元素文本
* `.is_displayed()`    判断元素是否可见
* `.is_enabled()`    判断元素是否可用
* `.is_selected()`    判断元素是否被选中(如：复选框、单选框)
* `.size`    获取元素大小
* `.location`    获取元素位置
* `.location_once_scrolled_into_view`    滚动到元素可见位置
* `.screenshot()`    截图
* `.get_screenshot_as_file("xxx.png")`    保存截图
* `.get_screenshot_as_png()`    获取截图为PNG格式
* `.get_screenshot_as_base64()`    获取截图为Base64格式


# 6. 浏览器操作
1. 窗口操作：
   * 窗口大小：
     * 最大化窗口：driver.maximize_window()
     * 最小化窗口：driver.minimize_window()
     * 设置窗口大小：driver.set_window_size(1024, 768)  # 设置窗口大小为 1024x768 像素
     * 全屏模式：driver.fullscreen_window()
     * 关闭窗口：driver.quit()
   * 切换窗口：
     * 打开新窗口：driver.execute_script("window.open('https://www.baidu.com/');")  （用JavaScript打开）
     * 切换窗口：driver.switch_to.window(new_window_handle)
     * 
2. 页面操作：
   * 访问网页：driver.get("https://www.baidu.com/")
   * 关闭当前标签页：driver.close()
   * 页面导航：
     * 后退：driver.back()
     * 前进：driver.forward()
     * 刷新：driver.refresh()
   * 获取页面信息：
     * 获取当前URL：driver.current_url
     * 获取页面标题：driver.title
     * 获取所有窗口句柄：driver.window_handles
     * 获取当前窗口句柄：driver.current_window_handle
     * 