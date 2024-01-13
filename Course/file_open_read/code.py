    
# écriture dans un fichier
with open('Affecter_planning_individuel.txt', 'w') as fichier:
    fichier.write("Ceci est une ligne écrite dans le fichier.")

#ajout 
with open ('Affecter_planning_individuel.txt', 'a') as fichier:
    fichier.write('\nCeci est une nouvelle ligne ajoutée au fichier.')
    
with open('Affecter_planning_individuel.txt', 'r')as fichier:
    contenu = fichier.read()
    print(contenu)