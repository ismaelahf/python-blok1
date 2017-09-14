stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam',
        'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal',
        '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

naam = input('Wat is uw naam?: ')

def inlezen_beginpunt():
 while True:
    beginstation = input("Wat is je beginstation?: ")
    if beginstation in stations:
       return(beginstation)
    else:
       print("Dit station is niet geldig")

def inlezen_eindpunt(begin):
 while True:
    eindstation = input("Wat is uw eindstation?: ")
    if eindstation in stations:
       if stations.index(eindstation) > stations.index(begin):
          return(eindstation)
       elif stations.index(eindstation) == stations.index(begin):
          print("Dit station is niet geldig")
       else:
          print("Dit station is niet geldig")
    else:
       print("Dit station is niet geldig")

def  beveiliging (string):
  r = str()
  for c in string:
     c = chr(ord(c) + 3)
     r += c
  print(r)

begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
beveiliging (naam)
beveiliging (begin)
beveiliging (eind)
