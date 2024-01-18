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

    def maj_contact(self, ancien_nom, ancien_prenom, nouveau_nom, nouveau_prenom, nouveau_numero, nouveau_email):
        contact_trouve = False
        for contact in self.contacts:
            if contact.nom == ancien_nom and contact.prenom == ancien_prenom:
                contact.nom = nouveau_nom
                contact.prenom = nouveau_prenom
                contact.numero = nouveau_numero
                contact.email = nouveau_email
                contact_trouve = True
        if contact_trouve:
            self.sauvegarderincsv()
            print("Mise à jour réussie")
        else:
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
                    new_contact = Contact(row['Nom'], row['Prenom'], row['Numero'], row['Email'])
                    self.contacts.append(new_contact)
        except FileNotFoundError:
            print(f"File '{self.basename}' introuvable.")
    
    def supprimer_all_contact(self):
        with open(self.basename, 'w', newline=''):
            pass