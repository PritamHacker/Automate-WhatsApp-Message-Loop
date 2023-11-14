word = "hello dosto"

import pyautogui # Install pyautogui Library from terminal (pip install pyautogui)
import time # Install time Library from terminal
time.sleep(5)
count = 0

while count <= 10:
	for j in range(1,5):
		for i in range(1, len(word) + 1):
			pyautogui.typewrite(word[:i])
			pyautogui.press("enter")
	count = count+1
