import pandas as pd

try:
    df = pd.read_csv("C:/Users/checc/OneDrive/Desktop/Progetto Python/Elenco-comuni-italiani.csv" ,
                 encoding="latin1", sep=";")

except FileNotFoundError:
    print("File CSV non trovato. Verifica il percorso.")
    exit()
    
consonants = "bcdfghjklmnpqrstvwxyz"


def genera_codici_catastali(comune, df):
    comune = comune.strip().title()  
    riga = df[df["Denominazione in italiano"] == comune]
    if not riga.empty:
        return riga.iloc[0]["Codice Catastale del comune"]
    else:
        return "XXXX"


def genera_cognome(cognome):
    consonants_local = ""
    for i in cognome:
        if i in consonants:
            consonants_local += i
    return consonants_local[0:3]


def genera_nome(nome):
    consonants_local = ""
    for i in nome:
        if i in consonants:
            consonants_local += i
    
    if len(consonants_local) >= 4:
        consonants_piu_4 = consonants_local[0] + consonants_local[2] + consonants_local[3]
        return consonants_piu_4
    else:
        return consonants_local.ljust(3, 'X')
    
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





def calcola_ultima_lettera(codice_fiscale):
    """
    L'ultima lettera segue un algoritmo specifico: 
    Convertire i caratteri in numeri: Ogni carattere del Codice Fiscale viene convertito in un numero in base alla posizione (pari o dispari) 

    Calcolare la somma ponderata:
    I caratteri nelle posizioni pari (come 2, 4, 6, ...) vengono mappati ai valori della colonna "Valore pari".
    I caratteri nelle posizioni dispari (come 1, 3, 5, ...) vengono mappati ai valori della colonna "Valore dispari".

    Somma e diviso 26:
    Sommiamo tutti i valori ottenuti dalla conversione dei caratteri e poi calcoliamo il resto della divisione per 26.
    Il resto della divisione viene usato per determinare la lettera attraverso una tabella di conversione
    """
    valori_pari = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 
        'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    
    valori_dispari = {
        '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21, 
        'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21, 
        'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14, 
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }
    
    lettere_di_controllo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    somma = 0
    
    for i, char in enumerate(codice_fiscale):  
        char = char.upper()
        pos_i = i + 1 
        
        if pos_i % 2 == 1: 
            somma += valori_dispari.get(char, 0)
        else: 
            somma += valori_pari.get(char, 0)

    resto = somma % 26
    lettera_controllo = lettere_di_controllo[resto]  
    return lettera_controllo
   



def genera_cf(cognome, nome, sesso, data_nascita, comune):
    cognome = genera_cognome(cognome)
    nome = genera_nome(nome)
    anno = anno_cf(data_nascita)
    mese = mese_cf(data_nascita)
    giorno = giorno_cf(data_nascita, sesso)
    comune = genera_codici_catastali(comune, df)
    codice_fiscale = cognome + nome + anno + mese + giorno + comune
    ultima_lettera = calcola_ultima_lettera(codice_fiscale)
    codice_fiscale += ultima_lettera
    codice_fiscale = codice_fiscale.upper()
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
    


        
