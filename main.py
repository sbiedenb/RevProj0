#!/usr/bin/env python3

'''

Authors:
- Steven Biedenbach
- Francis Kato
'''

import sys, json

def main(argv):
	weightValues=''
	if len(argv)!=2:
		print('======ERROR======')
		print('Usage: main.py <json parameters> <num of returns>')
		sys.exit()
	try:
		file=open(argv[0],"r")
		if file.mode == 'r':
			weightValues=json.load(file)
	except FileNotFoundError:
		print("File '"+argv[0]+"' not found. Aborting...")

	calcWeight(weightValues)

def calcWeight(weights):
	for k in weights:
		print (weights[k])
	return

if __name__=='__main__':
	main(sys.argv[1:])
