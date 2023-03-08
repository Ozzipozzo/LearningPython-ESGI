chaine = "Le chat est sur le tapis et le chien est sous le tapis"

def compterMots(chaine):
    mots = chaine.split()
    
    freq_mots = {}
    
    for mot in mots:
        if mot not in freq_mots:
            freq_mots[mot] = 1
        else:
            freq_mots[mot] += 1
    
    return freq_mots

freq_mots = compterMots(chaine)
print(freq_mots)
