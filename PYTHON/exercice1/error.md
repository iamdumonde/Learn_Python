# Créer une instance de ContactManager
manager = ContactManager()

# Ajouter un contact
contact1 = Contact("John Doe", "555-1234", "johndoe@example.com")
manager.add_contact(contact1)

# Afficher les contacts
manager.display_contacts()

# Mettre à jour un contact
manager.update_contact("John Doe", "555-5678", "johndoe@example.com")

# Supprimer un contact
manager.delete_contact("John Doe")












Ce code définit deux classes : `Contact` et `ContactManager`. Voici une explication de chaque partie :

1. **La classe `Contact` :**
   ```python
   class Contact:
       def __init__(self, name, phone_number, email):
           self.name = name
           self.phone_number = phone_number
           self.email = email
   ```
   - La classe `Contact` est une classe simple qui représente un contact avec trois attributs : `name` (nom), `phone_number` (numéro de téléphone) et `email` (adresse e-mail).
   - Le constructeur `__init__` est appelé lors de la création d'une nouvelle instance de la classe `Contact` et initialise les attributs de l'objet avec les valeurs fournies en argument.

2. **La classe `ContactManager` :**
   ```python
   class ContactManager:
       def __init__(self):
           self.contacts = []

       def add_contact(self, contact):
           self.contacts.append(contact)

       def display_contacts(self):
           for contact in self.contacts:
               print(f"Name: {contact.name}, Phone Number: {contact.phone_number}, Email: {contact.email}")

       def update_contact(self, name, phone_number, email):
           for contact in self.contacts:
               if contact.name == name:
                   contact.phone_number = phone_number
                   contact.email = email

       def delete_contact(self, name):
           for contact in self.contacts:
               if contact.name == name:
                   self.contacts.remove(contact)
   ```
   - La classe `ContactManager` gère une liste de contacts.
   - Le constructeur `__init__` initialise la liste de contacts à une liste vide lorsqu'une nouvelle instance de `ContactManager` est créée.
   - La méthode `add_contact` ajoute un contact à la liste des contacts.
   - La méthode `display_contacts` affiche les détails de chaque contact dans la liste.
   - La méthode `update_contact` prend un nom, un numéro de téléphone et une adresse e-mail en argument et met à jour les informations du contact correspondant dans la liste.
   - La méthode `delete_contact` prend un nom en argument et supprime le contact correspondant de la liste.

Ces classes sont conçues pour gérer des contacts, permettant d'ajouter, d'afficher, de mettre à jour et de supprimer des contacts.



import contact_manager

# Créer une instance de ContactManager
manager = contact_manager.ContactManager()

# Ajouter un contact
contact1 = contact_manager.Contact("John Doe", "555-1234", "johndoe@example.com")
manager.add_contact(contact1)

# Afficher les contacts
manager.display_contacts()

# Mettre à jour un contact
manager.update_contact("John Doe", "555-5678", "johndoe@example.com")

# Supprimer un contact
manager.delete_contact("John Doe")
