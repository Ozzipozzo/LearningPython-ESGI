x = int(input("Entrez le nombre de chaînes à enregistrer : "))

with open('data.txt', 'w') as f:
    for i in range(x):
        chaine = input(f"Entrez la chaîne {i+1} : ")
        f.write(chaine + '\n')

print(f"Les {x} chaînes de caractères ont été enregistrées dans le fichier 'data.txt'.")
