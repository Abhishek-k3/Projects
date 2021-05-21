
#import module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()

# url
driver.get('https://www.jio.com/selfcare/recharge/mobility/')

phoneNo = driver.find_element_by_name("jioNrInputName")
phoneNo.send_keys("8296604013")
phoneNo.send_keys(Keys.RETURN)
driver.get("https://www.stackoverflow.com")

a = driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[10]/div[2]/div[2]/button[2]")
a.click()
