while True:
    num = input("Veuillez saisir un nombre en 1 et 10 : ")
    try:
        num = int(num)
        if 1 <= num <= 10:
            break
        else:
            print("Mauvaise saisie, il n'est pas entre 1 et 10")
    except ValueError:
        print("Le nombre n'est pas un entier")
print("Vous avez saisie :", num)