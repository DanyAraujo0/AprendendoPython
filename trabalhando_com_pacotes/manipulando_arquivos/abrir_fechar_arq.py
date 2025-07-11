# usamos a função open() para abrir um aquivo
file = open("C:\\projetos\AprendendoPython\\trabalhando_com_pacotes\\manipulando_arquivos\\arquivo.txt", "r")
print(file.read())
# é necessario fechar todo arquivo aberto para isso usamos a função close()
file.close()
