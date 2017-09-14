tickerSymbols = {
	'YAHOO': 'YHOO',
	'GOOGLE INC': 'GOOG',
	'Harley-David son': 'HOG',
	'Yamana Gold': 'AUY',
	'Sotheby\'s': 'BID',
	'inBev': 'BUD'
}

def ticker(filename):
	for s in tickerSymbols.items():
		if filename in s:
			return(s)

print(ticker('YHOO'))
print(ticker("GOOG"))
print(ticker("HOG"))
print(ticker("AUY"))
print(ticker("BID"))
print(ticker("BUD"))

