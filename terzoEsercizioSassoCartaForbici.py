class c:
    OK = '\033[92m'  # GREEN
    WARNING = '\033[93m'  # YELLOW
    FAIL = '\033[91m'  # RED
    RESET = '\033[0m'  # RESET COLOR

import random  # importo random per generare le scelte della CPU


def checkWhoWin(player, computer):  # funzione che ritorna True se vince il giocatore o False se vince la CPU
    if player == computer:
        print(c.WARNING + "Pareggio!" + c.RESET)
        return -1
    elif (player == "sasso" and computer == "carta") or (player == "carta" and computer == "forbici") or (
            player == "forbici" and computer == "sasso"):
        print(c.FAIL + "Vince la CPU!" + c.RESET)
        return False
    else:
        print(c.OK + "Vince il player!" + c.RESET)
        return True


# dichiarazioni liste e variabili
choices = ["sasso", "carta", "forbici"]
gioco = ["si", "no"]
player = None
countPlayer = 0
countCPU = 0
continueGame = True
scelta = None

# ciclo che permette di continuare a giocare all'infinito, se deciso dal giocatore
while continueGame is True:

    countPlayer = 0
    countCPU = 0
    while countPlayer != 3 and countCPU != 3:  # condizione che se verificata permette lo svolgimento di un nuovo round
        computer = random.choice(choices)
        while player not in choices:  # controllo se la scelta dell'utente sia una tra sasso, carta o forbice
            player = input(c.OK + "\nSasso carta o forbici?: " + c.RESET).lower()
            if (player not in choices):
                print(c.FAIL + "\nInserire parametri accettati" + c.RESET)
        print(
            c.WARNING + f"\n\nScelta CPU : {computer}\nScelta Player : {player}" + c.RESET)  # stampo la scelta della CPU
        flag = checkWhoWin(player,computer)  # richiamo la funzione checkWhoWin per controllare la possibile vittoria o pareggio dei due giocatori
        if flag is True:
            countPlayer += 1  # incremento il punteggio del giocatore in caso di sua vittoria
        elif flag is False:
            countCPU += 1  # incremento il punteggio della CPU in caso di sua vittoria
        elif flag == -1:
            pass  # in caso di pareggio non incremento alcun punteggio

        print(
            c.WARNING + f"\nPunteggio:\nPlayer: {countPlayer} \nCPU: {countCPU}" + c.RESET)  # stampo i punteggi aggiornati dei due giocatori round per round
        player = None

    # essendo la vittoria assegnata a 3 vittorie di un giocatore controllo se uno dei due giocatori abbia vinto
    if countCPU == 3:
        print(c.FAIL + "\nVince la CPU! Ritenta" + c.RESET)
    else:
        print(c.OK + "\nVince il Player! Complimenti" + c.RESET)

    while scelta not in gioco:  # chiedo fin quando l'input non sia corretto se l'utente vuole continuare a giocare creando una nuova partita
        scelta = input(c.OK + "\nVuoi giocare ancora? " + c.RESET).lower()
    if scelta == "si":
        continueGame = True
    else:
        continueGame = False
        print("\nArrivederci!" + c.RESET)
    scelta = None
