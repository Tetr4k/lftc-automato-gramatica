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
	gramatica = []
	# linha 1 - Estado inicial
	aux = automato[0]
	I   = aux[-1]
	# linha 2 - Estados finais
	aux = automato[1]
	for c in aux:
		if c.isdigit():
			linha = c + " -> ε"
			gramatica.append(linha)			
	# linhas N - Transições
	aux = automato[2::]
	for transicao in aux:
		for c in transicao[4::]:
			if c.isdigit():
				linha = transicao[1] + " -> " + transicao[3] + c
				gramatica.append(linha)
				
	return gramatica


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
