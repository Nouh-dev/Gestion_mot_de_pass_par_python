#  Password Manager (Python)

##  Description
Ce projet est un gestionnaire de mots de passe simple écrit en Python.  
Il permet à l'utilisateur d'ajouter, afficher, rechercher et supprimer des comptes (site, nom d'utilisateur et mot de passe).

Les mots de passe sont masqués par défaut et ne sont visibles que si le mot de passe principal est correct.

---

##  Fonctionnalités

-  Ajouter un ou plusieurs comptes
-  Afficher tous les comptes
-  Rechercher un compte par nom de site
-  Supprimer un compte
-  Masquer les mots de passe sans authentification

---

##  Technologies utilisées

- Python 3
- Module `getpass` (pour cacher les mots de passe)

---

##  Structure des données

Les comptes sont stockés dans une liste sous forme de dictionnaires :

```python
account = {
    "site": "example.com",
    "username": "user123",
    "password": "mypassword"
}
