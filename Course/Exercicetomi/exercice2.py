

def nombre_divisible(number):
    nmbr_fois = 0
    while number % 2 == 0:
        nmbr_fois += 1
        number //= 2
    print(nmbr_fois)
    return nmbr_fois

nombre_divisible(4)
        
