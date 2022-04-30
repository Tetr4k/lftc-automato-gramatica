import sys

def fazConversao(automato):
'''
  Aqui a gente faz junto no laboratorio ☺
'''

argumentos = sys.argv
nomeArquivo = argumentos.pop()

arquivo = open(nomeArquivo, 'r') #Abre arquivo
automato = arquivo.readlines()          #Le arquivo
arquivo.close()                         #Fecha arquivo

gramatica = fazConversao(automato) #Converte o automato finito não deterministico em gramatica regular

for linha in gramatica: #Escreve a gramatica
	print(linha)
