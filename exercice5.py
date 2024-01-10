# while True:
#     entierpositif = input('Entrez un entier strictement positif : ')
#     print(entierpositif)
#     break

def display_diviseurs():
    all_diviseurs = []
    number = int(input("Enter a positive number superior to 1 :  "))
    while number <= 1:
        number = int(input('Enter a positive number superior to 1 :  ' ))
    
    for i in range(2, number):
            if number % i == 0:
                all_diviseurs.append(i)
    
    if not all_diviseurs:
        print("aucun, il est premier")
    else:    
        print(f"Les diviseurs propres de {number} sont : {all_diviseurs}")
                
display_diviseurs()