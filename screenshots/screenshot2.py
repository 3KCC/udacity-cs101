from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import os
import sys
import time
from PIL import Image
from PIL import ImageGrab

baseurl = "https://login.yahoo.com/config/login_verify2?&.src=ym&.intl=us"
username = "kisskindkid"
password = "nhancuu"

xpaths = { 'usernameTxtBox' : ".//*[@id='username']",
           'passwordTxtBox' : ".//*[@id='passwd']",
           'submitButton' :   ".//*[@id='.save']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()

#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)

#Clear Password TextBox if already allowed "Remember Me" 
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()

#Write Password in password TextBox
mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

time.sleep(5)

SaveDirectory=r'C:\Users\MinhTrang\Desktop'

def take_image():
	img=ImageGrab.grab()
	saveas=os.path.join(SaveDirectory,'RATES_'+ time.strftime('%d%m%y') + '_' + time.strftime('%I%p').lstrip('0')+'.jpg')
	img.save(saveas)
	return

take_image()