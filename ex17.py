mot = input("Vérifions si votre mot est un palindrome : ")

def pal(string):
    reverse_string = string[::-1]
    if reverse_string == string:
        return print("c'est un palindrome")
    else:
        return print("c'est n'est pas un palindrome")
    
pal(mot)