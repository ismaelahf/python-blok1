stations = ['Schagen', 'Heerhugowaard', 'Alkmaar','Castricum', 'Zaandam', 'Amsterdam Sloterdijk'
       ,'Amsterdam Centraal','Amsterdam Amstel','Utrecht Centraal','’s-Hertogenbosch','Eindhoven'
        ,'Weert','Roermond','Sittard','Maastricht']


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


def omroepen_reis(begin, eind):
  print("\nHet beginstation is %s, en het stationrangnummer is %i." % (begin, stations.index(begin) + 1))
  print("Het beginstation is %s, en het stationrangnummer is %i." % (eind, stations.index(eind) + 1))


  rangnm = (stations.index(eind) - stations.index(begin) - 1)
  if rangnm > 0:
     print("\nJij stapt in de trein in:",begin , ' en de rangnummer is:', rangnm)
     for i in range(stations.index(begin) + 1, stations.index(eind)):
        print('* ' + stations[i])


  print("\nDe prijs van het kaartje is %d euros." % ((rangnm + 1) * 5))




begin = inlezen_beginpunt()
eind = inlezen_eindpunt(begin)
omroepen_reis(begin, eind)
