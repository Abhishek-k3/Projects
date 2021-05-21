from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime


now = datetime.now()
current_time = now.strftime("%H:%M:%S")

sent = 0

ch = int(input("Enter the choice 1:Send Now\t 2:Schedule the Message"))
contact = input("Enter the contact name")
text = input("Enter the meassage You want to send to "+contact+".")
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

if ch == 2:

    user_time = input("enter time in H:M:S format at which you want this message to be sent")
    print("-------PLEASE KEEP THIS PROGRAM RUNNING IN ORDED TO SEND THE MESSAGE AT DESIRED TIME--------")





inp_xpath_search = "//*[@id='side']/div[1]/div/label/div/div[2]"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()
inp_xpath = "//*[@id='main']/footer/div[1]/div[2]/div/div[2]"
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)
if ch == 2:
    while sent!=1:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        if current_time == user_time:
            input_box.send_keys(text + Keys.ENTER)
            sent = 1
else:
    input_box.send_keys(text + Keys.ENTER)
    sent = 1




time.sleep(2)
    #driver.quit()
