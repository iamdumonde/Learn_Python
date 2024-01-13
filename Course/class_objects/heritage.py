class Faune:
    def __init__(self, animal, region):
        self.animal = animal
        self.region = region
    
    def affiche_faune(self):
        print(f"La faune de {self.region} est caractérisé par des {self.animal}")

class Animal(Faune):
    def __init__(self, animal, region, nom, category):
        super().__init__(animal, region)
        self.nom = nom
        self.category = category
        
    def affiche_animal(self):
        print(f"Ceci est un {self.category}. Il s'appelle {self.nom} .")
        
        
class Chien(Animal, Faune):
    def __init__(self, nom, category, poids, race, animal, region):
        super().__init__(animal, region, nom, category)
        # super().__init__(animal, region)
        self.poids = poids
        self.race = race
        
    def affiche_animal(self):
        super().affiche_faune()
        super().affiche_animal()
    
chien = Chien('Rex', 'Carnivore', 25, 'Berger', 'Griffes', 'Parakou')
print(chien.nom)
print(chien.category)
print(chien.poids)
print(chien.race)
print(chien.animal)
print(chien.region)
print(chien.affiche_animal())