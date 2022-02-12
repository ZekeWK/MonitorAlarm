import win32gui, win32con
import pyautogui
import time
import datetime

SC_MONITORPOWER = 0xF170
SETUP_DELAY = 30
LAG_DELAY = 5



def main():
    delay = input_delay()

    output_time(delay)

    time.sleep(SETUP_DELAY)

    power_off()

    time.sleep(delay)
    
    power_on()

    time.sleep(LAG_DELAY)

    start_video()
  


def input_delay():
    print("How long should the monitor be off? (Hours Minutes Seconds)")
    delay_ints = map(int, input("").strip().split())

    multipliers = [3600, 60, 1]
    delay = sum(map(lambda x : x[0]*x[1], zip(delay_ints, multipliers)))
    return delay

    
    
def output_time(delay):
    total_delay = delay + SETUP_DELAY + LAG_DELAY

    now = datetime.datetime.now()
    start_time = now + datetime.timedelta(seconds=total_delay)

    print("The monitor will be on at:")
    print(start_time)



def power_off(): #Curtesy off x011 on github
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, 2) # Off



def power_on(): #Curtesy off x011 on github
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SYSCOMMAND, SC_MONITORPOWER, -1) # On



def start_video():
    pyautogui.press("space")



if __name__ == "__main__":
    main()