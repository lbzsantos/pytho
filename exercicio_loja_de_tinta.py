#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# OP1 - comprar apenas latas de 18 litros;
# OP2 - comprar apenas galões de 3,6 litros;
# OP3 - misturar latas e galões, de forma que o preço seja o menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. 

print ("\n\n\n\n************** C A S A  B O R G E S  T I N T A S **************")
print("\t TABELA DE PREÇOS: ")
print("\t\t LATA DE 18L : RS80,00")
print("\t\t GALAO DE 3.6L : RS25,00\n")
print("\t* 1 LITRO E SUFICIENTE PARA PINTAR 6m2 *\n")

resp1 = float (input("Informe a medida em metros quadrados (caso tenha apenas as dimensoes, digite 0):\n "))

if resp1 == 0:
    resp2 = float (input("Digite a altura, em metros (somente numero): "))
    resp3 = float (input("Digite o comprimento, em metros (somente numero): "))
    resp1 = resp2*resp3

lts = (resp1/6)*1.1
lts = round(lts + 0.5)
print("Para uma area de",resp1,"m2, voce precisara de",lts,"litros.")

print("Voce tem a opcao de levar so latas de 18L: ")
lata= lts/18
lata= round(lata+0.5)
if lata <=1:
    print(lata,"lata x RS80,00 = RS", lata*80)
else:
    print (lata,"latas x RS80,00 = RS", lata*80)

print ("Voce tem a opcao de levar so galoes de 3,6L: ")
galao = lts/3.6
galao = round(galao+0.5) 
if galao <=1:
    print (galao,"galao x RS25,00 = RS", galao*25)
else:
    print(galao, "galoes x RS25,00= RS", galao*25)
    
if lts >18:
    print ("Voce tem a opcao de levar latas e galoes: ")
    lata = lts//18
    galao = (lts%18)/3.6
    galao = round (galao+0.5)
    if (lata > 1) & (galao > 1):
        print(lata,"latas x RS80,00 =", lata*80,"+", galao, "galoes x RS25,00 =", galao*25, "=RS",lata*80+galao*25)
    elif lata <=1:
        print("1 lata x RS80,00 = RS80","+", galao, "galoes x RS25,00 = RS", galao*25,"= RS", galao*25+80)
    elif galao <= 1:
        print(lata, "latas x RS80,00 = ", lata*80, "+ 1 galao x RS25,00 = RS", lata*80+25)
    else:
        print("1 lata x RS80,00 + 1 galao x RS25,00 = RS105")