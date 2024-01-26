import mysql.connector
from mysql.connector import Error

class BaseDeDonnees:
    def __init__(self, database, host, user, password):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        
            
    def connect(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password
        )
        
        
        try:
            self.mycursor = self.connection.cursor()
            ## Requête de création de la base de données 
            self.mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.database}")
            ## Requête de création de la table Produit
            self.requete_produits = "CREATE TABLE IF NOT EXISTS produits (id INT AUTO_INCREMENT PRIMARY KEY,  Nom VARCHAR(255), Prix FLOAT)"
            self.requete_paniers = "CREATE TABLE IF NOT EXISTS paniers (id INT AUTO_INCREMENT PRIMARY KEY, produit_id INT, FOREIGN KEY(produit_id) REFERENCES produits(id), quantite INT, total FLOAT)"
            self.mycursor.execute(f"USE {self.database}")
            self.mycursor.execute(self.requete_produits)
            self.mycursor.execute(self.requete_paniers)
            self.connection.commit()
            print("Base de données et tables créées avec succès .\n") 
                        
        except Error as e:
            print(e)
        
        return self.connection
    
    
    
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            print("Connexion fermée")
        
    
            
        
