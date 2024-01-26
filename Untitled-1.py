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
