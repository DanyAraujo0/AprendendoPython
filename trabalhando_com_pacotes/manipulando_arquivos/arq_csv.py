import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:  # boa pratica é utilizar writer e reader do que read/write
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])
        escritor.writerow(["1", "Maria"])
        escritor.writerow(["2", "Jão"])
except OSError as exc:
    print(f"Erro ao criar o arquivo {exc}")

# lendo o arquivo
try:
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for row in leitor:
            print(row)
except OSError as exc:
    print(f"Erro ao criar o arquivo {exc}")

# lendo de maneira mais visual
try:
    with open(ROOT_PATH / "usuarios.csv", newline="", encoding="utf-8") as arquivo:
        reader = csv.DictReader(arquivo)
        for row in reader:
            print(f"{row['id']}, {row['nome']}")
except OSError as exc:
    print(f"Erro ao criar o arquivo {exc}")
