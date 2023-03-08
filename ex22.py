with open('data.txt', 'r') as f:
    for ligne in f:
        ligne = ligne.strip()
        if '@' in ligne and ligne.endswith('.com'):
            print(f"{ligne} est un email valide.")
        else:
            print(f"{ligne} n'est pas un email valide.")
