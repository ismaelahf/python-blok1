import random

def monopoly():
	a = 6
	b = 6
	c = 1

	while a + b == 12:
		a = random.randrange(1,7)
		b = random.randrange(1,7)

		print(a, b, end='')

		if c == 2:
			print (' dubbel', end='')
		elif c == 3:
			print (' de speler moet naar de gevangenis! ')
			break

		print()
		c += 1

monopoly()
