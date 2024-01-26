import csv

#Créer un fichier csv simple et le lire
donnees = [['Nom', 'Age', 'Ville'], ['Alice', 25, 'Paris'], ['Bob', 30, 'Londres']]

# Ecriture dans un fichier CSV
with open('donnees.csv', 'w', newline='') as fichier_csv:
    writer = csv.writer(fichier_csv)
    writer.writerows(donnees)
    
# Lecture d'un fichier CSV
with open('donnees.csv', 'r') as fichier_csv:
    lecteur = csv.reader(fichier_csv)
    for ligne in lecteur:
        print(ligne)
        
        
with open(self.basename, 'w', newline='') as csvfile:
                fieldnames = ['Nom', 'Prenom', 'Numero', 'Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow({'Nom': contact.nom,
                                    'Prenom': contact.prenom,
                                    'Numero': contact.numero,
                                    'Email': contact.email})