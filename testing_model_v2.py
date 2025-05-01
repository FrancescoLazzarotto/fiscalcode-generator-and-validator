
import random
import pandas as pd

df = pd.read_csv("C:/Users/checc/OneDrive/Desktop/Progetto Python/Elenco-comuni-italiani.csv" ,
                 encoding="latin1", sep=";")
consonants = "bcdfghjklmnpqrstvwxyz"


def genera_codici_catastali(comune, df):
    comune = comune.strip().title()  
    riga = df[df["Denominazione in italiano"] == comune]
    if not riga.empty:
        return riga.iloc[0]["Codice Catastale del comune"]
    else:
        return "XXXX"


def genera_ultima_lettera():
    random_letter = chr(random.randint(ord('A'), ord('Z')))
    return random_letter


def genera_cognome(cognome):
    consonants_local = " "
    for i in cognome:
        if i in consonants:
            consonants_local += i
    return consonants_local[0:4]


def genera_nome(nome):
    consonants_local = " "
    for i in nome:
        if i in consonants:
            consonants_local += i
    consonants_piu_4 = consonants_local[1] + consonants_local[3] + consonants_local[4]
    if len(consonants_local) >= 4:
        return consonants_piu_4
    else:
        return consonants_local[0:4]
def anno_cf (data_nascita):
    anno = data_nascita[8:] 
    return anno  

def mese_cf(data_nascita):
    mese = data_nascita[3:5]
    conversione = {
        "01" : "A",
        "02" : "B",
        "03" : "C",
        "04" : "D", 
        "05" : "E",
        "06" : "H",
        "07" : "L",
        "08" : "M",
        "09" : "P", 
        "10" : "R",
        "11" : "S",
        "12" : "T"        
    }
    return conversione.get(mese, "")
    

def giorno_cf(data_nascita, sesso):  
    giorno = data_nascita[0:2]
    if sesso == "M" or sesso == "m":
        return giorno
    else:
        giorno_donna = int(giorno) + 40
        giorno_donna = str(giorno_donna) 
        return giorno_donna 

def genera_cf(cognome, nome, sesso, data_nascita, comune):
    cognome = genera_cognome(cognome)
    nome = genera_nome(nome)
    anno = anno_cf(data_nascita)
    mese = mese_cf(data_nascita)
    giorno = giorno_cf(data_nascita, sesso)
    comune = genera_codici_catastali(comune, df)
    lettera_finale = genera_ultima_lettera()
    codice_fiscale = cognome + nome + anno + mese + giorno + comune + lettera_finale
    return codice_fiscale
    
    
    
    
def validatore_codice_fiscale(codice):
    condizione_lunghezza = False
    condizione_maiuscole = False
    condizione_numeri = False
    condizione_spazi = True
    condizione_simboli = True 
    condizione_primi_sei_caratteri = False #abbreviazione cognome e nome 
    condizione_settimo_ottavo = False #anno numero
    condizione_nono = False #lettera mese
    condizione_decimo_undicesimo = False #numero giorno
    condizione_dodicesimo = False #lettera
    condizione_tredicesimo_quattordicesimo_quindicesimo = False #numero luogo nascita
    condizione_sedicesimo = False #lettera identificativa
    simbolo_speciale = ('@', '!', '#', '%', '$', '£', '?', '*', '.', ',' , '-', '_')
    numero = ('0','1','2','3', '4', '5', '6', '7', '8', '9')
    if len(codice) != 16:
        return False
    else: 
        condizione_lunghezza = True
    if codice.isupper():
        condizione_maiuscole = True
    if codice[0:6].isalpha() and codice[8].isalpha() and codice[11].isalpha() and codice[15].isalpha():
        condizione_primi_sei_caratteri = True
        condizione_nono = True
        condizione_dodicesimo = True
        condizione_sedicesimo = True
    
    if codice[6:8].isdigit() and codice[9:11].isdigit() and codice[12:15].isdigit():
            condizione_settimo_ottavo = True
            condizione_tredicesimo_quattordicesimo_quindicesimo = True
            condizione_decimo_undicesimo = True
        
    for i in codice:
        if i in numero and all([condizione_decimo_undicesimo, condizione_tredicesimo_quattordicesimo_quindicesimo, condizione_settimo_ottavo]):
            condizione_numeri = True
        if i in simbolo_speciale:
            condizione_simboli = False
            break
        if i == " ":
            condizione_spazi = False
        
    if all([condizione_sedicesimo, condizione_decimo_undicesimo, condizione_dodicesimo, condizione_lunghezza, condizione_maiuscole, condizione_numeri, condizione_simboli, 
           condizione_spazi, condizione_primi_sei_caratteri, condizione_settimo_ottavo, condizione_nono, condizione_tredicesimo_quattordicesimo_quindicesimo]):
        print(f"Codice fiscale: {codice} valido!")
        return True
        
    else:
        print(f"Codice fiscale: {codice} non valido!")
        return False       

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
            nome = input("Inserisci il tuo nome: ")
            cognome = input("Inserisci il tuo cognome: ")
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
    


        