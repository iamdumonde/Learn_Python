import mysql.connector
from mysql.connector import errors
from produit import Produit
from panier import Panier

class BaseDeDonnees:
    def __init__(self, host, user, password,database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
    
    # connexion à la base de donnée 
    def getConnectedtodb(self):
        try:
            #connexion à la base de données si elle existe déjà
            mysqldb = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database
            )
            #la connexion réussie
            return mysqldb
        except errors.DatabaseError as e:
            if "Unknown database" in str(e):
                #si la base de donnée n'existe pas encore
                self.createBDD()

                #reconnexion à nouveau
                mysqldb = mysql.connector.connect(
                    host = self.host,
                    user = self.user,
                    password = self.password,
                    database = self.database
                )
                #connexion réussie
                return mysqldb
            else:
                #affiche d'autres erreurs
                print("Erreur : ",str(e))
            
    #création de la base de donnée
    def createBDD(self):
        #se connecter au serveur mysql sans spécification de bdd
        connection = mysql.connector.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password
        )
        
        #mise en place de l'objet cursor pour exécuter les requêtes
        cursor = connection.cursor()
        
        #requête sql pour créer la base de données
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
        
        #sélection de la bdd nouvellement créée et créé les tables
        cursor.execute(f"USE {self.database}")
        
        #création des tables "Produits" "Paniers" "LigneFacture"
        #
        cursor.execute("""CREATE TABLE IF NOT EXISTS Produits (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nom VARCHAR(255),
                prix DECIMAL(10, 2)
            )""")
        #
        cursor.execute("""CREATE TABLE IF NOT EXISTS Paniers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produit_id INT,
                quantite INT,
                FOREIGN KEY (produit_id) REFERENCES Produits(id)
            )""")
        #
        cursor.execute("""CREATE TABLE IF NOT EXISTS LigneFacture (
                id INT AUTO_INCREMENT PRIMARY KEY,
                panier_id INT,
                produit_id INT,
                quantite INT,
                prix_total DECIMAL(10, 2),
                FOREIGN KEY (panier_id) REFERENCES Paniers(produit_id),
                FOREIGN KEY (produit_id) REFERENCES Produits(id)
            )""")
        
        # Fermeture du curseur
        cursor.close()
        # Fermeture de la connexion
        connection.close()
    
    #ajout de produit à la table "Produits"
    def ajouterProduit(self, produit):
        #connexion à la bdd
        connection = self.getConnectedtodb()
        cursor = connection.cursor()
        
        #requête sql
        cursor.execute("""
            INSERT INTO Produits (nom, prix)
            VALUES (%s, %s)
        """, (produit.nom, produit.prix))
        
        #valider la transaction 
        connection.commit()
        
        #fermer le curseur et la co
        cursor.close()
        connection.close()
       
       
    #affichage de tous les produits
    def afficheTousProduits(self):
        #co bdd
        connection = self.getConnectedtodb()
        cursor = connection.cursor()
        
        #requête sql
        cursor.execute("SELECT * FROM Produits")
        
        #récupération des résultats
        produits = cursor.fetchall()
        
        # Affichage des résultats
        for produit in produits:
            print(f"ID: {produit[0]}, Nom: {produit[1]}, Prix: {produit[2]}")

        # Fermeture du curseur et de la connexion
        cursor.close()
        connection.close()
       
       
    # Supprimer un produit de la table "Produits" par son ID
    def supprimerProduit(self, produit_nom):
        # Connexion à la base de données
        connection = self.getConnectedtodb()
        cursor = connection.cursor()

        cursor.execute("SELECT COUNT(*) FROM Produits WHERE nom = %s", (produit_nom,))
        nombre_produits = cursor.fetchone()[0]
        
        if nombre_produits == 0:
        # Aucun produit avec ce nom n'a été trouvé
            print(f"Le produit avec le nom '{produit_nom}' n'existe pas dans la base de données.")
        else:
        # Le produit existe, procéder à la suppression
            cursor.execute("DELETE FROM Produits WHERE nom = %s", (produit_nom,))
            connection.commit()
            print(f"Le produit '{produit_nom}' a été supprimé avec succès !")

        # Fermeture du curseur et de la connexion
        cursor.close()
        connection.close()  
    
    #création du panier
    def creerPanier(self, produit_id, quantity):
        connection = self.getConnectedtodb()
        cursor = connection.cursor()
        
        try:
            #création d'un nouveau panier et récupération de l'id du panier
            cursor.execute("INSERT INTO Paniers (produit_id, quantity) VALUES (%s, %s)", (produit_id, quantity))
            panier_id = cursor.lastrowid
            
            connection.commit()
            print(f"Panier créé avec ID {panier_id}")
            return panier_id
        except Exception as e:
            print(f"Erreur lors de la création du panier : {e}")
            
        cursor.close()
        connection.close()
    #ajouter de produit au panier
    def ajouterProduitauPanier(self):
        pass
       
       
       
