import pandas as pd

class DataCleaner:
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        # Convertir la date en datetime
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Supprimer les valeurs manquantes
        df = df.dropna()

        # Supprimer les doublons
        df = df.drop_duplicates()

        # Recalculer la colonne total
        df["total"] = df["prix"] * df["quantite"]

        return df
