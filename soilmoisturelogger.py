# -*- coding: utf-8 -*-

import serial
import time
import os
import time 
from time import sleep
from datetime import datetime

ser = serial.Serial('/dev/ttyACM2', 9600)

file = open("data_log.csv", "a")

#varl = 'temp'

if os.stat("data_log.csv").st_size == 0:
        file.write("Time,Sensor1\n")
while True:
		varl = ser.readline()
		time.sleep(1)
		varl = varl.decode('utf-8')
		#varl = varl.replace("\r'\n'",'')
		#varl = varl.replace("b'",'')
		now = datetime.now()
		print("Writting Reading - "+str(now))
		file.write(time	.strftime('%l:%M%p on %b %d %Y')+","+str(varl)+","+"\n")
		file.flush()
		time.sleep(60)
		#file.close()
		
