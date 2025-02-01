'''
Le but du juste prix est de deviner un nombre entier choisi aléatoirement par Python. 
Écrivez un script qui attribue un nombre à une variable. 
Dans une boucle, demandez un input à l’utilisateur et informez le joueur si le nombre entré est égale, plus grand ou plus petit que le juste prix.
'''

import random

prix = random.randint(1, 100)  #random.randint(1, 100) permet de generer un nombre aleatoire entre 1 et 100

score = 200

tentative = 0
print("Bienvenue dans le jeu du juste prix")
print("Vous avez 200 points pour deviner le juste prix")
print("Devinez le juste prix compris entre 1 et 100")

while True:
    nombre = int(input("Entrez un nombre : "))
    tentative += 1 # Incrementation de la variable tentative
    if nombre < prix:
        print("Le juste prix est plus grand")
        score -= 10
    if nombre > prix:
        print("Le juste prix est plus petit")
        score -= 10
    if nombre == prix:
        print(f"Bravo vous avez gagne en {tentative} tentatives")
        print(f"Votre score est de {score}")
        break

print("Fin de la partie")
print()
print("Souhaiterez vous rejouez")
rejouer = input("Oui ou Non : ")
if rejouer == "Oui":
    prix = random.randint(1, 100)
    score = 200
    tentative = 0
    print("Bienvenue dans le jeu du juste prix")
    print("Vous avez 200 points pour deviner le juste prix")
    print("Devinez le juste prix compris entre 1 et 100")
    while True:
        nombre = int(input("Entrez un nombre : "))
        tentative += 1
        if nombre < prix:
            print("Le juste prix est plus grand")
            score -= 10
        if nombre > prix:
            print("Le juste prix est plus petit")
            score -= 10
        if nombre == prix:
            print(f"Bravo vous avez gagne en {tentative} tentatives")
            print(f"Votre score est de {score}")
            break
    print("Fin de la partie")
else:
    print("Merci d'avoir jouer")
    print("Fin du jeu")
    exit()