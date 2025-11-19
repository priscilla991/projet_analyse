import os
import matplotlib.pyplot as plt

class ChartBuilder:
    def __init__(self, df):
        """Initialise avec un DataFrame nettoyé."""
        self.df = df

    def plot_sales_per_category(self, output_dir="plots"):
        os.makedirs(output_dir, exist_ok=True)
        self.df.groupby("categorie")["total"].sum().plot(kind="bar")
        plt.title("Ventes par catégorie")
        plt.ylabel("Montant (€)")
        plt.savefig(os.path.join(output_dir, "ventes_par_categorie.png"))
        plt.close()

    def plot_sales_over_time(self, output_dir="plots"):
        os.makedirs(output_dir, exist_ok=True)
        self.df.groupby("date")["total"].sum().plot(kind="line")
        plt.title("Évolution des ventes")
        plt.ylabel("Montant (€)")
        plt.savefig(os.path.join(output_dir, "evolution_ventes.png"))
        plt.close()

    def plot_sales_per_city(self, output_dir="plots"):
        os.makedirs(output_dir, exist_ok=True)
        self.df.groupby("ville")["total"].sum().plot(kind="bar")
        plt.title("Ventes par ville")
        plt.ylabel("Montant (€)")
        plt.savefig(os.path.join(output_dir, "ventes_par_ville.png"))
        plt.close()

    def generate_all(self, output_dir="plots"):
        """Génère tous les graphiques en une seule commande."""
        self.plot_sales_per_category(output_dir)
        self.plot_sales_over_time(output_dir)
        self.plot_sales_per_city(output_dir)
