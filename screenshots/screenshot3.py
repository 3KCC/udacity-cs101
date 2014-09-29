from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os
import sys
import time
from PIL import ImageGrab

fox = webdriver.Firefox()
fox.get('http://www.ezfx.com.sg/')

# now that we have the preliminary stuff out of the way time to get that image :D
fox.maximize_window()
def scroll_element_into_view(driver, element):
    """Scroll element into view"""
    y = element.location['y']
    driver.execute_script('window.scrollTo(0, {0})'.format(y))

def take_image():
	img=ImageGrab.grab()
	saveas=os.path.join(SaveDirectory,'RATES_'+ time.strftime('%d%m%y') + '_' + time.strftime('%I%p').lstrip('0')+'.jpg')
	img.save(saveas)
	return

try:
    element = WebDriverWait(fox, 10).until(
        EC.presence_of_element_located((By.ID, "change"))
    )
    
finally:
	element = fox.find_element_by_id('change') # find part of the page you want image of
	scroll_element_into_view(fox, element)
	#time.sleep(2)
	SaveDirectory=r'C:\Users\MinhTrang\Desktop'
	take_image()



