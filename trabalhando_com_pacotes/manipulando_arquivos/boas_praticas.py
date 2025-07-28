from pathlib import Path

ROOT_PATH = Path(__file__).parent

# use o gerenciamento de contexto (context manager) com a declaração with
# atraves disso poderemos trabalhar com os arquivos de forma segura garantindo que
# eles sejam fechados de forma segura

try:
    with open(ROOT_PATH / "aarquivo.txt") as arquivo:
        print(arquivo.read())
except OSError as exc:
    print(f"Erro ao abrir o arquivo {exc}")

# use a codificação correta ao ler e gravar arquivos de texto
# o argumento encoding da função open permite especificar a codificação correta

# try:
#     with open(ROOT_PATH / "arquivo-utf-8.txt", encoding="utf-8") as arquivo:
#         arquivo.write("Aprendendo manipular arquivos com python")
# except IOError as exc:
#     print(f"Erro ao abrir o arquivo {exc}")


try:
    with open(ROOT_PATH / "arquivo-utf-8.txt", encoding="ascii") as arquivo:
        print(arquivo.read())
except OSError as exc:
    print(f"Erro ao abrir o arquivo {exc}")
