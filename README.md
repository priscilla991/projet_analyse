## 📊 Plateforme d’Analyse de Données — Projet Python

Application modulaire permettant de charger, nettoyer, analyser et visualiser des données de ventes multi-sources.

### 🧩 1. Description du Projet

Ce projet a été réalisé dans le cadre d’un exercice complet d’architecture logicielle en Python.
L’objectif est de créer :

- un système robuste de chargement et validation de données CSV

- une couche de traitement et nettoyage avancé

- des statistiques et agrégations automatiques

- des visualisations professionnelles

- un rapport PDF généré automatiquement

L’application suit une architecture en couches bien structurée, proche d’un environnement professionnel.

### 📁 2. Architecture du Projet
projet_analyse/  
│
  
├── data_loader/            # Chargement & validation des données
│   ├── csv_loader.py
│   └── data_validator.py
│
  
├── data_processor/         # Nettoyage & agrégations
│   ├── cleaner.py
│   ├── aggregator.py
│   └── statistics.py
│ 
  
├── visualization/          # Graphiques & rapport PDF
│   ├── chart_builder.py
│   └── report_generator.py
│
  
├── data/                   # Données sources (CSV)
├── outputs/                # Rapport PDF généré automatiquement
├── plots/                  # Graphiques générés
│
  
├── main.py                 # Point d’entrée principal
├── config.py               # Configuration centralisée (optionnel)
├── requirements.txt        # Dépendances Python
└── README.md               # Documentation

### 🚀 3. Fonctionnalités principales
**🔹 Chargement & Validation**

Lecture sécurisé de fichiers CSV

Logs détaillés

Détection :

valeurs manquantes

doublons

erreurs de types

**🔹 Nettoyage des données**

Conversion des dates

Gestion des valeurs manquantes

Suppression des doublons

Création de colonnes dérivées (total = prix * quantite)

**🔹 Statistiques**

Total des ventes

Ventes par catégorie

Quantité moyenne vendue

Agrégations par mois et par ville

**🔹 Visualisations**

Graphique des ventes par catégorie

Graphique des ventes mensuelles

Graphique des ventes par ville

Histogrammes / barres

Toutes les images sont enregistrées dans /plots.

**🔹 Rapport PDF**

Génération automatique d’un rapport PDF contenant :

statistiques clés

graphiques intégrés

résumé des résultats

Le fichier est enregistré dans :

outputs/rapport.pdf

### 🛠️ 4. Installation & Exécution
**► 1. Cloner le projet**
git clone https://github.com/<ton-username>/projet_analyse.git
cd projet_analyse

**► 2. Créer un environnement virtuel**
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

**► 3. Installer les dépendances**
pip install -r requirements.txt

**► 4. Lancer l’application**
python main.py


Les résultats s’affichent dans le terminal
Les graphiques sont enregistrés dans : /plots
Le rapport PDF dans : /outputs/rapport.pdf

**🧪 5. Tests unitaires (optionnel)**

Des fichiers de test existent dans tests/.

Pour lancer tous les tests :

pytest

**📊 6. Exemple de Données**

Les fichiers CSV doivent contenir (au minimum) :

date,produit,categorie,prix,quantite,ville,source
2025-01-01,Stylo,Fournitures,1.5,10,Paris,web
...

**📝 7. Améliorations possibles**

API REST (FastAPI)

Dashboard interactif (Streamlit)

Export Excel

Tests d’intégration avancés

Dockerisation

**👤 8. Auteur**

Projet réalisé par : **Priscilla**
Formation : Administrateur Cloud SysOps — Projet d’Analyse de Données

**🎉 Merci d’avoir consulté ce projet !**
