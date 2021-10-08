from selenium import webdriver
import time

# 1、创建浏览器
driver = webdriver.Chrome()

# 2、浏览器最大化
driver.maximize_window()

# 3、打开对应的网址
driver.get(r'D:\use app\pycharm\pythonwork\day14自动化\练习的html\上传文件和下拉列表\autotest.html')

# 4、输入框输入数据
driver.find_element_by_xpath("//*[@id = 'accountID']").send_keys('wly')
driver.find_element_by_xpath("//*[@id = 'passwordID']").send_keys('123456')
driver.find_element_by_xpath("//*[@id = 'areaID']").send_keys("北京市")

time.sleep(3)

driver.find_element_by_xpath("//*[@id = 'sexID1']").click()
driver.find_element_by_xpath("//*[@value = 'spring']").click()
driver.find_element_by_xpath("//*[@value = 'summer']").click()
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r'D:\use app\pycharm\pythonwork\day14自动化\练习的html.7z')
driver.find_element_by_xpath("//*[@id='buttonID']").click()

time.sleep(3)
driver.switch_to.alert.accept()
# 5、关闭浏览器
time.sleep(5)
driver.quit()