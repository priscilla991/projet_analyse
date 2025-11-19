from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
import os

class ReportGenerator:

    def __init__(self, output_path="outputs/rapport.pdf"):
        self.output_path = output_path
        self.styles = getSampleStyleSheet()

    def build_report(self, stats, charts_dir="plots"):

        doc = SimpleDocTemplate(self.output_path, pagesize=A4)
        content = []

        # Title
        title = Paragraph("<b>Rapport d’Analyse des Ventes</b>", self.styles["Title"])
        content.append(title)
        content.append(Spacer(1, 20))

        # Stats section
        content.append(Paragraph("<b>Statistiques principales :</b>", self.styles["Heading2"]))
        content.append(Paragraph(f"Ventes totales : {stats['total_sales']} €", self.styles["BodyText"]))
        content.append(Paragraph(f"Quantité moyenne : {stats['avg_qty']}", self.styles["BodyText"]))
        content.append(Spacer(1, 12))

        content.append(Paragraph("<b>Ventes par catégorie :</b>", self.styles["Heading3"]))
        for cat, val in stats["sales_by_category"].items():
            content.append(Paragraph(f"{cat} : {val} €", self.styles["BodyText"]))

        content.append(Spacer(1, 20))

        # Add charts
        content.append(Paragraph("<b>Graphiques :</b>", self.styles["Heading2"]))
        content.append(Spacer(1, 12))

        for chart in os.listdir(charts_dir):
            if chart.endswith(".png"):
                img_path = os.path.join(charts_dir, chart)
                content.append(Image(img_path, width=14*cm, height=10*cm))
                content.append(Spacer(1, 25))

        # Build PDF
        doc.build(content)
        print(f"📄 Rapport généré : {self.output_path}")
