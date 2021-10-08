from selenium import webdriver
import time
# 创建浏览器
driver = webdriver.Chrome()

# 网页最大化
driver.maximize_window()

# 打开对应的网址
driver.get(r'D:\use app\pycharm\pythonwork\day14自动化\练习的html\弹框的验证\dialogs.html')
# 点击按钮
# driver.find_element_by_xpath("//*[@id='alert']").click()
driver.find_element_by_xpath("//*[@id = 'confirm']").click()

# 切换到当前弹框,并且接受/取消
time.sleep(3)
# driver.switch_to.alert.accept()  # 确定按钮
driver.switch_to.alert.dismiss() # 取消按钮


# 关闭浏览器
time.sleep(10)
driver.quit()







