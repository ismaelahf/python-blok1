import csv

file = open('score.csv', 'r')
reader = csv.reader(file, delimiter = ';', quotechar = '|')

Top= int()
for l in list(reader):
	score = int(l[2])
	if score > Top:
		hscore = score
		naam = l[0]

print('De hoogste score is:',hscore," behaald door", naam )

file.close()
