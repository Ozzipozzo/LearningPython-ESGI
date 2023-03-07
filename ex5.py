pSeuil = 2.3
vSeuil = 7.41

pression = float(input("Entrez une pression : "))
volume = float(input("Entrez un volume : "))

if pression > pSeuil and volume > vSeuil:
    print("Arrêt immédiat")
elif pression > pSeuil:
    choix = str(input("La pression est trop élevée, augmentez le volume de l'enceinte ? (o/n)"))
    if choix == "o":
        print("Merci d'augmenter le volume de l'enceinter")
    else:
        print("Arrêt immédiat")
elif volume > vSeuil:
    choix = str(input("Le volume est trop élevée, diminiuez le volume ? (o/n)"))
    if choix == "o":
        print("Merci de diminuez le volume de l'enceinte")
    else:
        print("Arrêt immédiat")
else:
    print("La pression et le volume sont bonnes")
