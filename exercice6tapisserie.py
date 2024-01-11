def tapisserie(n):
    for i in range(n + 1):
        for c in range(n + 1):
            if  i == c:
                print("a", end="")
            else:
                print("u", end="")
        print()
        
tapisserie(3)

# def afficher_tapis(n):
#     for i in range(n+1):
#         for j in range(n+1):
#             if i == j:
#                 print("X", end="")
#             else:
#                 print("O", end="")
#         print()

# afficher_tapis(3)