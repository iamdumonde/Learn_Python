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
        print("5. Supprimer tous les contacts")
        print("6. Quitter")
    
        choice = input("Faites un choix : ")

        if choice == '1':
            nom = input("Entrer votre nom : ")
            prenom = input("Entrer votre prenom : ")
            numero = input("Entrer un numéro : ")
            email = input("Entrer votre email : ")
            
            new_contact = Contact(nom, prenom, numero, email)
            
            contact_manager.ajout_contact(new_contact)
        
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()