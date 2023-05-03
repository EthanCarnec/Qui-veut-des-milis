import csv
with open("question-reponse.csv") as fileName:
    reader = csv.reader(fileName, delimiter=";")
    questions = choices(list(reader), k=21) #21 parce que sino out if range ! attention: A voir suivant les branches
