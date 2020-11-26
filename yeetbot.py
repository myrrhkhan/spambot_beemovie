import pyautogui, time, keyboard
while True:
    try: 
        headstart = int(input("enter how many seconds you need to get on your app? "))
        messagedelay = int(input("enter delay between messages, in seconds: "))
        print("you have %s seconds" %headstart)
        time.sleep(headstart)
    except: continue
    else: break
yeet = open("beemovie.txt", "r")
for uh in yeet:
    pyautogui.typewrite(uh)
    pyautogui.press("enter")
    time.sleep(messagedelay)
    if keyboard.is_pressed('esc'):
        break