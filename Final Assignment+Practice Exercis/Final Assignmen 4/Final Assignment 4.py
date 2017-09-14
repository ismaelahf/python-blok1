file = open('./annuleerd.txt', 'r')
geannuleerd = []
for line in file:
  geannuleerd.append(line[13:-1])
file.close()


file = open('./trein.txt', 'r+')
newfile = open('./newTrein.txt', 'w')
for line in file:
   if not line[11:-1] in geannuleerd:
      newfile.write(line)
else:
  print('%s is verwijderd uit trein.txt omdat het in annuleerd.txt is' % line[11:-1])
file.close()
newfile.close()

print()
