## 📊 Projet d’Analyse des Ventes – Python  

Ce projet a pour objectif de charger, valider, nettoyer et analyser un fichier de ventes, afin de produire :  

===> des statistiques descriptives  

===> des visualisations graphiques  

===> un rapport PDF complet  

Il s’agit d’un pipeline de traitement de données 100% automatisé, conçu avec une architecture modulaire (loader → validation → nettoyage → stats → agrégation → visualisation → rapport).  

### 📁 Structure du projet  
projet_analyse/  
│  
├── main.py                      # Script principal  
├── config.py                    # Configuration globale  
│
├── data/                        # Données brutes  
│   └── ventes_2025.csv  
│
├── data_loader/  
│   ├── csv_loader.py            # Chargement CSV  
│   └── data_validator.py        # Validation des données  
│
├── data_processor/  
│   ├── cleaner.py               # Nettoyage et prétraitement  
│   ├── aggregator.py            # Agrégations  
│   └── preprocess.py  
│
├── statistics/  
│   └── stats.py                 # Calculs statistiques  
│
├── visualization/  
│   ├── chart_builder.py         # Génération des graphiques  
│   └── report_generator.py      # Génération du rapport PDF  
│
├── plots/                       # Graphiques générés  
├── outputs/                     # Rapport PDF  
└── logs/                        # Log du programme  

### 🚀 Installation  

**1. Cloner le projet**  
git clone <ton_repo_git>  
cd projet_analyse  

**2. Créer un environnement virtuel**  
python3 -m venv .venv  
source .venv/bin/activate      # Linux/macOS  
.venv\Scripts\activate         # Windows  

**3. Installer les dépendances**  
pip install -r requirements.txt  


Si aucune liste n’est fournie, installer manuellement :  

pip install pandas matplotlib reportlab  

### ▶️ Exécution du projet  
python main.py  

### 🔄 Pipeline complet exécuté  

**1. Chargement des données**  

Lecture du fichier CSV  

Gestion des erreurs  

**2. Validation**  

Valeurs manquantes

Doublons

Info colonnes

**3. Nettoyage**

Correction des types

Formatage texte

Suppression des doublons

**4. Statistiques**

Ventes totales

Ventes par catégorie

Quantité moyenne

Colonnes dérivées (ex: total = prix × quantité)

**5. Agrégations**

Ventes mensuelles

Ventes par ville

**6. Visualisation**

Graphique des ventes par catégorie

Évolution mensuelle

Ventes par ville

Sauvegarde dans /plots

**7. Génération d’un rapport PDF**

Résumé statistiques

Graphiques intégrés

Rapport généré dans /outputs/rapport.pdf

**📄 Exemple de sortie PDF**

**Un rapport professionnel comprenant :**

- Page de résumé

- Statistiques détaillées

- Graphiques en couleur

- Format adapté à l’impression

**🔧 Technologies utilisées**

Python 3

Pandas

Matplotlib

ReportLab

Logging intégré

**🧪 Tests**

Les tests unitaires sont prévus dans le dossier :

tests/

**📌 Prochaines améliorations possibles**

CLI avec argparse

Interface graphique Tkinter

Export Excel / SQL

Interface Web (Flask, FastAPI)

Dashboard interactif (Plotly Dash)
