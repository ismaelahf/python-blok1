import xmltodict

xml = xmltodict.parse(open('trein.xml', 'rb'))
stations = xml['Stations']['Station']

print(stations)

print('Dit zijn de codes en types van de 4 stations:')
for i in stations:
    print(i['Code'], '-', i['Type'])

print()

print('Dit zijn alle stations met één of meer synoniemen:')
for i in stations:
    if i['Synoniemen']:
        print(i['Namen']['Middel'] + ':')
        for j in i['Synoniemen']['Synoniem']:
            print('\t-', j)

print()

print('Dit zijn de codes en types van de 4 stations:')
for i in stations:
    print(i['Code'], '-', i['Namen']['Lang'])

print()

