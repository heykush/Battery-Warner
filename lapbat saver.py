import os ,sys
from time import sleep
from plyer import notification
from psutil import sensors_battery

percentage_trigger = 95

def notify():
    notification.notify(
        title='Hey!, Unplug your Charger!',
        message='Your battery is already charged',
        app_name='Gaurav'
        app_icon=None,
        timeout=10,
    )

if __name__ == "__main__":
    while True:
        battery = sensors_battery()
        percent = battery.percent
        power_plugged = battery.power_plugged
        codition=[percent > percentage_trigger and power_plugged]
        if all(codition):
            notify()
    sleep(60*3)
