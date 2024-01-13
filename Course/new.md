Bien sûr, pour stocker les données dans un fichier CSV, vous pouvez ajouter des méthodes dans la classe `ContactManager` pour sauvegarder et charger les contacts à partir d'un fichier CSV. Voici une mise à jour du code :



class Contact:
    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Phone: {self.phone_number}, Email: {self.email}"

### contact_manager.py
```python
import csv
from contact import Contact

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, first_name, last_name, phone_number, email):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                contact.phone_number = phone_number
                contact.email = email
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'First Name': contact.first_name,
                                 'Last Name': contact.last_name,
                                 'Phone Number': contact.phone_number,
                                 'Email': contact.email})

    def load_from_csv(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_contact = Contact(row['First Name'], row['Last Name'], row['Phone Number'], row['Email'])
                self.contacts.append(new_contact)
```

### main.py
```python
from contact_manager import ContactManager
from contact import Contact

def main():
    contact_manager = ContactManager()

    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Save contacts to CSV")
        print("6. Load contacts from CSV")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            new_contact = Contact(first_name, last_name, phone_number, email)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.update_contact(first_name, last_name, phone_number, email)

        elif choice == '4':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contact_manager.delete_contact(first_name, last_name)

        elif choice == '5':
            filename = input("Enter the filename to save contacts to (e.g., contacts.csv): ")
            contact_manager.save_to_csv(filename)

        elif choice == '6':
            filename = input("Enter the filename to load contacts from (e.g., contacts.csv): ")
            contact_manager.load_from_csv(filename)

        elif choice == '7':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
```

Avec ces modifications, vous pouvez sauvegarder les contacts dans un fichier CSV et les charger à partir d'un fichier CSV en utilisant les options du menu. Vous devrez créer les fichiers CSV avant d'utiliser l'option de chargement.


Dans ce cas, vous pouvez modifier la classe `ContactManager` pour utiliser un fichier CSV unique pour stocker tous les contacts. Chaque fois que vous ajoutez, mettez à jour ou supprimez un contact, la classe gérera ces opérations dans le même fichier CSV. Voici une mise à jour du code :

### contact_manager.py
```python
import csv
from contact import Contact

class ContactManager:
    def __init__(self, filename):
        self.contacts = []
        self.filename = filename
        self.load_from_csv()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_to_csv()
        print("Contact added successfully.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, first_name, last_name, phone_number, email):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                contact.phone_number = phone_number
                contact.email = email
                self.save_to_csv()
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                self.save_to_csv()
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def save_to_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'First Name': contact.first_name,
                                 'Last Name': contact.last_name,
                                 'Phone Number': contact.phone_number,
                                 'Email': contact.email})

    def load_from_csv(self):
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_contact = Contact(row['First Name'], row['Last Name'], row['Phone Number'], row['Email'])
                    self.contacts.append(new_contact)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new file.")

    def clear_csv(self):
        with open(self.filename, 'w', newline='') as csvfile:
            pass
```

### main.py
```python
from contact_manager import ContactManager
from contact import Contact

def main():
    filename = "contacts.csv"  # Vous pouvez changer le nom du fichier ici
    contact_manager = ContactManager(filename)

    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Clear all contacts (start fresh)")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            new_contact = Contact(first_name, last_name, phone_number, email)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.update_contact(first_name, last_name, phone_number, email)

        elif choice == '4':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contact_manager.delete_contact(first_name, last_name)

        elif choice == '5':
            confirm = input("Are you sure you want to clear all contacts? (y/n): ")
            if confirm.lower() == 'y':
                contact_manager.clear_csv()
                print("All contacts cleared.")
            else:
                print("Operation cancelled.")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```

Avec ces modifications, l'application utilise un fichier CSV unique (`contacts.csv` par défaut) pour stocker tous les contacts. Vous pouvez ajouter, mettre à jour, supprimer, et même effacer tous les contacts avec les options du menu. Les changements seront reflétés directement dans le fichier CSV.


Je m'excuse pour le malentendu. Voici le code avec des commentaires expliquant chaque ligne :

### contact_manager.py
```python
import csv
from contact import Contact

class ContactManager:
    def __init__(self, filename):
        self.contacts = []
        self.filename = filename
        self.load_from_csv()

    def add_contact(self, contact):
        # Ajoute un contact à la liste et sauvegarde dans le fichier CSV
        self.contacts.append(contact)
        self.save_to_csv()
        print("Contact added successfully.")

    def display_contacts(self):
        # Affiche tous les contacts dans la liste
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def update_contact(self, first_name, last_name, phone_number, email):
        # Met à jour les informations d'un contact et sauvegarde dans le fichier CSV
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                contact.phone_number = phone_number
                contact.email = email
                self.save_to_csv()
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, first_name, last_name):
        # Supprime un contact de la liste et sauvegarde dans le fichier CSV
        for contact in self.contacts:
            if contact.first_name == first_name and contact.last_name == last_name:
                self.contacts.remove(contact)
                self.save_to_csv()
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def save_to_csv(self):
        # Sauvegarde tous les contacts dans le fichier CSV
        with open(self.filename, 'w', newline='') as csvfile:
            fieldnames = ['First Name', 'Last Name', 'Phone Number', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for contact in self.contacts:
                writer.writerow({'First Name': contact.first_name,
                                 'Last Name': contact.last_name,
                                 'Phone Number': contact.phone_number,
                                 'Email': contact.email})

    def load_from_csv(self):
        # Charge les contacts depuis le fichier CSV
        try:
            with open(self.filename, 'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    new_contact = Contact(row['First Name'], row['Last Name'], row['Phone Number'], row['Email'])
                    self.contacts.append(new_contact)
        except FileNotFoundError:
            print(f"File '{self.filename}' not found. Creating a new file.")

    def clear_csv(self):
        # Efface le contenu du fichier CSV
        with open(self.filename, 'w', newline=''):
            pass  # Ne fait rien, juste pour effacer le contenu du fichier
```

### main.py
```python
from contact_manager import ContactManager
from contact import Contact

def main():
    filename = "contacts.csv"  # Vous pouvez changer le nom du fichier ici
    contact_manager = ContactManager(filename)

    while True:
        print("\nMenu:")
        print("1. Add a new contact")
        print("2. Display all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Clear all contacts (start fresh)")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email address: ")
            new_contact = Contact(first_name, last_name, phone_number, email)
            contact_manager.add_contact(new_contact)

        elif choice == '2':
            contact_manager.display_contacts()

        elif choice == '3':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email address: ")
            contact_manager.update_contact(first_name, last_name, phone_number, email)

        elif choice == '4':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            contact_manager.delete_contact(first_name, last_name)

        elif choice == '5':
            confirm = input("Are you sure you want to clear all contacts? (y/n): ")
            if confirm.lower() == 'y':
                contact_manager.clear_csv()
                print("All contacts cleared.")
            else:
                print("Operation cancelled.")

        elif choice == '6':
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```

J'espère