import pyautogui as pg
import time

msg = input('Enter you message(separate by comma): ').split(',')
time.sleep(5)
while True:
	for x in msg: 
 		 pg.write(x, interval=0.1)
 		 pg.press('enter')
