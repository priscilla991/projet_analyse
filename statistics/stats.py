import pandas as pd

class StatsCalculator:
    def __init__(self, df):
        # Création d'une copie pour éviter SettingWithCopyWarning
        self.df = df.copy()

        # Calcul systématique de la colonne total
        self.df.loc[:, "total"] = self.df["prix"] * self.df["quantite"]

    def total_sales(self):
        return self.df["total"].sum()

    def sales_by_category(self):
        return self.df.groupby("categorie")["total"].sum()

    def average_quantity(self):
        return self.df["quantite"].mean()
