from pathlib import Path

# para tratar erros de arquivos não encotrado

# try:
#     arquivo = open("meu_arquivo.txt")
# except FileNotFoundError as exc:
#     print("Arquivo não encontrado!!")
#     print(exc)

# erros no diretorio

# ROOT_PATH = Path(__file__).parent

# try:
#     arquivo = open(ROOT_PATH / "novo_dir")
# except IsADirectoryError as exc:
#     print(f"Não foi possivel abrir o arquivo {exc}")

# tratamento de erros comuns

ROOT_PATH = Path(__file__).parent

try:
    arquivo = open(ROOT_PATH / "novo_dir" / "novo.txt")
except FileNotFoundError as exc:
    print(f"Arquivo não encontrado! {exc}")
except IsADirectoryError as exc:
    print(f"Não foi possivel abrir o arquivo! {exc}")
except OSError as exc:
    print(f"Erro ao abrir o arquivo! {exc}")
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo! {exc}")
