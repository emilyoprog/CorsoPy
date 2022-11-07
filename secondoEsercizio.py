'''
Scrivi una funzione a cui vengono passati come parametro un elemento e una lista di elementi,
e che ti dica in output se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, la funzione dovrà inoltre comunicarci l'indice dell'elemento.
'''

def findIfTrue(value, list):
    if value in list:
        print(f"Elemento inserito gia presente nella postizione {list.index(value)}")
    else:
        list.append(value)

def inputValue(scelta):
    if scelta == 1:
        value = input("Inserire la stringa da aggiungere: ")
    elif scelta == 2:
        value = int(input("Inserire l'intero da aggiungere: "))
    elif scelta == 3:
        value = float(input("Inserire il float da aggiungere: "))
    else:
        print("Valore non accettato")
        return -1
    return value


listToPass = ["Francesco", "Emilio", 15, 35.45]
ciclo = int(input("Quanti dati vuoi inserire :"))

for x in range(ciclo):
    scelta = int(input("Che valore vuoi aggiungere? (1-stringa / 2-Intero / 3-Float :"))
    value = inputValue(scelta)
    if value == -1:
        exit(-1)
    findIfTrue(value,listToPass)


