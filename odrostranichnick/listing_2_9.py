companies = {
    'CoolCompany': {'Alice': 33, 'Bob': 28, 'Frank': 29},
    'CheapCompany': {'Ann': 4, 'Lee': 9, 'Chrisi': 7},
    'SosoCompany': {'Esther': 38, 'Cole': 8, 'Paris': 18}
}

illegal = [x for x in companies if any(y < 9 for y in companies[x].values())]

for i in illegal:
    print(i)
