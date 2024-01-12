def calculer_moyenne(list_numbers):
    sumof = 0
    longueur = len(list_numbers)
    for number in list_numbers:
        sumof += number
    moyenne = round((sumof / longueur), 2)
    # print(sumof, longueur, moyenne)
    # print(f'La moyenne de la liste "{list_numbers}" est "{moyenne}"') 
    return moyenne
    
# calculer_moyenne([2,2,5,6,8])
# calculer_moyenne([10,2,5,6,8])
# calculer_moyenne([2,2,25,6,8])
# calculer_moyenne([2,2,15,69,8])