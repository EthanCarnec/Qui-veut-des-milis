from random import sample

import csv
from random import choices
 
 
with open("question-reponse.csv") as fileName:
    reader = csv.reader(fileName, delimiter=";")
    questions = choices(list(reader), k=21) #21 parce que sino out if range ! attention: A voir suivant les branches
i=0
for i in range (60):# pour afficher 10 questions
    i +=1
    question = questions [i][0]
    ra = questions [i][1]
    rb = questions [i][2]
    rc = questions [i][3]
    print ("")
    print(question)
    print ("")
    print ("REPONSES")
    print (ra, rb, rc)
 
 
fileName.close()

def main():
    print ("*** Début du Quiz ***\n")
nom = input (" Entrez votre nom: ").title()
print ()


def quiz(qs):
    points = 0
    for qu,an in qs.items():
        if input(qu).lower() == an.lower():
            points += 1
            print("Juste.")
        else:
            print("Oups, la bonne réponse est \"{}\".".format(an))
            return points
if __name__ == "__main__":
    main()


def argent(points):
    if points==1 :
        argent = 100
    elif points == 2 :
        argent = 200
    elif points == 3 :
        argent = 300
    elif points == 4 :
        argent = 500
    elif points == 5 :
        argent = 1000
    elif points == 6 :
        argent = 2000
    elif points == 7 :
        argent = 4000
    elif points == 8 :
        argent = 8000
    elif points == 9 :
        argent = 12000
    elif points == 10 :
        argent = 24000
    elif points == 11 :
        argent = 36000
    elif points == 12 :
        argent = 72000
    elif points == 13  :
        argent = 150000
    elif points == 14 :
        argent = 300000
    elif points == 15 :
        argent = 1000000
    return argent
        

