import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leAutomato(nomeArquivo):
	if not ".txt" in nomeArquivo:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')	#Abre arquivo
	automato = arquivo.readlines()          #Le arquivo
	arquivo.close()                         #Fecha arquivo
	return filtra(automato)			#Filtra "\n"s e espacos

def fazConversao(automato):
	#Aqui a gente faz junto no laboratorio ☺
	return []


argumentos    = sys.argv	#Captura argumentos passados
listaArquivos = argumentos[1::]	#Remove primeiro argumento(converte.py)

for nomeArquivo in listaArquivos:

	limpaTela()
	
	automato  = leAutomato(nomeArquivo)	#Lê automato a partir de um arquivo
	print("AFND:")
	escreve(automato)
	
	gramatica = fazConversao(automato)	#Converte o automato finito não deterministico em gramatica regular
	print("Gramatica:")
	escreve(gramatica)
	
	input("Pressione ENTER para continuar . . .")