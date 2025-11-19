import pandas as pd
import logging

class DataValidator:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def check_missing_values(self):
        """Affiche les valeurs manquantes par colonne."""
        missing = self.df.isnull().sum()
        print("\nValeurs manquantes :")
        print(missing)
        return missing

    def check_duplicates(self):
        """Affiche le nombre de doublons."""
        duplicates = self.df.duplicated().sum()
        print("\nDoublons :")
        print(duplicates)
        return duplicates

    def validate(self):
        """Exécute toutes les validations utiles."""
        print("\n=== VALIDATION DES DONNÉES ===")
        self.check_missing_values()
        self.check_duplicates()
        print("\nValidation terminée ✔️")
