def seizoen(maand):
	if maand in [12, 1, 2]:
		return('winter')
	elif maand in [3, 4, 5]:
		return('lente')
	elif maand in [6, 7, 8]:
		return('zomer')
	elif maand in [9, 10, 11]:
		return('herft')

print(seizoen(2))
print(seizoen(4))
print(seizoen(9))
print(seizoen(12))
