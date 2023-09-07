# Ce fichier n'est uniquement composé que d'une liste de mots pour chacune des lettres de l'alphabet
# Il est utilisé par le script to_debug.py, il n'est pas nécessaire de le modifier


liste_de_mots = [
  "alphabet",
  "dinosaure",
  "elephant",
  "fleur",
  "hamburger",
  "igloo",
  "loup",
  "maman",
  "nourriture",
  "oiseau",
  "papa",
  "quitter",
  "souris",
  "tortue",
  "uniforme",
  "wagon",
  "xylophone",
  "zoo",
]

# Concepts vus plus tard dans la session, vous n'avez pas à les comprendre
def cherche_mot_commence_par(lettre: str):
    for mot in liste_de_mots:
        if mot.startswith(lettre):
            return mot 
