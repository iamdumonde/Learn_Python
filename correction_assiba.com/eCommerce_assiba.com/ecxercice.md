# Projet E-Commerce en Python

Vous êtes chargé de développer un système de gestion pour un magasin en ligne. Le système doit permettre la création de produits, l'ajout de produits au panier, et la génération de factures en format CSV.

## Classes à Implémenter :

- Produit : Une classe représentant un produit avec les attributs id, nom, et prix.

- BaseDeDonnees : Une classe pour gérer la connexion à la base de données. Elle doit avoir des méthodes pour exécuter des requêtes SQL et récupérer les résultats.

- Panier : Une classe représentant le panier de l'utilisateur. Elle doit permettre d'ajouter des produits avec la quantité et de calculer le total.

- LigneFacture : Une classe représentant une ligne dans la facture. Elle doit contenir un produit, une quantité et permettre de calculer le prix total de la ligne.

- Facture : Une classe qui génère la facture en format CSV. Elle doit prendre le panier comme entrée et créer un fichier CSV avec les informations des produits ajoutés, la quantité, le prix unitaire et le prix total.

## Fonctionnalités à Implementer :

1-Créer un produit.
2- Afficher les produits disponibles.
3- Ajouter un produit au panier avec une quantité spécifiée.
4- Imprimer la facture en format CSV.

## Contraintes :

- Utilisez une base de données MySQL pour stocker les produits.
- Utilisez une approche orientée objet (OOP).
- N'utilisez pas de framework Python.
- Gérez la connexion à la base de données dans la classe BaseDeDonnees.
- La classe Facture doit générer un fichier CSV nommé "facture.csv".
