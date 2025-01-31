# Projet debutant python. 
# Convertisseur d'unite

# Demander a l'user quel type de conversion il veut faire


print("Bienvenue dans notre programme")
print()
print("Nous allons vous demmander votre nom pour continuer ")
nom_user = input(print("Quel est votre nom ? "))

print("Bonjour " +(nom_user), "nous allons vous demander quel type de conversion vous voulez faire. Vous avez le choix entre : ")

print("1. Conversion de pouce vers centimetre")
print("2. Conversion de centimetre vers pouce")

choix = input(print("Quel est votre choix ? : "))

if choix != "1" and choix != "2":
    print("Vous avez choisi une option invalide. Veuillez relancer le programme")
    exit()  # Quitter le programme

print(f"Vous avez choisi l'option {choix}. Nous allons commencer la conversion")

if choix == "1":
    print("Vous avez choisi la conversion de pouce vers centimetre")
    pouce = float(input("Entrez la valeur en pouce : ")) # Demande a l'user de rentrer une valeur qui est de type float
    centimetre = pouce * 2.54
    print(f"La valeur en centimetre est de {centimetre} cm")

elif choix == "2":
    print("Vous avez choisi la conversion de centimetre vers pouce")
    centimetre = float(input("Entrez la valeur en centimetre : ")) # Demande a l'user de rentrer une valeur qui est de type float
    pouce = centimetre / 2.54
    print(f"La valeur en pouce est de {pouce} pouce")

print(f"Merci d'avoir utilise notre programme {nom_user}. A bientot")
print("-----------------Fin du programme---------------------")