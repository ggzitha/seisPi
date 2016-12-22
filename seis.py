#! /usr/bin/python

import time
import datetime
import os
import Adafruit_ADS1x15

# ADC instance members
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 8
MULTIPLIER = 0.015625;

# Seismograph members
sourceName = "AmySeis"
samplesPerSecond = 20
samplesPerFile = 3600 * samplesPerSecond
format = "SLIST"
type = "INTEGER"
units = "COUNT"

# Directory organization
dir = "/home/pi/Desktop/AmySeis/data/"
dir = dir + datetime.datetime.now().strftime('%Y-%m-%d') + "/"
if not os.path.exists(dir):
	os.makedirs(dir)
fileName = dir + sourceName + "_" + datetime.datetime.now().strftime('%H')

# Open file to output to
file = open(fileName + ".txt", "w+")
file.write("TIMESERIES _AMY__BHZ_, %s samples, %s sps, %s, %s, %s, %s\n" % (samplesPerFile, samplesPerSecond, datetime.datetime.now().isoformat(), format, type, units))
file.close()

for i in range(0, samplesPerFile / 6): # one day 288000
	file = open(fileName + ".txt", "a+")

	for j in range(0, 6):
		prevTime = time.time()
		value = adc.read_adc_difference(0, gain=GAIN)
		file.write("\t" + '{0}'.format(value))
		while((time.time() - prevTime) < 0.05):
			pass

	file.write("\n")
	file.close()
