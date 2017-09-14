lst = '5-9-7-1-7-8-3-2-4-8-7-9'
lst = list(map(int, lst.split('-')))
lst.sort()

print('De grootste waarde:', lst[-1])
print('De kleinste waarde:', lst[0])
print('Number of numbers:', len(lst))
print('Het aantal getallen', sum(lst))
print('het gemiddelde:', (sum(lst) / len(lst)))
