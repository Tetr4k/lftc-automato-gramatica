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
	#Pega primeira linha e retorna o ultimo caractere
	aux = automato[0]
	return aux[-1]

def capturaFinais(automato):
	#Pega segunda linha e retorna uma lista ordenada com os finais
	aux    = automato[1]
	finais = aux[3::2]
	return sorted(finais)

def trocaInicio(gramatica, I):
	aux = []
	for linha in gramatica:
		linha.replace("1", "0").replace(I, "1").replace("0", I)
		aux.append(linha)
	return aux

def converteSimbolos(gramatica):
	aux = []
	for linha in gramatica:
		auxLinha = ""
		for c in linha:
			if c.isdigit():
				c = chr(int(c)+64)
			auxLinha+=c
		aux.append(auxLinha)
	return aux
def fazConversao(automato):
	#Inicia lista de linhas da gramatica
	gramatica = []
	
	#Captura estado inicial a partir da primeira linha
	inicio = capturaInicio(automato)
	
	#Captura estados finais a partir da segunda linha
	finais = capturaFinais(automato)
	
	#Captura transições das linhas seguintes
	for transicao in automato:
		for c in transicao[4::]:
			if c.isdigit():
				linha = transicao[1] + "->"
				if transicao[3] != "@":
					linha+=transicao[3]
				linha+=c
				gramatica.append(linha)

	#Caso I seja diferente de 1, troca todo I com 1
	if inicio!="1":
		gramatica = trocaInicio(gramatica, inicio)

	gramatica = sorted(gramatica)
				
	#Converter numeros dos estados em seus respectivos simbolos
	gramatica = converteSimbolos(gramatica)

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
