import csv

class ContactManager:
    def __init__(self, csv_file):
        # Le constructeur de la classe ContactManager prend un fichier CSV en argument
        # et initialise l'attribut csv_file pour stocker le nom du fichier.
        self.csv_file = csv_file

    def ajouter_contact(self, contact):
        # Cette méthode permet d'ajouter un contact au fichier CSV.
        with open(self.csv_file, mode='a', newline='') as file:
            # Ouvre le fichier CSV en mode d'ajout ('a') pour ajouter des contacts à la fin.
            writer = csv.writer(file)  # Crée un objet writer pour écrire dans le fichier CSV.
            writer.writerow([contact.nom, contact.prenom, contact.telephone, contact.email])
            # Écrit une nouvelle ligne dans le fichier CSV avec les informations du contact.

    def afficher_contacts(self):
        # Cette méthode permet d'afficher tous les contacts du fichier CSV.
        with open(self.csv_file, mode='r') as file:
            # Ouvre le fichier CSV en mode lecture ('r').
            reader = csv.reader(file)  # Crée un objet reader pour lire le fichier CSV.
            for row in reader:
                # Parcourt chaque ligne du fichier CSV.
                print(f"Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}, Email: {row[3]}")
                # Affiche les informations de chaque contact.

    def mettre_a_jour_contact(self, email, new_contact):
        # Cette méthode permet de mettre à jour les informations d'un contact par son adresse email.
        with open(self.csv_file, mode='r') as file:
            # Ouvre le fichier CSV en mode lecture ('r').
            reader = csv.reader(file)  # Crée un objet reader pour lire le fichier CSV.
            rows = list(reader)  # Lit toutes les lignes du fichier et les stocke dans une liste.

        with open(self.csv_file, mode='w', newline='') as file:
            # Ouvre le fichier CSV en mode écriture ('w') pour mettre à jour les informations.
            writer = csv.writer(file)  # Crée un objet writer pour écrire dans le fichier CSV.
            for row in rows:
                if row[3] == email:
                    # Si l'adresse email correspond à celle du contact à mettre à jour.
                    writer.writerow([new_contact.nom, new_contact.prenom, new_contact.telephone, new_contact.email])
                    # Écrit les nouvelles informations du contact.
                else:
                    writer.writerow(row)
                    # Écrit les informations inchangées des autres contacts.

    def supprimer_contact(self, email):
        # Cette méthode permet de supprimer un contact par son adresse email.
        with open(self.csv_file, mode='r') as file:
            # Ouvre le fichier CSV en mode lecture ('r').
            reader = csv.reader(file)  # Crée un objet reader pour lire le fichier CSV.
            rows = list(reader)  # Lit toutes les lignes du fichier et les stocke dans une liste.

        with open(self.csv_file, mode='w', newline='') as file:
            # Ouvre le fichier CSV en mode écriture ('w') pour supprimer le contact.
            writer = csv.writer(file)  # Crée un objet writer pour écrire dans le fichier CSV.
            for row in rows:
                if row[3] != email:
                    # Si l'adresse email ne correspond pas à celle du contact à supprimer.
                    writer.writerow(row)
                    # Réécrit les informations des contacts non supprimés.

    def contact_existe(self, email):
        # Cette méthode permet de vérifier si un contact existe dans le fichier CSV par son adresse email.
        with open(self.csv_file, mode='r') as file:
            # Ouvre le fichier CSV en mode lecture ('r').
            reader = csv.reader(file)  # Crée un objet reader pour lire le fichier CSV.
            for row in reader:
                if row[3] == email:
                    # Si l'adresse email correspond à celle d'un contact existant.
                    return True  # Retourne True pour indiquer que le contact existe.
        return False  # Retourne False si le contact n'existe pas.



# L'importation du module CSV est nécessaire car il est utilisé dans ce code pour lire et écrire des fichiers CSV. Le module CSV est une bibliothèque Python standard qui offre des fonctionnalités pour travailler avec des fichiers CSV, qui sont couramment utilisés pour stocker des données tabulaires, telles que les informations de contacts dans ce cas.

# Le module CSV fournit des classes et des méthodes pour lire des fichiers CSV, écrire des données dans des fichiers CSV et effectuer des opérations telles que la lecture de lignes, l'écriture de lignes, le traitement de valeurs séparées par des virgules, etc