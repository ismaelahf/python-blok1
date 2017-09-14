
inputlist = ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stamppot"]

vier = []
for word in inputlist:
	if len(word) == 4:
		vier.append(word)

print('De nieuw-gemaakte lijst met alle vier-letter strings is: ', vier)
