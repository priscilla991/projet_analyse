import pandas as pd

class Preprocessor:

    def fill_missing_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remplit les valeurs manquantes dans quantite avec 0."""
        df["quantite"] = df["quantite"].fillna(0)
        return df

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        """Supprime les doublons."""
        df = df.drop_duplicates()
        return df

    def normalize_text(self, df: pd.DataFrame) -> pd.DataFrame:
        """Met les colonnes texte en minuscules et enlève les espaces."""
        text_cols = ["produit", "categorie", "ville", "source"]
        for col in text_cols:
            df.loc[:, col] = df[col].str.lower().str.strip()

        return df

    def preprocess(self, df: pd.DataFrame) -> pd.DataFrame:
        """Pipeline complet."""
        df = self.fill_missing_values(df)
        df = self.remove_duplicates(df)
        df = self.normalize_text(df)
        return df
