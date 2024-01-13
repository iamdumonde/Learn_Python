import csv
from contact import Contact


class ContactManager:
    def __init__(self, basename):
        self.contacts = []
        self.basename = basename
        self.chargement_basename()

    def ajout_contact(self, contact):
        self.contacts.append(contact)
        self.sauvegarderincsv()
        print("Ajout de contact réussi !")

    def affiche_contacts(self):
        if not self.contacts:
            print("Pas de contacts !")
        else:
            for contact in self.contacts:
                print(contact)

    def maj_contact(self, nom, prenom, numero, email):
        for contact in self.contacts:
            if contact.nom == nom and contact.prenom == prenom:
                contact.numero = numero
                contact.email = email
                self.sauvegarderincsv()
                print("Mise à jour réussi")
                return
        print("Contact non trouvé.")

    def suppr_contact(self, nom, prenom):
        for contact in self.contacts:
            if contact.nom == nom and contact.prenom == prenom:
                self.contacts.remove(contact)
                self.sauvegarderincsv()
                print("Contact supprimé")
                return
        print("Contact non trouvé")
    
    def sauvegarderincsv(self):
            with open(self.basename, 'w', newline='') as csvfile:
                fieldnames = ['Nom', 'Prenom', 'Numero', 'Email']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for contact in self.contacts:
                    writer.writerow({'Nom': contact.nom,
                                    'Prenom': contact.prenom,
                                    'Numero': contact.numero,
                                    'Email': contact.email})
                    
    def chargement_basename(self):
        # Charge les contacts depuis le fichier CSV
        try:
            with open(self.basename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_contact = Contact(row['Nom'], row['Prénom'], row['Numéro'], row['Email'])
                    self.contacts.append(new_contact)
        except FileNotFoundError:
            print(f"File '{self.basename}' introuvable.")
    
    def supprimer_all_contact(self):
        with open(self.basename, 'w', newline=''):
            pass