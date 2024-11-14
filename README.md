# Architecture monolithique centralisée

## Etapes

1. initialiser un environnement virtuel (conda, venv, ...)
2. créer un unique script python
3. modéliser les différents concepts manipulés en classe (Book, Lib, BookShop)
4. permettre au script python de fonctionner en attente (boucle) infinie d'une commande utilisateur à travers le terminal => doit récupérer une saisie utiliser depuis le terminal
5. déclencher la commande donnée par l'utilisateur :
   1. créer un livre
   2. lister tous les livres
   3. mettre à jour un livre
   4. supprimer un livre
   5. afficher le détail d'un livre
   6. acheter un livre

