#! /usr/bin/python

from obspy.core import read
from subprocess import call
import sys, getopt, os

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hio:") 
	except getopt.GetoptError:
		print 'readSeis_ASCII.py [-i <inputfile>] [-o <outputfile>]'
		sys.exit(2)
	date = args[0]
	infile = "*"
	outfile = "data/mseed/" + date + ".mseed"
	for opt, arg in opts:
		if opt == '-h':
			print 'readSeis_ASCII.py [-i <inputfile>] [-o <outputfile>]'
		elif opt in ("-o", "--outfile"):
			outfile = "mseed/" + arg + ".mseed"
		elif opt in ("-i", "--ifile"):
			infile = arg + ".txt"
			outfile = outfile + "-" + arg

	# Creating the MSEED format file to plot
	if not os.path.exists("data/mseed/"):
		os.makedirs("data/mseed/")
	call(["./ascii2mseed -o " + outfile + " data/" + date + "/" + infile], shell=True)

	# Plotting
	data = read(outfile)
	data.plot(type='dayplot')

if __name__ == "__main__":
	main(sys.argv[1:])
