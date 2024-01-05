sum = 0
dataNumber = 0
numbersup_100 = 0
entryNumber1 =  int(input('Enter a number'))
while entryNumber1 > 0:
    entryNumber1 =  int(input('Enter a number'))
    sum += entryNumber1
    dataNumber += 1
    
    if entryNumber1 > 100:
        numbersup_100 += 1
    if entryNumber1 <= 0:
        break
print(f'La somme des entrées: {sum}') 
print(f'Le nombre de données entré: {dataNumber}')
print(f'Le nombre de données supérieur à 100: {numbersup_100}')
    
    


    