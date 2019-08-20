#Meu primeiro projeto em python
#Autor: Lucas Santos
#Data: 12/08/2019
#Consiste em um programa para auxiliar o condutor a definir o que é melhor para abastecer o carro entre gasolina e etanol
#Comandos: 

et = float(input("Valor do litro do etanol: "))
gas = float(input("Valor do litro da gasolina: "))
porc = et/gas

if porc > 0.74:
    print ("Gasolina vale mais a pena")
else:
    print ("Etanol vale mais a pena")