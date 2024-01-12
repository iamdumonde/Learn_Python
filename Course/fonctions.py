#  jamais de majuscules dans le nom d'une fonction
# on évite de donner le même nom d'une fonction à une variable
# pour accéder à une variable globale en python utilisation du mot clé "globale"
# def year():
#     print('Nous sommes en 2024')

# year = 2024
# def next_year():
#     global year
#     year += 1
#     print(year)
    
# next_year()

#
year = 2024
def next_year(year):
    year += 1
    print(year)
    
# next_year(year)

#
def addition():
    sum = 5 + 5
    print(sum)
 
# addition()

def addition1():
    sum = 5 + 9
    print(sum)
# addition1()

#ajout des paramètres par défaut( def fonction(n=6, y=7):)
def addition2(n=5):
    sum = 5 + n
    # print(f'addition2 : {sum}')
addition2(9)

# une fonction avec return
def addition3(n):
    return 6 + n

# print(addition3(30))

#
def multiply(x, y):
    return x * y
# print(multiply(2, 2))

#
def puissance(n):
    multiply = addition3(n)
    puissance = 2 ** multiply
    return puissance

# print(puissance(2))


#######################
def voyelle_number(word):
    count = 0
    voyelles = 'aeuoiAEUOI'
    all_voyelles = []
    for letter in word:
        if letter in voyelles:
            count += 1
            all_voyelles.append(letter)
        elif not letter in voyelles:
            print('none vowels')
    # count = len(all_voyelles)
    print(f'Les voyelles dans "{word}" sont : {all_voyelles}')
    print(f'Nous avons "{count}" voyelles dans "{word}"')

mot = "Magnifique"
# voyelle_number(mot)

def digitize(n):
    list_n = list(map(int, str(n)))
    list_n.reverse()
    print(list_n)
    # return list_n.reverse()

numbers = 3696
# digitize(numbers)

# liste_chiffres = list(map(int, str(nombre)))

nombre = 35231
liste_chiffres = list(map(int, str(nombre)))
liste_chiffres.reverse()
# print(liste_chiffres)

# def count_numbers(start, end):
#     count = 0
#     for i in range(start, end+1):
#         if '5' not in str(i):
#             count += 1
#     # return count
#     print(count)
    
# count_numbers(1, 9)
# count_numbers(4, 17)

def dont_give_me_five(start,end):
    # your code here
    n = 0
    for number in range(start, end + 1):
        if number != 5:
            n += 1
    # return n   # amount of numbers
    print(n)
    
dont_give_me_five(1,9)
dont_give_me_five(4,17)

def count_numbers(start, end):
    count = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            count += 1
    print(count)

count_numbers(1, 9)  # Résultat attendu : 8
count_numbers(4, 17) # Résultat attendu : 12


def find_deleted_number(arr, mixed_arr):
    if not arr:
        return 0
    
    original_sum = sum(arr)
    
    mixed_sum = sum(mixed_arr)
    
    deleted_number = original_sum - mixed_sum
    
    return deleted_number
    # print(deleted_number)

# Example usage:
original_sequence = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_sequence = [3, 2, 4, 6, 7, 8, 1, 9]

result = find_deleted_number(original_sequence, mixed_sequence)
print(result)