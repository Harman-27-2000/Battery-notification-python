#This is a program to write the bettery percentage in the laptop/device.

"""Here psutil (process and system utilities) library it is used to retrive information about system 
    plyer is another module which is used. it can access the featires of the hardware.
    """

import psutil
from plyer import notification
import time

while(True):
    battery = psutil.sensors_battery() #to get battery percentage of device
    percent = battery.percent #battrey percentage will be stored in percent variable
     
    notification.notify(title="Battery Percentage",message=str(percent)+"% Battery remaining",timeout=10)
    # to diplay the notification box we used notification library which will write the battery percentage of device
    time.sleep(60*60)
    continue
