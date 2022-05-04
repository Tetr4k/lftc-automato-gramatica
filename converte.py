import sys, os, platform

sistema = platform.system()

def limpaTela():
	if sistema == "Windows":
		os.system("cls")
	else:
		os.system("clear")	

def escreve(texto):
	for linha in texto:
		print(linha)

def filtraQuebraDeLinha(linha):
	return linha.replace("\n", "")

def leAutomato(nomeArquivo):
	if not ".txt" in nomeArquivo:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')	#Abre arquivo
	automato = arquivo.readlines()          #Le arquivo
	arquivo.close()                         #Fecha arquivo
	automatoFiltrado = []
	for linha in automato:
		linhaSemQuebra = linha.replace("\n", "")		#Remove quebras de linha
		linhaSemEspaco = linhaSemQuebra.replace(" ", "")	#Remove espaços
		automatoFiltrado.append(linhaSemEspaco)
	return automatoFiltrado

def fazConversao(automato):
'''
  Aqui a gente faz junto no laboratorio ☺
'''

argumentos    = sys.argv	#Captura argumentos passados
listaArquivos = argumentos[1::]	#Remove primeiro argumento("converte.py")

for nomeArquivo in listaArquivos:
	
	limpaTela()
	
	automato  = leAutomato(nomeArquivo)	#Lê automato a partir de um arquivo
	print("AFND:")
	escreve(automato)	#Escreve o automato
	
	print("-----------------")
	
	gramatica = fazConversao(automato)	#Converte o automato finito não deterministico em gramatica regular
	print("Gramatica:")
	escreve(gramatica)	#Escreve a gramatica
	
	input("Pressione ENTER para continuar . . .")
