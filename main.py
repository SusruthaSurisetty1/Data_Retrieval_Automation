from datetime import datetime, timedelta
from time import sleep
import pyautogui as pt
def sleep_till_download_time():
    temp = datetime.now()
    rem = temp.minute % 6
    print("rem", (6- rem))
    sleep((6- rem) * 60)
def downloader():
    print("Downloader Started At:", datetime.now())
    sleep(1)
    x_refresh, y_refresh = 98, 61
    pt.click(x_refresh, y_refresh, clicks=6, duration=0.5)
    sleep(30)
    x_pokeball, y_pokeball = 1183,67
    pt.click(x_pokeball, y_pokeball, clicks=1, duration=0.5)
    sleep(3)
    x_download_button, y_download_button = 847, 125
    pt.click(x_download_button, y_download_button, clicks=1, duration=0.5)
    sleep(3)
    x_close_extension, y_close_extension = 1137, 34
    pt.click(x_close_extension, y_close_extension, clicks=1, duration=0.5)
today_datetime = datetime.now()
start_time = datetime(year=today_datetime.year, month=today_datetime.month, day=today_datetime.day, hour=20, minute=4)
current_time_1 = start_time
end_time = start_time + timedelta(hours=999)
print("First Print\nShift Start Time", str(start_time))
print("Shift End Time", end_time, '\n')
i = 0
while start_time <= end_time:
    temp_current = datetime.now()
    if temp_current < current_time_1:
        diff = (current_time_1 - temp_current)
        diff += datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        print(f"Shift Starts In {diff.hour} Hours {diff.minute} Minutes {diff.second} Seconds")
        sleep((diff.hour * 3600) + (diff.minute * 60) +(diff.second))
    print("i", i)
    i += 1
    sleep_till_download_time()
    downloader()
    start_time = datetime.now()
    print("Download End Time:", start_time)
    print()


