from basededonnees import BaseDeDonnees
from produit import Produit

def main():
    #Instance de la base de donnée
    bdd = BaseDeDonnees('127.0.0.1', 'root', '', 'assiba_database')
    bdd.getConnectedtodb()
    
    
    #Menu
    while True:
        print("\nMenu")
        print("1. Créer un produit")
        print("2. Supprimer un produit")
        print("3. Afficher les produits disponibles")
        print("4. Créer un panier")
        print("5. Ajouter un produit au panier avec une quantité spécifiée")
        print("6. Imprimer la facture en format CSV")
        print("7. Quitter")
        
        makeChoice = input("Que voulez-vous faire ?\nEntrez le numéro correspondant à votre choix : ")
        
        if makeChoice == '1':
            nom = input("Entrez le nom du produit : ")
            prix = float(input("Entrez le prix du produit : "))
            nouveau_produit = Produit(id=None, nom = nom, prix = prix)
            bdd.ajouterProduit(nouveau_produit)
            print("Produit ajouté successfully")
            
        elif makeChoice == '2':
            nom = input("Entrez le nom du produit à supprimer : ")
            bdd.supprimerProduit(nom)
            
        elif makeChoice == '3':
            bdd.afficheTousProduits()
            
        elif makeChoice == '4':
            panier_id = bdd.creerPanier()
            print(f"Panier créé avec ID {panier_id}")
            
        
        elif makeChoice == "7":
            print("Au revoir !")
            break
        
        else:
            print("Choix invalide. Veuillez entrer un numéro de choix valide !")
        

    
if __name__ == "__main__":
    main()