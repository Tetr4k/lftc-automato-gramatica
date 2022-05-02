import sys

def escreve(texto):
	for linha in texto:
		print(linha)

def leAutomato(nomeArquivo):
	arquivo	 = open(nomeArquivo, 'r')	#Abre arquivo
	automato = arquivo.readlines()          #Le arquivo
	arquivo.close()                         #Fecha arquivo
	return automato

def fazConversao(automato):
'''
  Aqui a gente faz junto no laboratorio ☺
'''

argumentos    = sys.argv		#Captura argumentos passados
listaArquivos = argumentos.pop()	#Remove primeiro argumento("converte.py")

for nomeArquivo in listaArquivos:
	
	automato  = leAutomato(nomeArquivo)	#Lê automato a partir de um arquivo
	print("AFND:")
	escreve(automato)	#Escreve o automato
	
	print("-----------------")
	
	gramatica = fazConversao(automato)	#Converte o automato finito não deterministico em gramatica regular
	print("Gramatica:")
	escreve(gramatica)	#Escreve a gramatica
