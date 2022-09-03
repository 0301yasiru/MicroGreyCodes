from pynput.keyboard import Key, Controller
import win32clipboard
from time import sleep

# Key.print_screen

# get the screenshot
keyboard = Controller()
keyboard.press(Key.print_screen)
keyboard.release(Key.print_screen)

sleep(1)

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

with open("scrshot.png", 'rb') as file_:
    file_.write(data)