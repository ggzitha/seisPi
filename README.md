install obsPy:

add to /etc/apt/sources.list
deb http://deb.obspy.org jessie main
get the key
wget --quiet -O - https://raw.github.com/obspy/obspy/master/misc/debian/public.key | sudo apt-key add -
install the program
sudo apt-get install python-obspy python3-obspy

enable i2c:

sudo apt-get install python-smbus i2c-tools

add to /etc/modules
i2c-bcm2708
i2c-dev

add to /boot/config.txt
dtparam=i2c_arm=on


install ADS1x15:

sudo pip install adafruit-ads1x15


Add to crontab:

crontab -e
0 0 * * * /usr/bin/python /home/pi/Desktop/AmySeis/seis.py


Convert to mseed:

ascii2mseed [fileName] -o [outputFileName]


Plot using ObsPy:

from obspy.core import read
data = read('FILENAME', "MSEED")
data.plot()
