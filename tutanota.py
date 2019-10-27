
#Akash Sarkars

from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
import os
import random
url='https://mail.tutanota.com/login?noAutoLogin=true'

def driver(username,password):
    driver=webdriver.Firefox()
    driver.get(url)
    driver.find_element_by_xpath("//div[@class='flex items-center']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='button-content flex items-center secondary plr-button justify-center']").click()
    time.sleep(1.5)
    driver.find_element_by_xpath("//div[@class='button-min-height']").click()
    time.sleep(1.5)
    driver.find_element_by_xpath("//div[@class='button-content flex items-center primary plr-button justify-center']").click()
    time.sleep(1.5)
    driver.find_element_by_xpath("//input[@style='min-width: 20px; line-height: 24px; opacity: 1;']").send_keys(username)
    time.sleep(1.6)
    driver.find_element_by_xpath("//input[@autocomplete='off']").send_keys(password)
    time.sleep(1.66)
    x=driver.find_element_by_xpath("//*[@autocomplete=''][@class='input']")
    x.send_keys(password)
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='I have read and agree to the following documents:']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[text()='I am at least 16 years old.']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='button-content flex items-center login plr-button justify-center']").click()

def write_email(file):
    with open(file, "w") as writer:
        for i in range (0,len(usernames)):
            writer.write(usernames[i]+"@tutanota.com"+"\n")

usernames=[]
def user_generate(user,number,name):
    for i in range(0,user):
        x=random.randint(0,200)
        number=number+x;
        usernames.append(name+str(number))
        
def driver_main(name,file,user,number,password):
    user_generate(user,number,name)
    for i in range(0,len(usernames)):
        try:
            driver(usernames[i],password)
        except Exception:
            pass
    write_email(file)
name=input("Give the Name for Username= ")
file=input("Give the file name in .txt = ")
user=int(input("Number of users account to be created = "))
number=int(input("Give a unique no. min 4 digit= "))
password=input("Give the password(would be same for all email address)= ")
print("Processing.............................................")
print(name,file,user,number,password)
driver_main(name,file,user,number,password)
    

