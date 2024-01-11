def nombre_chiffres(nombre, chiffre):
    if nombre == 0 and chiffre == 0:
        return 1
    count = 0
    while nombre > 0:
        if nombre % 10 == chiffre:
            count += 1
        nombre //= 10
    print(count)

nombre_chiffres(2998756, 9)