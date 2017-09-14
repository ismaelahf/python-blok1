import datetime
import csv



bestand = open('./inloggers.csv', 'a')
writer = csv.writer(bestand, delimiter = ';', quotechar = '|', quoting = csv.QUOTE_MINIMAL)

while True:
	naam = input('Wat is je achternaam? ')
	if naam == 'einde':
		break
	voorletters = input('Wat zijn je voorletters? ')
	geboortebdatum = input('Wat is je geboortedatum? ')
	email = input('Wat is je e-mail adres? ')

	writer.writerow([datetime.datetime.today().strftime('%a %d %b %Y at %H:%M'), naam, voorletters, geboortebdatum, email])

