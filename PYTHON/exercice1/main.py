from contact_manager import ContactManager
from contact import Contact

def main():
    #nom du fichier csv
    basename = "basededonnees.csv"
    contact_manager = ContactManager(basename)
    
    while True:
        print("\nMenu")
        print("1. Ajouter un nouveau contact")
        print("2. Afficher tous les contacts")
        print("3. Mise à jour du contact")
        print("4. Supprimer le contact")
        print("5. Quitter")
    
        choice = input("Faites un choix : ")

        if choice == '1':
            nom = input("Entrer votre nom : ")
            prenom = input("Entrer votre prenom : ")
            numero = input("Entrer un numéro : ")
            email = input("Entrer votre email : ")
            
            new_contact = Contact(nom, prenom, numero, email)
            
            contact_manager.ajout_contact(new_contact)
            
        elif choice == '2':
            contact_manager.affiche_contacts()
            
        elif choice == '3':
            ancien_nom = input("Entrer l'ancien nom du contact :  ")
            ancien_prenom = input("Entrer l'ancien prenom du contact :  ")
            nouveau_nom = input("Entrer le nouveau nom du contact :  ")
            nouveau_prenom = input("Entrer le nouveau prenom du contact :  ")
            nouveau_numero = input("Entrer le nouveau numéro du contact :  ")
            nouveau_email = input("Entrer le nouvel email du contact :  ")
            contact_manager.maj_contact(ancien_nom, ancien_prenom, nouveau_nom, nouveau_prenom, nouveau_numero, nouveau_email)

        elif choice == '4':
            nom = input("Entrez le nom du contact à supprimer : ")
            prenom = input("Entrez le prenom du contact à supprimer : ")
            contact_manager.suppr_contact(nom, prenom)
        
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()