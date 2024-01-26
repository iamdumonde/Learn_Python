from mysql.connector import Error
import csv


class QueryExecutor:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None
    
    ## Insérer une donnée
    def insert_requete(self, query, values):
        self.cursor = self.connection.cursor()
        
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        
        except Error as er:
            print(er)
            
        finally:
            self.cursor.close()
            
    ## Afficher une donnée
    def show_requete(self, query):
        self.cursor = self.connection.cursor()
        try:
            
            self.cursor.execute(query)
            result = self.cursor.fetchall()
            for ele in result:
                print(f"Id : {ele[0]} |Nom : {ele[1]} | Prix : {ele[2]}")
            
        except Error as er:
            print(er)
        
        finally:
            self.cursor.close()
            
    def add_panier(self, produit_id, quantite):
        self.cursor = self.connection.cursor()
        try:
            request = f"SELECT * FROM produits WHERE id = {produit_id}"    
            
            self.cursor.execute(request)
            product_price =  self.cursor.fetchone()
            
            # print(product_price[2])
            
            if product_price:
                total = product_price[2] * quantite
            
            add_panier_requete = "INSERT INTO paniers (produit_id, quantite, total) VALUES (%s, %s, %s)"
            
            values = (produit_id, quantite, total)
            
            self.insert_requete(add_panier_requete, values)
            
            print("Produit enregistré dans le panier\n")
        except Error as er:
            print(er)
        
        finally:
            self.cursor.close()
        
    def add_produit(self, produit):
       self.cursor = self.connection.cursor()
       try:
            ## Requête d'ajout d'un produit
            add_produit_requete = "INSERT INTO produits (Nom, Prix) VALUES (%s, %s)"
            
            values = (produit.nom, produit.prix)
            
            ## Exécution de la requête d'ajout du produit
            self.insert_requete(add_produit_requete, values)
            
            ## Message de succès 
            print("Produit ajouté avec succès .\n")
       except Error as er:
           print("Error:", er)
       finally:
            self.cursor.close()
    
    def show_produit(self):
        self.cursor = self.connection.cursor()
        try:
            ## Requête de récupération des produits
            show_produit_requete = "SELECT * FROM produits"
            
            ## Exécution de la requête d'ajout du produit
            self.show_requete(show_produit_requete)
        except Error as e:
            print("Error : ", e)
        finally:
            self.cursor.close()
        
    def facture(self):
        self.cursor = self.connection.cursor()
        try:
            # facture_requete = "SELECT * FROM paniers"
            # self.cursor.execute(facture_requete)
            # factures =  self.cursor.fetchall()
            requete = "SELECT produits.Nom, produits.Prix, paniers.quantite, paniers.total FROM produits INNER JOIN paniers ON produits.id = paniers.produit_id"
            self.cursor.execute(requete)
            factures =  self.cursor.fetchall()
            print(factures)
            
            with open('facture.csv', 'w', newline="") as fichier:
                fact = csv.writer(fichier)
                fact.writerows(factures)
                
        except Error as e:
            print("Error : ", e)
        finally:
            self.cursor.close()
    
    
