   
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