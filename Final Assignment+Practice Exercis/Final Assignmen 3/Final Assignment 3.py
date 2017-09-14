standaardtarief = 0.80
age = eval(input("wat is uw leeftijd: "))
weekend = eval(input("type: True/False voor weekendrit: "))
afstand = eval(input('wat is de afstand:  '))

def standaardprijs(afstandKM):
   if afstandKM <0:
       prijs = 0
   elif afstandKM > 50:
       prijs = afstandKM * 0.80 + 15

   else:
      prijs = afstandKM * 0.80

   return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
   totaalprijs = standaardprijs(afstandKM)


   if leeftijd <12 or leeftijd >= 65:
       if weekendrit:
           totaalprijs =  totaalprijs * 0.65
       else:
           totaalprijs = totaalprijs * 0.70
   else:
       if weekendrit:
           totaalprijs =  totaalprijs * 0.60
       else:
           totaalprijs = totaalprijs

   return totaalprijs

Euro = (ritprijs(age, weekend, afstand))
print()
print()
print("Uw Treinkaart kost", (Euro),"Euro")
