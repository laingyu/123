from selenium import webdriver
import time

# 创建浏览器
chrome = webdriver.Chrome()

# 浏览器最大化
chrome.maximize_window()

# 打开浏览器
chrome.get('http://www.jd.com')

# 搜索栏输入
chrome.find_element_by_xpath("//*[@id = 'key']").send_keys("外星人")

# 点击搜索按钮
chrome.find_element_by_xpath("//button[@clstag = 'h|keycount|head|search_a']").click()
# 强行挺10s，等待网页刷新，稳定定位
time.sleep(10)
chrome.find_element_by_xpath("/html/body/div[5]/div[3]/div/div[1]/div/div[3]/ul/li[1]/div/div[3]/a/em").click()

# 关闭浏览器
time.sleep(10)
chrome.quit()



















