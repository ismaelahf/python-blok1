def kwadraten_som(grondgetallen):
	r = 0
	for i in grondgetallen:
		if i > 0:
			r += i**2
	return(r)

print(kwadraten_som([4, 5, 3, -81]))
print(kwadraten_som([-7, -3, 1, 1]))
