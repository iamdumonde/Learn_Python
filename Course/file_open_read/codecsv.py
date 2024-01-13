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