from datetime import date

class Commande:
    def __init__(self, date_commande: date, numero: str, prix: float = 0):
        self._date_commande = date_commande
        self._numero = numero
        self._prix = prix
        
    def get_date_commande(self) -> date:
        return self._date_commande
    
    def set_date_commande(self, date_commande: date):
        self._date_commande = date_commande
        
    def get_numero(self) -> str:
        return self._numero
    
    def set_numero(self, numero: str):
        self._numero = numero
        
    def get_prix(self) -> float:
        return self._prix
    
    def set_prix(self, prix: float):
        self._prix = prix
        
    def calcul_TVA(self) -> float:
        return self._prix * 0.196
    
    def acquitter(self) -> 'CommandeAcquittee':
        return CommandeAcquittee(self._date_commande, self._numero, self._prix)
    
    def __add__(self, other: 'Commande') -> 'Commande':
        nouveau_numero = max(int(self._numero), int(other.get_numero())) + 1
        nouvelle_date = date.today()
        nouveau_prix = self._prix + other.get_prix()
        return Commande(nouvelle_date, str(nouveau_numero), nouveau_prix)
    
    def __str__(self) -> str:
        return f"Commande {self._numero} du {self._date_commande} d'un montant de {self._prix} euros"


class CommandeAcquittee(Commande):
    def __init__(self, date_commande: date, numero: str, prix: float = 0, date_paiement: date = date.today()):
        super().__init__(date_commande, numero, prix)
        self._date_paiement = date_paiement
        
    def get_date_paiement(self) -> date:
        return self._date_paiement
    
    def set_date_paiement(self, date_paiement: date):
        self._date_paiement = date_paiement
    
    def acquitter(self) -> 'CommandeAcquittee':
        return self
    
    def __str__(self) -> str:
        if self._date_paiement:
            date_paiement_str = str(self._date_paiement)
        else:
            date_paiement_str = "non acquittée"
        return f"Commande {self._numero} du {self._date_commande} d'un montant de {self._prix} euros, acquittée le {date_paiement_str}"

class Client:
    def __init__(self, nom: str, adresse: str):
        self.nom = nom
        self.adresse = adresse

    def contacter(self) -> str:
        return f"Contacter le client {self.nom} à l'adresse {self.adresse}"

commande1 = Commande("20/03/2023", "001", 102.90)
commande2 = Commande("20/03/2023", "002", 59.90)
both_commande = commande1.__add__(commande2)
commande_paid = CommandeAcquittee(commande1.get_date_commande(), commande1.get_numero(), commande1.get_prix(), date.today())
commande1.acquitter()
print(both_commande)

client1 = Client("GAMBLER", "10 rue naxator 93 Sevran")
print(client1.contacter())