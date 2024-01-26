from BaseDeDonnees import BaseDeDonnees
from Produit import Produit
from QueryExecutor import QueryExecutor

def main():
    
    ## Instanciation de BaseDeDonnees
    db = BaseDeDonnees("Ecommerce", "localhost", "root", "")
    connection = db.connect()
    
    query_executor = QueryExecutor(connection)
    
    while True:
        ## Demander le choix à l'utilisateur
        print("\nProjet E-Commerce")
        print("1-Créer un produit")
        print("2- Afficher les produits disponibles")
        print("3- Ajouter un produit au panier avec une quantité spécifiée")
        print("4- Imprimer la facture en format CSV")
        print("5- Quitter")
        
        choix = input("\nChoisissez une option : ")
        
        while choix.isdigit() == False:
            choix = input("\nChoisissez une option :")
        
        
        
        if choix == "1":
            
            produit_nom = input("\nEntrez le nom du produit : ")
            produit_prix = int(input("Entrez le prix : "))
            
            ##Instanciation de la classe Produit
            new_produit = Produit(produit_nom, produit_prix)
            
            # Ajout d'un produit en base de donnée
            query_executor.add_produit(new_produit)
            
        if choix == "2":
            query_executor.show_produit()
            
        
        if choix == "3":
            print("Liste des produits :")
            query_executor.show_produit()
            
            
            id = int(input("\nInsérer l'id du produit : "))
            quantite = int(input("Veuillez entrer une quantité : "))
            query_executor.add_panier(id, quantite)
            
        if choix == "4":
            query_executor.facture()
            
        if choix == "5":
            db.close()
            break
    
main()