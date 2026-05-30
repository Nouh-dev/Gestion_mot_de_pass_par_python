# Password Manager

## Description

Password Manager is a Python console application designed to securely manage account credentials. Users can add, search, display, and delete account information, including website names, usernames, and passwords.

The application uses password masking for additional privacy and exports all saved accounts to an Excel file using OpenPyXL.

## Features

* Add new accounts
* Display stored accounts
* Search accounts by website name
* Delete accounts
* Password protection for viewing credentials
* Export data to Excel (.xlsx)

## Technologies Used

* Python
* OpenPyXL
* GetPass

## How to Run

1. Install OpenPyXL:

```bash
pip install openpyxl
```

2. Run the application:

```bash
python main.py
```

3. Use the menu to manage your accounts.

## Author

Nouh Marzak
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
