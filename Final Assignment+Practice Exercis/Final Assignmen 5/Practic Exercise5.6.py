studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
	antw = []
	for lst in studentencijfers:
		antw.append(round(sum(lst) / len(lst)))
	return(antw)

def gemiddelde_van_alle_studenten(studentencijfers):
	return(round(sum(studentencijfers) / len(studentencijfers)))

resultaat1 = gemiddelde_per_student(studentencijfers)
print(resultaat1)
resultaat2 = gemiddelde_van_alle_studenten(resultaat1)
print(resultaat2)
