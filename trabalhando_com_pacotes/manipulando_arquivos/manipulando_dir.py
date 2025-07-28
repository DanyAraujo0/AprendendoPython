import shutil
from pathlib import Path

ROOT_PATH = Path(
    __file__
).parent  # atraves do path ele pega o caminho do arquivo e não importa o sistema operacional da maq

# os.mkdir(ROOT_PATH / 'novo_dir')

# arquivo = open(ROOT_PATH / "novo.txt", "w")
# arquivo.close()

# # renomeando um arquivo

# os.rename(ROOT_PATH / 'novo.txt',ROOT_PATH / 'alterado.txt')

# removendo um arquivo

# os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo_dir" / "novo.txt")
