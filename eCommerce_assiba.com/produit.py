from typing import Optional

class Produit:
    def __init__(self, id:int, nom: str, prix: float ):
        self.id = id
        self.nom = nom
        self.prix = prix
        
    def __str__(self):
        pass