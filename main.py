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
			for k in weightValues:
				weightValues[k]=int(weightValues[k])
	except FileNotFoundError:
		print("File '"+argv[0]+"' not found. Aborting...")

	finalWeights=calcWeight(weightValues)

	i=0
	for n in weightValues:
		weightValues[n]=finalWeights[i]
		i+=1

	print(weightValues)

def calcWeight(weights):
	rows=[0 for _ in range(len(weights))]
	collumn=[]
	for k in weights:
		total=0
		collumn.clear()
		for x in weights:
			if (weights[x]-weights[k])>0:
				collumn.append((weights[x]-weights[k])+1)
				total+=(weights[x]-weights[k])+1
			else:
				collumn.append(1/((weights[k]-weights[x])+1))
				total+=1/((weights[k]-weights[x])+1)
		for i in range(0,len(collumn)):
			collumn[i]=collumn[i]/total
			rows[i]+=collumn[i]
	for n in range(0,len(rows)):
		rows[n]=round(rows[n]/len(rows),2)
	return rows

if __name__=='__main__':
	main(sys.argv[1:])
