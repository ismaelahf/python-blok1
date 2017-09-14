Getal= []
while True:
	try:
		i = int(input("Geef een getal "))
		if i != 0:
			Getal.append(i)
		else:
			break
	except ValueError:
		pass

print()
print(Getal)
print(sum(Getal))
