#création et manipulation
#Un dictionnaire est une structure de données qui permet de stocker des paires clé-valeur. Chaque clé doit être unique, et elle est associée
#à une valeur. Les dictionnaires sont définis avec des accolades {}

mon_dico = {'nom' : 'ABOU', 'prenom' : 'Martin', 'age' : 25, 'ville' : 'Porto-Novo'}

#accès aux éléments
nom_personne = mon_dico['nom']
mon_dico['age'] = 26

#ajout d'éléments
mon_dico['genre'] = 'masculin'

#suppression pop():supprimer un élément spécifié par clé
value_delete = mon_dico.pop('ville')

#Opération sur les dictionnaires
#Obtention des clés et des valeurs
all_key = mon_dico.keys()
value = mon_dico.values()
print(all_key, value)

#Exercice pratique