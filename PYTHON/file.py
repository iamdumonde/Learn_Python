# import csv

# donnees = [['Nom', 'Age', 'Ville'], ['Alice', 25, 'Paris'], ['Bob', 30, 'Londres']]

# with open('donnees.csv', 'w', newline='') as fichier_csv:
#     writer = csv.writer(fichier_csv)
#     writer.writerows(donnees)


# with open('donnees.csv', 'r') as fichier_csv:
#     lecteur = csv.reader(fichier_csv)
#     for ligne in lecteur:
#         print(ligne)

# try:
#     print('Tola bola')
# except:
#     print('Error')
#     raise 
# else:
#     print('next execution')
# finally:
#     print('De toute façon je serai executé')
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
        print(f"Ceci est un {self.category}. Il s'appelle {self.nom}")


class Chien(Animal , Faune ):
    def __init__(self, nom, category, poids, race, animal, region):
        super().__init__(animal, region, nom, category, )
        # super().__init__(animal, region)
        self.poids = poids
        self.race = race

    def affiche_animal(self):
        super().affiche_faune()
        super().affiche_animal()


chien = Chien('Rex', 'Homnivore', 5.0, 'Berger', 'Chien','Allemagne')
print(chien.nom)
print(chien.category)
print(chien.poids)
print(chien.race)
chien.affiche_animal()











