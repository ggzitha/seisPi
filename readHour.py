#! /usr/bin/python

from obspy.core import read
from subprocess import call
import sys, getopt, os

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "h:io") 
	except getopt.GetoptError:
		print 'readSeis_ASCII.py [-i <inputfile>] [-o <outputfile>]'
		sys.exit(2)
	date = args[0]
	outfile = "data/mseed/" + date + ".mseed"
	for opt, arg in opts:
		if opt == '-h':
			print 'readSeis_ASCII.py [-i <inputfile>] [-o <outputfile>]'
		elif opt in ("-i", "--ifile"):
			infile = "data/" + arg + ".txt"
			outfile = outfile + "-" + arg

	# Plotting
	data = read(infile)
	data.plot()

if __name__ == "__main__":
	main(sys.argv[1:])
