email = input("Saisir une adresse email : ")

if "@" in email and email.endswith(".com"):
    print("Adresse mail valide")
else:
    print("Ce n'est pas une adresse email")