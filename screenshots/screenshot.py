import os
import sys
import time
from PIL import Image
from PIL import ImageGrab
#---------------------------------------------------------
#User Settings:
SaveDirectory=r'C:\Users\MinhTrang\Desktop'
#ImageEditorPath=r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\mspaint.exe'
#Here is another example:
#ImageEditorPath=r'C:\Program Files\IrfanView\i_view32.exe'
#---------------------------------------------------------
import webbrowser

webbrowser.open('http://google.com.sg')

time.sleep(5)

def take_image():
	img=ImageGrab.grab()
	saveas=os.path.join(SaveDirectory,'RATES_'+ time.strftime('%d%m%y') + '_' + time.strftime('%I%p').lstrip('0')+'.jpg')
	img.save(saveas)
	return

take_image()