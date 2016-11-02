# -*- coding: utf-8 -*-

import serial
import time
import os
import time
from time import sleep
from datetime import datetime

ser = serial.Serial('/dev/ttyACM2', 9600, timeout=10)

with open("data_log.csv", "a") as file:
    if os.stat("data_log.csv").st_size == 0:
        file.write("Time\tSensor1\n")

    while True:
        varl = ser.readline().decode('utf-8')
        #varl = varl.replace("\r'\n'",'')
        #varl = varl.replace("b'",'')
        print("Writing Reading - " + str(datetime.now()))
        file.write(time.strftime('%l:%M%p on %b %d %Y') + "t" + str(varl) + "\n")
