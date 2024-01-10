# le nombre exact de grains (nombre entier)
grains = 1
for i in range(1, 65):
    # print(f'{i} : {grains}')
    grains *= 2
    
# le nombre de grains en notation scientifique (nombre réel)
grains = 1
for i in range(1, 65):
    print(i, ': ',"{:.2e}".format(grains))
    grains *= 2
