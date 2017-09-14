cijferICOR = 6
cijferPROG = 7
cijferCSN = 8
beloning = 30
totaal = cijferICOR + cijferPROG +  cijferCSN
gem = totaal / 3


overzicht ='Mijn cijfer (gemiddeld een ' + str(gem ) + ')leveren een beloning van € '+str(beloning*totaal)
print(overzicht)
