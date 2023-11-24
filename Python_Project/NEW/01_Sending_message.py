import pyautogui
import time
message=5
while message>0:
    time.sleep(4)
    pyautogui.typewrite("Whatsapp bro  I am sending the message by using the python ")
    time.sleep(4)
    pyautogui.press('enter')
    message=message-1



