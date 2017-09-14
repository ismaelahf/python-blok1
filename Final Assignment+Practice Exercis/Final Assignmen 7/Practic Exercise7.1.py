groep = int()
while groep == 0:
	try:
		groep = int(input('Met hoeveel personen zijn jullie '))
		if groep == 0:
			print('Delen door nul kan niet! ')
			groep = int()
		elif groep < 0:
			print('Negatieve getallen zijn niet toegestaan! ')
			groep= int()
	except ValueError:
		print('Onjuiste invoer! ')
		pass

print(4356 / groep)
