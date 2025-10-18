from src.generatore_cf import genera_cf

def test_genera_cf_base():
    cf = genera_cf("Rossi", "Mario", "M", "01/01/1980", "Torino")
    assert len(cf) == 16
    assert cf[:3] == "RSS"
    assert cf[3:6] == "MRA"

def test_genera_cf_donna():
    cf = genera_cf("Bianchi", "Anna", "F", "15/05/1990", "Milano")
    giorno = int(cf[9:11])
    assert giorno > 31  # giorno per donna aumenta di 40
