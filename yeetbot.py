import pyautogui, time
time.sleep(10)
yeet = open("beemovie.txt", "r")
for uh in yeet:
    pyautogui.typewrite(uh)
    pyautogui.press("enter")