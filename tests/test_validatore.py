from src.validatore_cf import validatore_codice_fiscale

def test_cf_valido():
    assert validatore_codice_fiscale("RSSMRA80A01H501U") == True

def test_cf_non_valido():
    assert validatore_codice_fiscale("RSSMRA80A01H501") == False  # lunghezza sbagliata
