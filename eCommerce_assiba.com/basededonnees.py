import mysql.connector

class BaseDeDonnees:
    def __init__(self, host, user, password):
        self.host = host,
        self.user = user,
        self.password = password
        
    def getConnectedtodb(self):
        mysqldb = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = ""
        )
        print(mysqldb)
       
       
       
       
       
       
       
       
        
# db = BaseDeDonnees("localhost", "root", "root")
# print