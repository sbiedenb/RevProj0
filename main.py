#!/usr/bin/env python3

'''

Authors:
- Steven Biedenbach
- Francis Kato

Abstract:
-Program used to select candidates based on predetermined score matrix.

Usage:
$ main.py [json desired scores] [number of return candidates]
'''

import sys, json

def main(argv):
	weightValues=''
	candidates=int(argv[1])
	#Checking for correct number of input arguments
	if len(argv)!=2:
		print('======ERROR======')
		print('Usage: main.py <json parameters> <num of returns>')
		sys.exit()
	#Try to open the file and load the json data into a dictionary format
	try:
		file=open(argv[0],"r")
		if file.mode == 'r':
			weightValues=json.load(file)
			for k in weightValues:
				weightValues[k]=int(weightValues[k])
	except FileNotFoundError:
		print("File '"+argv[0]+"' not found. Aborting...")

	#Calculate the final weights used to compare individuals
	finalWeights=calcWeight(weightValues)

	#Inserting final weights into the original json dictionary
	i=0
	for n in weightValues:
		weightValues[n]=finalWeights[i]
		i+=1

	#print(weightValues)

	#TEST VALUES
	finalScore={'John':40,'Mary':20,'Sam':80,'Bob':50}

	#Sort the final list of candidates by overall scores
	#returns the desired number of top candidates
	sortedList=sorted(finalScore.items(), key=lambda x: x[1], reverse=True)
	print("Top "+argv[1]+' Candidates:')
	for key in range(0,candidates):
		print(sortedList[key])

#=======================#
#Calculation for determining final category weights
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

#=======================#
if __name__=='__main__':
	main(sys.argv[1:])
