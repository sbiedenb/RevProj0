'''
    Driver of the program
'''

#!usr/env/bin python3


import sys
import json
import pandas 
import numpy as np



'''
    Main
'''
def main(argv):
    
    #Validate the command line input

    if len(sys.argv) < 2:
        print("Incorrect number of input!!!!")
        print("./<executable> <filename1> filename<2>")
        exit()

    else:
        persons = readGradesFromFile(sys.argv[1])
        conversion = convertData(persons)
        pairwise(conversion)

        '''
        organizedData = organizeData(persons)
        conversionTable = convertData(organizedData)
        pairWise(conversionTable)

        
        score1 = pairWiseSubtraction(7,2)
        score2 = pairWiseSubtraction(1,3)
        score3 = pairWiseSubtraction(5, 4)
        score4 = pairWiseSubtraction(9, 3)
        print(score1)
        print(score2)
        print(score3)
        print(score4)

        '''
        
        print("")
'''
    Collect People's information; names and skill grades
'''

def readGradesFromFile(fileName):

    persons = {}

    with open(fileName) as f:
        persons = json.load(f)

    return persons


'''
    Convert the data into conversion table, that means the percentage scores
    now have specified values based on range they are in.

'''

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
    

 
def pairWise(people):

    
    for person, skills in people.items():


        for technology





























                            
                                


if __name__ == "__main__":
    main(sys.argv[1:])




























































