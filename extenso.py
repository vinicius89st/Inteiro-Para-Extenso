import math
import sys

extenso = {1 : "um", 
		   2 : "dois", 
		   3 : "três", 
		   4: "quatro", 
		   5 : "cinco", 
		   6 : "seis",	
		   7 : "sete",	
		   8 : "oito",	
		   9 : "nove",	
		   10 : "dez",	
		   11 : "onze", 
		   12 : "doze", 
		   13 : "treze",	
		   14 : "quatorze", 
		   15 : "quinze",	
		   16 : "dezesseis",	
		   17 : "dezessete", 
		   18 : "dezoito", 
		   19 : "dezenove", 
		   20 : "vinte", 
		   30 : "trinta", 
		   40 : "quarenta", 
		   50 : "cinquenta", 
		   60 : "sessenta", 
		   70 : "setenta",
		   80 : "oitenta", 
		   90 : "noventa", 
		   100 : "cento", 
		   200 : "duzentos", 
		   300 : "trezentos", 
		   400 : "quatrocentos", 
		   500 : "quinhentos", 
		   600 : "seissentos", 
		   700 : "setessentos", 
		   800 : "oitossentos",
		   900 : "novessentos", 
		  }

def qtdNumeros(numero):
	'''
	Conta a quantidade de digitos um número possui
	'''
	contador = 0
	decimal = 1
	while decimal <= numero:
		decimal *= 10
		contador += 1
	return contador

def tresDigitos(numero):
	'''
	imprime por extenso uma sequencia de até três números
	'''
	decimal = 10
	lista = []
	resposta = ""
	i = 0 # contador da lista
	if(numero == 0):
		print ("zero ", end="")
		return
	if(numero == 100):
		print ("cem ", end="")
		return
	while (len(lista) < 3):
		lista.append((numero % decimal))
		numero -= lista[i] # subtraindo unidade, dezena e centena (nesta ordem) do número dado como parâmetro
		i += 1  
		decimal = decimal * 10
	if(lista[1] == 10): # verifica se o numero se encontra entre 10 e 19, caso positivo, soma a dezena com a unidade
		lista[1] = lista[1] + lista[0]
		lista[0] = 0
	for i in reversed(lista):
		if(i > 0):
			resposta += extenso[i] + " e "
	print (resposta[:-2], end= "") #

def porExtenso(numero):
	'''
	Imprime por extenso um numero de até 9 digitos, esse metodo se apoia no metodo tresDigitos() para funcionar
	'''
	qtd = qtdNumeros(numero)
	if(numero == 0):#trata caso o numero seja zero
		print ("zero ", end="")
	if(qtd >= 7 and qtd <= 9):
		tresDigitos(math.floor(numero/1000000)) #arredondamento dos numeros
		if(numero < 2000000): #verifica se deve ser impresso a palavra milhão ou milhões
			print ("milhão", "" ,end="")
		else:
			print ("milhões", "" ,end="")
		numero -= math.floor(numero/1000000)*1000000
		qtd = qtdNumeros(numero)
	if(qtd >= 4 and qtd <= 6):
		tresDigitos(math.floor(numero/1000))
		print ("mil", "" ,end="")
		numero -= math.floor(numero/1000)*1000
		qtd = qtdNumeros(numero)
	if(qtd >= 1 and qtd <= 3):
		tresDigitos(numero)


#Parte utilizada para imprimir em reais o valor com até 9 digitos antes da virgula e com dois digitos após
entrada = input("insira o valor desejado: ")
valor = entrada.split(",")
if(int(valor[0]) > 999999999 or len(valor[1]) != 2):
	print("só é possível inserir um valor de até 9 digitos antes da vírgula e exatamente 2 após.")
	sys.exit()
porExtenso(int(valor[0]))
if(int(valor[0]) == 1):
	print("real", end="")
else:
	print("reais", end="")
print(" e ", end="")
porExtenso(int(valor[1]))
if(int(valor[1]) == 1):
	print("centavo")
else:
	print("centavos")
