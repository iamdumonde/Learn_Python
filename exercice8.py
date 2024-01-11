import math

def calculer_volume_cone(rayon, hauteur):
    # Calcul du volume du cône droit
    volume = (1/3) * math.pi * rayon**2 * hauteur
    return volume

# Saisie du rayon et de la hauteur
rayon = float(input("Entrez le rayon du cône : "))
hauteur = float(input("Entrez la hauteur du cône : "))

# Calcul du volume en utilisant la fonction
volume_cone = calculer_volume_cone(rayon, hauteur)

# Affichage du résultat
print(f"Le volume du cône avec un rayon de {rayon} et une hauteur de {hauteur} est : {volume_cone}")
