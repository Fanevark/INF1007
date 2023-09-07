#!/usr/bin/python3
# Voici un petit script qui vous permettra de découvrir l'outil de débogage de VSCode ou PyCharm 

# Concept que vous allez voir plus loin dans la session. 
# Permet d'utiliser la liste de mots du fichier word_list.py 
from liste_mots import word_list, cherche_mot_commence_par

while True:
    nom: str = input("Quel est votre nom ?")
    print(f"Bonjour {nom} !")
    
    compteur_de_letres = 0


    # Un mot pour chacune des lettres de votre nom sera affiché
    for lettre in nom:
        if cherche_mot_commence_par(lettre) is not None:
            print(f"{lettre} comme dans {cherche_mot_commence_par(lettre)}")
        else:
            print(f"{lettre} comme dans ... euh ... {lettre}")