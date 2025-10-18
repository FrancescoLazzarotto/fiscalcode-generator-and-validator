from pathlib import Path
import pandas as pd

DATASET_PATH = Path(__file__).parent.parent / "dataset" / "Elenco-comuni-italiani.csv"

try:
    df = pd.read_csv(DATASET_PATH, encoding="latin1", sep=";")
except FileNotFoundError:
    print(f"File CSV non trovato in {DATASET_PATH}")
    exit()