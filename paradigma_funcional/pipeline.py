import csv
from collections.abc import Iterator

def generar_lineas(path: str) -> Iterator[list[str]]:
    with open(path) as f:
        csv_reader = csv.reader(f)
        for linea in csv_reader:
            yield linea