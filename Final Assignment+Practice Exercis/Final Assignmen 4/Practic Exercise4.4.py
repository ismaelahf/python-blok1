file = open('Kaartnummers.txt', 'r')

count = 0
card = [0, 0]
for line in file:
	count += 1
	cardline, _ = line.split(', ')
	if int(cardline) > card[0]:
		card = [int(cardline), count]

file.close()

print('This file has %d lines.\nTHet grootste kaartnummer is: %d en dat staat op regel %d.' % (count, card[0], card[1]))

#Het grootste kaartnummer is: 645345 en dat staat op regel 4
