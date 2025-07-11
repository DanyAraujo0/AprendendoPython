arquivo = open(
    "C:\\projetos\AprendendoPython\\trabalhando_com_pacotes\\manipulando_arquivos\\arq_escrito.txt",
      "w")
# para escrever é necessario passar w para abrir e usar write
arquivo.write("Escrevendo no arquivo de teste")
arquivo.writelines(["\n","Escrevendo","\n","outra","\n","linha","\n","no","\n","arquivo","\n","de","\n","teste"])

arquivo.close()