
# Librerie
import random as rm

def gioco():
    nome = str(input("Ciao, ti do il benvenuto al BlackJack! Come ti chiami? "))
    eta = int(input(f"Ottimo, {nome}. Quanti anni hai? "))
    if eta >= 18:
        print(f"Perfetto, {nome}! Giochiamo. Distribuisco le carte...")
        mazzo = ["Asso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Regina", "Re"]
        carta1 = rm.choice(mazzo)
        carta2 = rm.choice(mazzo)
        carta3 = rm.choice(mazzo)
        punteggioG = 0  # Punteggio giocatore
        punteggioB = 0 # Punteggio banco

        # GESTIONE PRIMA CARTA
        if carta1.isdigit():  #.isdigit() verifica se la carta è un numero o una stringa.
            punteggioG = punteggioG + int(carta1) # Se pesco un numero, si trasforma in intero e si somma al punteggio.
        elif carta1 in ["Jack", "Regina", "Re"]:
            punteggioG = punteggioG + 10
        elif carta1 == "Asso":
            punteggioG = punteggioG + 11
        
        # GESTIONE SECONDA CARTA
        if carta2.isdigit():
            punteggioG = punteggioG + int(carta2)
        elif carta2 in ["Jack", "Regina", "Re"]:
            punteggioG = punteggioG + 10
        elif carta2 == "Asso":
            punteggioG = punteggioG + 11

        # GESTIONE TERZA CARTA
        if carta3.isdigit():
            punteggioB = punteggioB + int(carta3)
        elif carta3 in ["Jack", "Regina", "Re"]:
            punteggioB = punteggioB + 10
        elif carta3 == "Asso":
            punteggioB = punteggioB + 11
            
        giocatore = [{carta1: punteggioG}, {carta2: punteggioG}]
        print(f"Hai pescato: {carta1} e {carta2}. Quindi hai: {punteggioG}. Invece, il banco ha pescato: {carta3}. Quindi ha: {punteggioB}. Vuoi carta? (sì/no)")

        # Nel caso in cui il giocatore chieda di pescare una terza carta, si pesca e si calcola il punteggio.     
        # GESTIONE QUARTA CARTA  
        risposta = str(input().lower())
        if risposta == "sì":
            carta4 = rm.choice(mazzo)
            if carta4.isdigit():
                punteggioG = punteggioG + int(carta4)
            elif carta4 in ["Jack", "Regina", "Re"]:
                punteggioG = punteggioG + 10
            elif carta4 == "Asso":
                punteggioG = punteggioG + 11
            print(f"Hai pescato {carta1}, {carta2} e {carta4}. Quindi hai: {punteggioG}. Invece, il banco ha: {punteggioB}.")
        
        # Nel caso in cui il giocatore ha un punteggio di 11 o meno.
        if punteggioG <= 11:
            carta5 = rm.choice(mazzo)
            if carta5.isdigit():
                punteggioG = punteggioG + int(carta5)
            elif carta5 in ["Jack", "Regina", "Re"]:
                punteggioG = punteggioG + 10
            elif carta5 == "Asso":
                punteggioG = punteggioG + 11
            print(f"Hai pescato {carta1}, {carta2} e {carta5}. Quindi hai: {punteggioG}. Invece, il banco ha: {punteggioB}.")
    
        # Nel caso in cui il giocatore abbia 21 punti, vince automaticamente.
        if punteggioG == 21:
            print(f"Complimenti, {nome}! Hai fatto 21 punti, hai vinto!")
            return
        else:
            if punteggioG > 21:
                print(f"Mi dispiace, {nome}, ma hai sballato quindi hai perso.")
     
        # FINE GIOCATORE
        # INIZIO BANCO
        
        # REGOLA DEL 17: se il banco ha meno di 16 punti, deve pescare una carta.
        if punteggioB <= 16:
            carta6 = rm.choice(mazzo)
            if carta6.isdigit():
                punteggioB = punteggioB + int(carta6)
            elif carta6 in ["Jack", "Regina", "Re"]:
                punteggioB = punteggioB + 10
            elif carta6 == "Asso":
                punteggioB = punteggioB + 11
            print(f"Il banco ha {carta3} e {carta6}. Quindi ha: {punteggioB}.")

        
        # Nel caso abbia 17 punti o più, SI FERMA
        if punteggioB >= 17:
            print(f"Il banco si ferma con {punteggioB} punti.")
        
        # CONFRONTO PUNTEGGI
        if punteggioG > 21:
            print(f"Mi dispiace, {nome}, ma hai sballato quindi hai perso.")
        elif punteggioB > 21:
            print(f"Complimenti, {nome}! Il banco ha sballato quindi hai vinto!")
        elif punteggioG > punteggioB:
            print(f"Complimenti, {nome}! Hai vinto!")
        elif punteggioG < punteggioB:
            print(f"Mi dispiace, {nome}, ma hai perso.")
        else:
            print(f"Parità! Nessuno vince, {nome}.")
    else:
        print(f"Mi dispiace, {nome}, ma sei troppo piccolo per queste cose.")
    return

gioco()