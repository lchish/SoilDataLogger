# -*- coding: utf-8 -*-

import serial
import time
import os
import time
from time import sleep
from datetime import datetime

port = '/dev/ttyACM2'
timeout = 10

ser = serial.Serial(port, 9600, timeout=timeout)

with open("data_log.csv", "a") as file:
    if os.stat("data_log.csv").st_size == 0:
        file.write("Time\tSensor1\n")

    while True:
        varl = ser.readline().decode('utf-8')
        if len(varl) > 0:
            #varl = varl.replace("\r'\n'",'')
            #varl = varl.replace("b'",'')
            print("Writing Reading - " + str(datetime.now()))
            file.write(time.strftime('%l:%M%p on %b %d %Y') + "\t" + str(varl) + "\n")
        else:
            file.write(time.strftime('%l:%M%p on %b %d %Y') + "\t" + str(timeout) + "second timeout reading from serial " + port + "\n")
