# 1 -
all_dictionnary = [
    {
        "title": "LaRousse",
        "author": "Albert Einstein",
        "genre": "educational"
    },
    {
        "title": "Oxford",
        "author": "English School",
        "genre": "Learning"
    },
    {
        "title": "Bilingual",
        "author": "Teacher Training",
        "genre": "Interesting"
    },
    {
        "title": "French to English",
        "author": "David",
        "genre": "educational"
    },
    {
        "title": "Rigobert",
        "author": "Académie Française",
        "genre": "Interesting"
    }
]

# 2
livres_genre_educ = []
livres_genre_inter = []
livres_genre_lear = []
for dictionnary in all_dictionnary:
    if dictionnary['genre'] == "educational":
        livres_genre_educ.append(dictionnary)
    elif dictionnary['genre'] == "Interesting":
        livres_genre_inter.append(dictionnary)
    elif dictionnary['genre'] == "Learning":
        livres_genre_lear.append(dictionnary)
        
print(livres_genre_educ)
print(livres_genre_inter)
print(livres_genre_lear)

