#!/usr/bin/env python3

'''

Authors:
- Steven Biedenbach
- Francis Kato

Abstract:
-Program used to select candidates based on predetermined score matrix.

Usage:
$ main.py [json desired scores] [number of return candidates] [json grades]
-Desired objectives must be in correct Json format eg.({"Java":"9","Angular":"4","SOAP":"2"})
-Positive integers only (Negative integers will be converted to positive)
-Desired amount of candidates should be less than or equal to the amount of total candidates
-Output format: ('[Candidate]')
-Output is in descending order
'''

import sys, json

def main(argv):
	weightValues=''
	
	#Checking for correct number of input arguments
	if len(argv)!=3:
		print('======ERROR======')
		print('Usage: main.py <JSON parameters> <num of returns> <JSON Grades>')
		sys.exit()

	try:
		candidates=abs(int(argv[1]))
	except ValueError:
		print('======ERROR======')
		print('Usage: main.py <JSON parameters> <num of returns> <JSON Grades>')
		sys.exit()

	#Try to open the file and load the json data into a dictionary format
	try:
		file=open(argv[0],"r")
		if file.mode == 'r':
			try:
				weightValues=json.load(file)
			except UnicodeDecodeError:
				print('======ERROR======')
				print('File not in JSON format.')
				sys.exit()
			for k in weightValues:
				weightValues[k]=abs(int(weightValues[k]))
	except (FileNotFoundError, ValueError):
		print('======ERROR======')
		print("File '"+argv[0]+"' not found or incorrect format. Aborting...")
		sys.exit()

	#Calculate the final weights used to compare individuals
	#print(weightValues)
	finalWeights=calcWeight(weightValues)

	#Inserting final weights into the original json dictionary
	i=0
	for n in weightValues:
		weightValues[n]=finalWeights[i]
		i+=1

	#print(weightValues)

	persons = readGradesFromFile(argv[2])
	conversion = convertData(persons)
	#print(conversion)

	#TEST VALUES
	#{'John':40,'Mary':20,'Sam':80,'Bob':50}
	finalScore=candidateScores(weightValues,conversion)
	#print(finalScore)
	
	# Sort the final list of candidates by overall scores
	# returns the desired number of top candidates
	sortedList=sorted(finalScore.items(), key=lambda x: x[1], reverse=True)
	print("Top "+str(abs(int(argv[1])))+' Candidates:')
	if int(argv[1])==0:print('-Nobody is Worthy!')
	try:
		for key in range(0,candidates):
			print((sortedList[key])[0])
	except IndexError:
		print('======ERROR======')
		print('End of Candidates List')
		sys.exit()

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
def readGradesFromFile(fileName):

    persons = {}

    with open(fileName) as f:
        persons = json.load(f)

    return persons

#=======================#
def convertData(people):

    for person, skills in people.items():

        for technology, score in skills.items():
                
            if score >= 95:
                skills[technology] = 8
            elif score < 95 and score >= 90:
                skills[technology] = 7
            elif score < 90 and score >= 85:
                skills[technology] = 6
            elif score < 85 and score >= 80:                     
                skills[technology] = 5
            elif score < 80 and score >= 75:                     
                skills[technology] = 4
            elif score < 75 and score >= 70:                     
                skills[technology] = 3
            elif score < 70 and score >= 65:
                skills[technology] = 2
            elif score < 65 and score >= 60:
                skills[technology] = 1
            else:
                skills[technology] = 0

    return people 

#=======================#
def candidateScores(catWeights, personWeights):
	finalWeight=[]
	tempWeight = {}
	dictionary = {}
	for p in personWeights:
		dictionary[p]=0

	for tech, weight in catWeights.items():
		for person, skills in personWeights.items():
			if tech in skills:
				tempWeight[person]=skills[tech]		
			else:
				tempWeight[person]=0
		finalWeight=calcWeight(tempWeight)
		i=0
		for person in tempWeight:
			dictionary[person]+=finalWeight[i]*weight
			i+=1
	return dictionary

#=======================#
if __name__=='__main__':
	main(sys.argv[1:])
