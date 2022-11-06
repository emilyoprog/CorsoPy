'''
Scrivi una funzione che data in ingresso una lista A contenente n parole,
restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
'''

def returnLength(list):
    listLength = []
    a = 0
    for i in list:
        listLength.append(len(i))
        print(listLength[a], end=" ")
        a = a + 1


listName = ["Anna",
            "Francesco",
            "Emilio",
            "Michele"]

returnLength(listName)
