import pyautogui

pyautogui.FAILSAFE = True

# Grab the UDT window and move to an optimal location and resize the window
UDTWindow = pyautogui.getWindow('ESS Analyst Desktop')
UDTWindow.minimize()
UDTWindow.restore()
UDTWindow.resize(600,410)
UDTWindow.move(x=600, y=300)

# Move to phone(723,706)
pyautogui.click(x=700, y=690, button='left')

# Move to email (1000,706)
pyautogui.click(x=1000, y=690, button='left')

# Move to chat (1050,706)
pyautogui.click(x=1050, y=690, button='left')