
# raise permet de lever une exception, ou erreur d'indentation
# en python, les exceptions sont gérées à l'aide des blocs try, except, else, et éventuellement finally;
# lE BLOC "try" contient le code susceptible de générer une exception
# Le Bloc "except" spécifie le code à exécuter si une exception est levée
# Le bloc "else"(optionnel) contient le code à exécuter si aucune exception n'est levée.
# Le bloc "finally"(optionnel) contient le code qui s'exécute toujours, que des exceptions soient levées ou non.

try:
    print('Tola bola')
except:
    print('Error')
    raise
else:
    print('next execution')
finally:
    print('De toute façon  je serai exécuté')