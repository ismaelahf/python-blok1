leeftijd = eval(input('Geef je leeftijd: '))
paspoort = (input('Nederlands paspoort: '))
if (leeftijd >= 18 ) and (paspoort == 'ja' or 'Ja'):
   print("Gefeliciteerd, je mag stemmen!")
else:
   print("Helaas, je mag niet stemmen!")
