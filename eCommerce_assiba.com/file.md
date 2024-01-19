Vous pouvez définir des méthodes supplémentaires dans votre classe BaseDeDonnees pour exécuter des requêtes SQL et récupérer les résultats. Par exemple, vous pouvez définir une méthode execute_query qui prend une requête SQL en paramètre et retourne le résultat de la requête sous forme de jeu de résultats.

Voici un exemple de définition de la méthode execute_query :

Copy code
import mysql.connector

class BaseDeDonnees:
    def __init__(self, host, user, password):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )

    def execute_query(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
Vous pouvez ensuite utiliser cette méthode pour exécuter des requêtes SQL et récupérer les résultats. Par exemple :

Copy code
db = BaseDeDonnees("localhost", "yourusername", "yourpassword")
result = db.execute_query("SELECT * FROM your_table")
print(result)
Notez que dans cet exemple, la connexion à la base de données est établie lors de la création d'un objet BaseDeDonnees et est stockée dans l'attribut mydb. Vous pouvez également définir une méthode close pour fermer la connexion lorsque vous n'en avez plus besoin.

Copy code
def close(self):
    self.mydb.close()
Et n'oubliez pas de l'appeler lorsque vous avez terminé de travailler avec la base de données.

Copy code
db = BaseDeDonnees("localhost", "yourusername", "yourpassword")
result = db.execute_query("SELECT * FROM your_table")
print(result)
db.close()
Il est important de noter que cette classe est juste un exemple et peut être améliorée pour gérer les erreurs, les transactions, les requêtes préparées, etc.