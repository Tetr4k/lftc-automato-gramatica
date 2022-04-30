import sys

argumentos = sys.argv
nomeArquivo = argumentos.pop(0)

arquivo = open(nomeArquivo+".txt", 'r') #Abre arquivo
automato = arquivo.readLines()          #Le arquivo
arquivo.close()                         #Fecha arquivo
