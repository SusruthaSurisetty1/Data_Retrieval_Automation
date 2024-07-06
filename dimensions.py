import pyautogui as pt
from time import sleep
def get_position():
    sleep(10)
    print("Actual:", pt.position())
get_position()