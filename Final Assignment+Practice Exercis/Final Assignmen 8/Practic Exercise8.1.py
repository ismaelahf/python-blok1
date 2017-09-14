import json
import xmltodict

xml = xmltodict.parse(open('producten.xml', 'rb'))
for i in xml['artikelen']['artikel']:
    print(i['@nummer'], i['code'], i['naam'], i['voorraad'], i['prijs'])

print()
