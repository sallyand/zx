from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()#打开浏览器
driver.implicitly_wait(10)
driver.get('http://erp.lemfix.com/')
driver.find_element(By.ID,'username').send_keys('test123')
driver.find_element(By.ID,'password').send_keys('123456')
driver.find_element(By.ID,'btnSubmit').click()
time.sleep(0.5)
uname = driver.find_element(By.XPATH,"//div[@class='pull-left info']//p").text
print(uname)
driver.find_element(By.XPATH,"//span[text()='零售出库']").click()
time.sleep(0.5)
id = driver.find_element(By.XPATH,"//div[text()='零售出库']/..").get_attribute('id')
iframe_id = id + "-frame"
driver.switch_to.frame(iframe_id)#通过iframe进行子页面的切换
driver.find_element(By.ID,"searchNumber").send_keys('028')
driver.find_element(By.XPATH,"//span[text()='查询']").click()
number = driver.find_element(By.XPATH,"//tr[@id='datagrid-row-r1-2-0']").text
if '028' in number:
    print('查询成功')
else:
    print('查询失败')