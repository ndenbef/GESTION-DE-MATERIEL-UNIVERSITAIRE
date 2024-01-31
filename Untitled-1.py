class Category:
    categories = []  # Liste pour stocker les catégories créées

    def __init__(self, id, libelle, budget):
        self.id = id
        self.libelle = libelle
        self.budget = budget
        self.depense = 0
        self.budget_restant = budget
        Category.categories.append(self)  # Ajout de la catégorie à la liste

    @staticmethod
    def ajoutCategory(id, libelle, budget):
        Category(id, libelle, budget)

    @staticmethod
    def retirerCategory(id):
        for cat in Category.categories:
            if cat.id == id:  # Cherche la catégorie avec l'id correspondant
                Category.categories.remove(cat)
                return
        print("La catégorie avec l'id {0} n'existe pas.".format(id))

    @staticmethod
    def modifierBudget(id, nouveau_budget):
        for cat in Category.categories:
            if cat.id == id:  # Cherche la catégorie avec l'id correspondant
                if nouveau_budget >= cat.depense:
                    cat.budget = nouveau_budget
                    cat.budget_restant = nouveau_budget - cat.depense
                else:
                    print("Le nouveau budget est inférieur à la dépense.")
                return
        print("La catégorie avec l'id {0} n'existe pas.".format(id))

    @staticmethod
    def suiviCategory():
        for cat in Category.categories:
            print("Catégorie : {0} - Budget restant : {1}/{2} - Dépense : {3}".format(
                cat.libelle, cat.budget_restant, cat.budget, cat.depense))

class Article:
    def __init__(self, id, code, nom, stock, categorie, fournisseur):
        self.Id = id
        self.code = code
        self.nom = nom
        self.stock = stock
        self.categorie = categorie
        self.fournisseur = fournisseur

    def suiviStock(self):
        print(f"Article : {self.nom} - Stock : {self.stock}")

    def ajouter(self, quantite):
        self.stock += quantite

    def retirer(self, quantite):
        if quantite <= self.stock:
            self.stock -= quantite
        else:
            print("Quantité demandée supérieure au stock disponible")

    def modifier(self, code=None, nom=None, stock=None, categorie=None, fournisseur=None):
        if code is not None:
            self.code = code
        if nom is not None:
            self.nom = nom
        if stock is not None:
            self.stock = stock
        if categorie is not None:
            self.categorie = categorie
        if fournisseur is not None:
            self.fournisseur = fournisseur


class Suppression:
    def __init__(self, date, retiree):
        self.date = date
        self.retiree = retiree

    def suppArticle(self, article):
        if not self.retiree:
            self.retiree = True
            article.retirer(1)
            print(f"L'article {article.nom} a été retiré.")
        else:
            print("Cet article a déjà été retiré.")
            
class Sortie:
    def __init__(self, id, code, type, quantite):
        self.id = id
        self.code = code
        self.type = type
        self.quantite = quantite


class Fournisseurs:
    def __init__(self, id, nom, telephone):
        self.id = id
        self.nom = nom
        self.telephone = telephone

    def ajoutFournisseur(self):
        # Code pour enregistrer le fournisseur dans la base de données ou autre action à réaliser lors de l'ajout
        print(f"Le fournisseur {self.nom} a été ajouté avec succès.")
        
class Entree:
    def __init__(self, id, code, type, quantite):
        self.id = id
        self.code = code
        self.type = type
        self.quantite = quantite
        
class Enregistrement:
    def __init__(self, date, ajoute):
        self.date = date
        self.ajoute = ajoute

    def ajoutArticle(self, article):
        # Code pour ajouter l'article à l'enregistrement
        print(f"L'article {article} a été ajouté à l'enregistrement du {self.date}.")

class Coût:
    def __init__(self, id, code, opération, montant, articles):
        self.id = id
        self.code = code
        self.opération = opération
        self.montant = montant
        self.articles = articles

    def enregistrementCout(self):
        print(f"Coût enregistré : ID={self.id}, Code={self.code}, Opération={self.opération}, Montant={self.montant}, Articles={self.articles}")

    def changerOpération(self, nouvelle_opération):
        self.opération = nouvelle_opération
        print(f"L'opération a été mise à jour : {nouvelle_opération}")

# import sqlite3
# import tkinter as tk

# # Classe Category modifiée pour intégrer la base de données
# class Category:
#     def _init_(self, id, libelle, budget):
#         self.id = id
#         self.libelle = libelle
#         self.budget = budget
#         self.depense = 0
#         self.budget_restant = budget

#     @staticmethod
#     def ajoutCategory(id, libelle, budget):
#         # Code pour ajouter une catégorie dans la base de données
#         print("Ajout de la catégorie dans la base de données")

#     @staticmethod
#     def retirerCategory(id):
#         # Code pour retirer une catégorie de la base de données
#         print("Retrait de la catégorie de la base de données")

#     @staticmethod
#     def modifierBudget(id, nouveau_budget):
#         # Code pour modifier le budget d'une catégorie dans la base de données
#         print("Modification du budget dans la base de données")

#     @staticmethod
#     def suiviCategory():
#         # Code pour récupérer les catégories depuis la base de données et afficher le suivi
#         print("Suivi des catégories")

# # Classe Article modifiée pour intégrer la base de données
# class Article:
#     def _init_(self, id, code, nom, stock, categorie, fournisseur):
#         self.id = id
#         self.code = code
#         self.nom = nom
#         self.stock = stock
#         self.categorie = categorie
#         self.fournisseur = fournisseur

#     def suiviStock(self):
#         print(f"Article : {self.nom} - Stock : {self.stock}")

#     def ajouter(self, quantite):
#         self.stock += quantite

#     def retirer(self, quantite):
#         if quantite <= self.stock:
#             self.stock -= quantite
#         else:
#             print("Quantité demandée supérieure au stock disponible")

#     def modifier(self, code=None, nom=None, stock=None, categorie=None, fournisseur=None):
#         if code is not None:
#             self.code = code
#         if nom is not None:
#             self.nom = nom
#         if stock is not None:
#             self.stock = stock
#         if categorie is not None:
#             self.categorie = categorie
#         if fournisseur is not None:
#             self.fournisseur = fournisseur


# # Classe Coût modifiée pour intégrer la base de données
# class Coût:
#     def _init_(self, id, code, opération, montant, articles):
#         self.id = id
#         self.code = code
#         self.opération = opération
#         self.montant = montant
#         self.articles = articles

#     def enregistrementCout(self):
#         print(f"Coût enregistré : ID={self.id}, Code={self.code}, Opération={self.opération}, Montant={self.montant}, Articles={self.articles}")

#     def changerOpération(self, nouvelle_opération):
#         self.opération = nouvelle_opération
#         print(f"L'opération a été mise à jour : {nouvelle_opération}")

#     def générerStat(self):
#         # Code pour générer des statistiques sur le coût
#         print("Statistiques du coût")

# # Classe pour l'interface graphique
# class Application(tk.Tk):
#     def _init_(self):
#         tk.Tk._init_(self)

#         # Initialisation de la base de données
#         self.conn = sqlite3.connect("coûts.db")
#         self.c = self.conn.cursor()

#         # Création des tables dans la base de données si elles n'existent pas
#         self.c.execute("""CREATE TABLE IF NOT EXISTS categories (
#                         id INTEGER PRIMARY KEY,
#                         libelle TEXT NOT NULL,
#                         budget REAL NOT NULL,
#                         depense REAL NOT NULL,
#                         budget_restant REAL NOT NULL
#                         )""")
#         self.c.execute("""CREATE TABLE IF NOT EXISTS articles (
#                         id INTEGER PRIMARY KEY,
#                         code TEXT NOT NULL,
#                         nom TEXT NOT NULL,
#                         stock INTEGER NOT NULL,
#                         categorie_id INTEGER NOT NULL,
#                         fournisseur TEXT NOT NULL,
#                         FOREIGN KEY (categorie_id) REFERENCES categories (id)
#                         )""")

#         # ...
#         # Code pour créer les autres tables dans la base de données si nécessaire
#         # ...

#     def quitter(self):
#         self.conn.close()
#         self.destroy()

# # Exemple d'utilisation
# if _name_ == "_main_":
#     app = Application()
#     app.mainloop()
