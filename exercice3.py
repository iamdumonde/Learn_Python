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
print(sum) 
print(dataNumber)
print(numbersup_100)
    
    


    