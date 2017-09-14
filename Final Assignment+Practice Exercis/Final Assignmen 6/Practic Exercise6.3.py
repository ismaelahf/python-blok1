def namen():
	names = {}

	while True:
		name = input('Hoe heet je: ')
		if name == '':
			return(names)
		else:
			if name in names:
				names[name] += 1
			else:
				names[name] = 1

names = namen()
print()

for value in names:
	print('Number of students with the name %s in the class: %s' % (value, names[value]))
