class Contact:
    def __init__(self, nom, prenom, numero, email):
        self.nom = nom
        self.prenom = prenom
        self.numero = numero
        self.email = email
        
    def affiche_info(self):
        print(f"Nom: {self.nom}, Prénom: {self.prenom}, Numéro : {self.numero}, Email : {self.email}")