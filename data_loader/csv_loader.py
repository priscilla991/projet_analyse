import pandas as pd
import logging
import os

class CSVLoader:
    """
    Classe simple pour charger des fichiers CSV avec gestion d'erreurs.
    """

    def __init__(self, filepath: str):
        self.filepath = filepath

    def load(self):
        """
        Charge le fichier CSV et renvoie un DataFrame.
        """
        logging.info(f"Tentative de chargement du fichier : {self.filepath}")

        if not os.path.exists(self.filepath):
            logging.error(f"Fichier introuvable : {self.filepath}")
            raise FileNotFoundError(f"Le fichier {self.filepath} n'existe pas.")

        try:
            df = pd.read_csv(self.filepath)
            logging.info(f"Chargement réussi ({len(df)} lignes).")
            return df
        except Exception as e:
            logging.error(f"Erreur lors du chargement : {e}")
            raise e
