import sys
from funcoesAuxiliares import limpaTela, filtra, escreve

def leAutomato(nomeArquivo):
	if not ".txt" in nomeArquivo:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')	#Abre arquivo
	automato = arquivo.readlines()          #Le arquivo
	arquivo.close()                         #Fecha arquivo
	return filtra(automato)			#Filtra "\n"s e espacos

def capturaInicio(automato):
	aux = automato[0]
	return aux[-1], automato[1::]


def fazConversao(automato):
	#Inicia lista de linhas da gramatica
	gramatica = []
	
	#Captura estado inicial a partir da primeira linha
	I, automato = capturaInicio(automato)
	
	#Captura estados finais a partir da segunda linha
	aux = automato[1]
	for c in aux:
		if c.isdigit():
			linha = c + " -> ε"
			gramatica.append(linha)	
	
	#Captura transições das linhas seguintes
	aux = automato[2::]
	for transicao in aux:
		for c in transicao[4::]:
			if c.isdigit():
				linha = transicao[1] + "->"
				if transicao[3] != "@":
					linha+=transicao[3]
				linha+=c
				gramatica.append(linha)
				
	#Converter numeros dos estados em seus respectivos simbolos
				
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
