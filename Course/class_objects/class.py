class Chien:
    # Constructors (__init__)
    #self, est considéré comme this. en js
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def aboyer(self):
        print("Woof!")
        
# Création d'un objet de la classe Chien
mon_chien = Chien("Rex", 3)
print(mon_chien.aboyer())
print(mon_chien.nom)
print(mon_chien)