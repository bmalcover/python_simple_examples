import random

'''
Programa aritmetic que permet fer una serie d'operacions simples i comprovar el seu resultat
Amb aquest programa practicam: E/S, condicionals, bucles, assignacions i generacio de nombres aleatoris
'''

punts = 0
nom = input("Com et dius? ")
print(nom)

num = input("Quantes operacions vols fer?")
print("Vols fer: " + num + " operacions")

num = int(num)

for i in range(num):

    operand1 = random.randint(0, 20)
    operand2 = random.randint(1, 20)

    operacio = random.randint(0, 3)
    resultat = 0

    print("Quant fan ")
    if(operacio == 0): # suma
        print(str(operand1) + " + " + str(operand2) + "?")
        resultat = operand1 + operand2
    elif(operacio == 1):
        print(str(operand1) + " - " + str(operand2) + "?")
        resultat = operand1 - operand2

    elif (operacio == 2):
        print(str(operand1) + " * " + str(operand2) + "?")
        resultat = operand1 * operand2

    elif (operacio == 3):
        print(str(operand1) + " / " + str(operand2) + "?")
        resultat = operand1 // operand2


    resultat_usuari = int(input())

    if resultat == resultat_usuari:
        print("Bona resposta")
        punts += 1
    else:
        print(" :( La resposta era: " + str(resultat))

print(nom + ", has fet: " + str(punts) + " punts")