import pyautogui

#Move mouse to upper-left screen just in case something goes wrong. 
pyautogui.FAILSAFE = True

#Enter extention
pyautogui.typewrite('2772')
pyautogui.press('enter')