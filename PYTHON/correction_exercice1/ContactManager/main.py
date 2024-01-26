# Importation des classes Contact et ContactManager à partir de fichiers externes
from contact import Contact
from contact_manager import ContactManager

# Fonction principale du programme
def main():
    # Création d'une instance de ContactManager en spécifiant le fichier CSV 'database.csv' pour stocker les contacts
    manager = ContactManager('database.csv')

    while True:
        # Affichage du menu principal du gestionnaire de contacts
        print("\nGestionnaire de Contacts")
        print("1. Ajouter un nouveau contact")
        print("2. Afficher tous les contacts")
        print("3. Mettre à jour un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        # L'utilisateur choisit une option du menu
        choix = input("Choisissez une option : ")

        if choix == "1":
            # Ajout d'un nouveau contact
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            telephone = input("Téléphone : ")
            email = input("Email : ")
            if not manager.contact_existe(email):
                # Vérification que le contact n'existe pas déjà par son email
                contact = Contact(nom, prenom, telephone, email)
                manager.ajouter_contact(contact)
                print("Contact ajouté avec succès!")
            else:
                print("Un contact avec cet email existe déjà.")

        elif choix == "2":
            # Affichage de tous les contacts
            manager.afficher_contacts()

        elif choix == "3":
            # Mise à jour d'un contact par son email
            email = input("Email du contact à mettre à jour : ")
            if manager.contact_existe(email):
                new_nom = input("Nouveau nom : ")
                new_prenom = input("Nouveau prénom : ")
                new_telephone = input("Nouveau téléphone : ")
                new_email = input("Nouvel email : ")
                new_contact = Contact(new_nom, new_prenom, new_telephone, new_email)
                manager.mettre_a_jour_contact(email, new_contact)
                print("Contact mis à jour avec succès!")
            else:
                print("Aucun contact avec cet email n'a été trouvé.")

        elif choix == "4":
            # Suppression d'un contact par son email
            email = input("Email du contact à supprimer : ")
            if manager.contact_existe(email):
                manager.supprimer_contact(email)
                print("Contact supprimé avec succès!")
            else:
                print("Aucun contact avec cet email n'a été trouvé.")

        elif choix == "5":
            # Sortie du programme si l'utilisateur choisit de quitter
            break

if __name__ == "__main__":
    main()
