mail = "abdallah@gmail.com"

def verif_mail(string):
    if '@' in string and '.' in string:
        last_dot = string.rfind('.')
        extension = string[last_dot+1:]
        if len(extension) <= 3:
            return print("c'est un mail")
    return print("c'est n'est pas un mail")

verif_mail(mail)