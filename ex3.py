import math

x = float(input("Entrez un nombre : "))

if x >= 0:
    racine = math.sqrt(x)
    print("La racine carrée de", x, "est", racine)
else:
    print("Erreur : le nombre doit être positif ou nul")
