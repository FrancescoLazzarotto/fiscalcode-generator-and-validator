from cf_validator import validatore_codice_fiscale
from cf_generator import genera_cf


def main():
    print("----- Portale Codice Fiscale -----")
    print("Vuoi generare il tuo codice fiscale oppure controllare che sia valido?")
    print("Scegli 1 per generare il tuo codice fiscale oppure 2 per controllare il tuo codice fiscale.")

    while True:
        try:
            scelta = int(input("1: Generatore Codice Fiscale | 2: Controllo Codice Fiscale: "))
        except ValueError:
            print("Inserisci un numero valido (1 o 2).")
            continue

        if scelta not in [1, 2]:
            print("Perfavore inserisci 1 oppure 2 in base alla tua scelta.\n")
            continue

        elif scelta == 1:
            nome = input("Inserisci il tuo nome: ").lower()
            cognome = input("Inserisci il tuo cognome: ").lower()
            data_nascita = input("Inserisci la tua data di nascita nel formato (gg/mm/aaaa): ")

            while True:
                sesso = input("Inserisci il tuo sesso nel formato (M/F): ").strip().upper()
                if sesso not in ["M", "F"]:
                    print("Valore non valido. Inserisci M o F.")
                    continue
                break

            comune = input("Inserisci il tuo comune di nascita (es: Torino, non TO): ")
            risultato_generazione = genera_cf(cognome, nome, sesso, data_nascita, comune)
            print("Il tuo codice fiscale generato è:", risultato_generazione)

        elif scelta == 2:
            codice = input("Inserisci il tuo codice fiscale: ")
            risultato_validazione = validatore_codice_fiscale(codice)  
            print("Risultato della validazione:", risultato_validazione)
    

if __name__ == "__main__":
    main()