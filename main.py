import logging
from data_loader.csv_loader import CSVLoader
from data_loader.data_validator import DataValidator
from data_processor.cleaner import DataCleaner
from data_processor.aggregator import DataAggregator
from statistics.stats import StatsCalculator
from visualization.chart_builder import ChartBuilder

logging.basicConfig(level=logging.INFO)


def main():
    print("\n=== CHARGEMENT DU FICHIER ===\n")
    loader = CSVLoader("data/ventes.csv")

    try:
        df = loader.load()
    except FileNotFoundError as e:
        logging.error(e)
        return

    # -------------------------------------------------------
    # VALIDATION
    # -------------------------------------------------------
    print("\nValidation terminée ✔️")
    print("\n=== VALIDATION DES DONNÉES ===")
    validator = DataValidator(df)
    validator.validate()

    # -------------------------------------------------------
    # NETTOYAGE DES DONNÉES
    # -------------------------------------------------------
    print("\n=== PRÉTRAITEMENT DES DONNÉES ===\n")
    cleaner = DataCleaner(df)
    df_clean = cleaner.clean()
    print("Prétraitement terminé ✔️")

    # -------------------------------------------------------
    # STATISTIQUES
    # -------------------------------------------------------
    print("\n=== CALCUL DES STATISTIQUES ===")
    stats = StatsCalculator(df_clean)

    total_sales = stats.total_sales()
    sales_by_cat = stats.sales_by_category()
    avg_qty = stats.average_quantity()

    print(f"Ventes totales : {total_sales:.2f} €\n")
    print("Ventes par catégorie :")
    print(sales_by_cat, "\n")
    print(f"Quantité moyenne vendue : {avg_qty:.2f}\n")
    print("Statistiques terminées ✔️")

    # -------------------------------------------------------
    # AGRÉGATIONS (pour graphes)
    # -------------------------------------------------------
    aggregator = DataAggregator(df_clean)
    ventes_par_mois = aggregator.monthly_sales()
    ventes_par_ville = aggregator.sales_by_city()

    # -------------------------------------------------------
    # GRAPHES
    # -------------------------------------------------------
    print("\n=== GÉNÉRATION DES GRAPHIQUES ===\n")
    charts = ChartBuilder(df_clean)
    charts.generate_all()

    print("\nGraphiques générés dans /plots ✔️")
    print("\nTraitement global terminé ✔️")

    # -------------------------------------------------------
    # RAPPORT PDF
    # -------------------------------------------------------
    print("\n=== GÉNÉRATION DU RAPPORT PDF ===")
    from visualization.report_generator import ReportGenerator

    report = ReportGenerator()
    report.build_report({
        "total_sales": float(total_sales),
        "avg_qty": float(avg_qty),
        "sales_by_category": sales_by_cat.to_dict()
    })


if __name__ == "__main__":
    main()
