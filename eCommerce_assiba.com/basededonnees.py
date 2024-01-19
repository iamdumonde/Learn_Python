import mysql.connector
from mysql.connector import errors
from produit import Produit

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
                produit_id INT,
                quantite INT,
                FOREIGN KEY (produit_id) REFERENCES Produits(id)
            )""")
        #
        cursor.execute("""CREATE TABLE IF NOT EXISTS LigneFacture (
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

        # Requête SQL pour supprimer un produit par son nom
        affected_rows = cursor.execute("DELETE FROM Produits WHERE nom = %s", (produit_nom,))

        if affected_rows == 0:
            #aucune ligne n'a été affectée le produit n'existe pas
            print(f"Le produit avec le nom '{produit_nom}' n'existe pas dans la base de donnée !")
        else: 
            # Validation de la transaction
            connection.commit()
            print(f"Le produit '{produit_nom}' successfull deleted !")

        # Fermeture du curseur et de la connexion
        cursor.close()
        connection.close()  
       
       
       
