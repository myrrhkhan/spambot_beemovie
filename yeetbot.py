import pyautogui, time, keyboard, cv2
time.sleep(5)
yeet = open("beemovie.txt", "r")
for uh in yeet:
    pyautogui.typewrite(uh)
    pyautogui.press("enter")
    if keyboard.is_pressed('esc'):
        break