import pandas as pd

class DataAggregator:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def sales_by_category(self):
        """Retourne total des ventes par catégorie"""
        self.df["total"] = self.df["prix"] * self.df["quantite"]
        return self.df.groupby("categorie")["total"].sum()

    def sales_by_city(self):
        """Retourne total des ventes par ville"""
        self.df["total"] = self.df["prix"] * self.df["quantite"]
        return self.df.groupby("ville")["total"].sum()

    def monthly_sales(self):
        """Retourne un series avec les ventes par mois"""
        if "date" in self.df.columns:
            self.df["total"] = self.df["prix"] * self.df["quantite"]
            self.df["mois"] = self.df["date"].dt.to_period("M").astype(str)
            return self.df.groupby("mois")["total"].sum()
        return None
