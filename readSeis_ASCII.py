#! /usr/bin/python

from obspy.core import read
from subprocess import call
import sys, getopt, os, obspy

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hs", ["hour=", "scale="]) 
	except getopt.GetoptError:
		print 'readSeis_ASCII.py [-o <outputfile>] [--hour=<HH>] <YYYY-MM-DD>'
		sys.exit(2)
	date = args[0]
	scale = 500
	infile = "*"
	outfile = "data/mseed/" + date + ".mseed"
	for opt, arg in opts:
		if opt == '-h':
			print 'readSeis_ASCII.py [-o <outputfile>] [--hour=<HH>] <YYYY-MM-DD>'
		elif opt in ("-o", "--outfile"):
			outfile = "data/mseed/" + arg + ".mseed"
		elif opt in ("-s", "--scale"):
			scale = int(arg)
		elif opt in ("--hour"):
			infile = arg + ".txt"
			data = read(("data/" + date + "/" + infile))
			data.filter('lowpass', freq=1.0, corners=4, zerophase=True)
			data.plot()
			sys.exit()

	# Creating the MSEED format file to plot
	if not os.path.exists("data/mseed/"):
		os.makedirs("data/mseed/")
	call(["./ascii2mseed -o " + outfile + " data/" + date + "/" + infile], shell=True)

	# Plotting
	data = read(outfile)
	data.filter('lowpass', freq=1.0, corners=4, zerophase=True)
	data.plot(type='dayplot', vertical_scaling_range= scale)

if __name__ == "__main__":
	main(sys.argv[1:])
