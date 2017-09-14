file = open('Kaartnummers.txt', 'r')

for line in file:
	card, name = line[:-1].split(', ')
	print('%s heeft kaartnummer %s.' % (name, card))

file.close()
