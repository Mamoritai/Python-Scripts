employee = [
    {
        "name": "Al Buquerque",
        "boss": None,
        "party-animal-score": 2.0
    },
    {
        "name": "Ferb Jinglemore",
        "boss": "Al Buquerque",
        "party-animal-score": 12.1
    },
    {
        "name": "Click N. Clack",
        "boss": "Al Buquerque",
        "party-animal-score": 34.3
    },
    {
        "name": "Carl Balgruuf",
        "boss": "Ferb Jinglemore",
        "party-animal-score": -0.4
    },
    {
        "name": "Moe Shroom",
        "boss": "Carl Balgruuf",
        "party-animal-score": 44.91
    },
    {
        "name": "Jerky McGetsDrunkAndPeesInYourFridge",
        "boss": "Carl Balgruuf",
        "party-animal-score": -9999.99
    },
    {
        "name": "Howard M. Burgers",
        "boss": "Click N. Clack",
        "party-animal-score": 14.4
    },
    {
        "name": "Soren de Kiester",
        "boss": "Click N. Clack",
        "party-animal-score": 25
    }
]
##print (len(employee))
##for i in range (len(employee)):
##    if None in employee[i].values():
##        print(employee[i].keys())

final_list = []
length = (len(employee))
print (employee)
for i in range (length):
    temp = []
    dictlist = []
    print (employee[i])
    for key, value in employee[i].items():
        temp = [key, value]
        dictlist.append(temp)
    final_list.append(dictlist)
    print(final_list[i])

