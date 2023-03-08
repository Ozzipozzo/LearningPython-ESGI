def somme(a, b, c):
    return a + b + c

nombres = (2, 5, 8)
resultat = somme(*nombres)
print("La somme des nombres", nombres, "est", resultat)
