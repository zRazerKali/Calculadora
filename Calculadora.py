#!/usr/bin/python
import os,requests,sys
os.system("clear")

os.system("figlet -t Calculadora")
print "#====================#"
print "| [1] Mais           |"
print "| [2] Menos          |"
print "| [3] Vezes          |"
print "| [4] Divisao        |"
print "#====================#"
print
x = int(input("Digite a opcao desejada: "))

if 1:
	print "Escolhido Com Sucesso"
elif 2:
	print "Escolhido Com Sucesso"
elif 3:
        print "Escolhido Com Sucesso"
elif 4:
        print "Escolhido Com Sucesso"

numer1 = int(input("Primeiro Valor: "))
numer2 = int(input("Segundo Valor: "))

if x == 1:
	print "Resultado: ",numer1 + numer2

elif x == 2:
        print "Resultado: ",numer1 - numer2

elif x == 3:
        print "Resultado: ",numer1 * numer2

elif x == 4:
        print "Resultado: ",numer1 / numer2




