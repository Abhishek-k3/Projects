
#import module
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
print("----------------Automatic modile bill payment-------------")
print("--------------------Project By Abhishek.K-----------------")
print("--------------e-mail me at: abhisheku3u@gmail.com---------")
print("-----------------Contact me for publishing----------------")

# url
driver.get('https://www.jio.com/selfcare/recharge/mobility/')

phoneNo = driver.find_element_by_name("jioNrInputName")
phoneNo.send_keys("8296604013")   #Change the number here if needed
phoneNo.send_keys(Keys.RETURN)

a = driver.find_element_by_xpath("//*[@id='__next']/div/div[2]/div[1]/div[2]/div[2]/div[2]/div[10]/div[2]/div[2]/button[2]")
a.click()
driver.close()
#The project is bounded till here as the website is unstable and had a lot of timeout problems
