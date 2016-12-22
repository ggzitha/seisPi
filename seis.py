import time
import datetime
import Adafruit_ADS1x15

# ADC instance members
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 8
MULTIPLIER = 0.015625;

# Seismograph members
sourceName = "AmySeis"
samplesPerSecond = 20
samplesPerFile = 86400 / 24 * samplesPerSecond
timeStamp = datetime.datetime.now().isoformat()
format = "SLIST"
type = "FLOAT"
units = "COUNT"

fileName = sourceName + "_" + timeStamp

# Open file to output to
file = open(fileName + ".txt", "w+")
file.write("TIMESERIES _Amy__Z_, %s samples, %s sps, %s, %s, %s, %s\n" % (samplesPerFile, samplesPerSecond, timeStamp, format, type, units))
file.close()

for i in range(0, samplesPerFile / 6): # one day 288000
	file = open(fileName + ".txt", "a+")

	for j in range(0, 6):
		value = adc.read_adc_difference(0, gain=GAIN)
		file.write("\t" + '{0}'.format(value))
		time.sleep(0.05)

	file.write("\n")
	file.close()
