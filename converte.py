import sys, os, platform

sistema = platform.system()

def limpaTela():
	if sistema == "Windows":
		os.system("cls")
	else:
		os.system("clear")	

def escreve(texto):
	cont=0
	for linha in texto:
		cont+=1
		print(f'\t{cont}| {linha}')
	print("\t----------------")

def filtraQuebraDeLinha(linha):
	return linha.replace("\n", "")

def filtraEspacos(linha):
	return linha.replace(" ", "")

def filtra(linha):
	linha = filtraQuebraDeLinha(linha)
	linha = filtraEspacos(linha)
	return linha

def leAutomato(nomeArquivo):
	if not ".txt" in nomeArquivo:
		nomeArquivo += ".txt"
	arquivo	 = open(nomeArquivo, 'r')	#Abre arquivo
	automato = arquivo.readlines()          #Le arquivo
	arquivo.close()                         #Fecha arquivo
	automatoFiltrado = []
	for linha in automato:
		linha = filtra(linha)		#Filtra "\n"s e " "s
		automatoFiltrado.append(linha)
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
	
	gramatica = fazConversao(automato)	#Converte o automato finito não deterministico em gramatica regular
	print("Gramatica:")
	escreve(gramatica)	#Escreve a gramatica
	
	input("Pressione ENTER para continuar . . .")
