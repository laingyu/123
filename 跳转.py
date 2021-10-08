from selenium import webdriver
import time
# 1、创建
driver = webdriver.Chrome()

# 2、最大化
driver.maximize_window()

# 3、打开对应的网址
driver.get(r"D:\use app\pycharm\pythonwork\day14自动化\练习的html\跳转页面\pop.html")

# 4、点击
driver.find_element_by_xpath("//*[@id='goo']").click()

# 5、关闭
time.sleep(10)
driver.quit()






