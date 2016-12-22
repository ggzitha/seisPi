Add to crontab:

crontab -e
0 0 * * * /usr/bin/python /home/pi/Desktop/AmySeis/seis.py


Convert to mseed:

ascii2mseed [fileName] -o [outputFileName]


Plot using ObsPy:

from obspy.core import read
data = read('FILENAME', "MSEED")
data.plot()
