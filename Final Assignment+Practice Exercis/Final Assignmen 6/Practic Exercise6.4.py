groen = ['Boxtel', 'Best', 'Beukelaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert']
bruin = ['Boxtel', 'Best', 'Beukelaan', 'Eindhoven', 'Helmond Hout', 'Helmont', 'Helmont Brouwhuis', 'Deurne']

def samen(a, b):
	for s in a:
		if s in b:
			print(s)

def verschil(a, b):
	for s in a:
		if s not in b:
			print(s)
	for s in b:
		if s not in a:
			print(s)

samen(groen, bruin)
print()
verschil(groen, bruin)
