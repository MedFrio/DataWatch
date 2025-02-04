# DataWatch

## Description
Ce projet implémente un pipeline serverless pour l'analyse automatique de fichiers CSV. Il s'appuie sur Python (Django) pour la gestion du backend et intègre SharePoint et Power Automate pour le traitement des fichiers.

## Architecture du Projet

1. **Envoi des fichiers CSV** :
   - Les fichiers CSV sont envoyés via une API Graph vers SharePoint.
   
2. **Traitement des fichiers** :
   - Power Automate détecte l'ajout de nouveaux fichiers et les traite selon les règles définies.
   
3. **Retour du traitement** :
   - Power Automate génère un retour et met à jour SharePoint avec les résultats du traitement.
   
4. **Analyse des résultats** :
   - Le backend en Django analyse la bibliothèque SharePoint pour détecter l'arrivée du retour.
   - En fonction des résultats, des actions spécifiques sont déclenchées.

## Technologies utilisées

- **Backend** : Python, Django
- **Stockage** : SharePoint (via API Graph)
- **Automatisation** : Power Automate
- **Analyse des données** : Django et bibliothèques Python pour la manipulation des CSV

## Installation et configuration

1. **Cloner le dépôt** :
   ```sh
   git clone https://github.com/MedFrio/DataWatch.git
   cd DataWatch
   ```
2. **Créer et activer un environnement virtuel** :
   ```sh
   python -m venv venv
   source venv/bin/activate  # Sur Mac/Linux
   venv\Scripts\activate     # Sur Windows
   ```
3. **Installer les dépendances** :
   ```sh
   pip install -r requirements.txt
   ```
4. **Configurer les accès SharePoint et Power Automate** :
   - Modifier les variables d'environnement ou configurer un fichier `.env` avec les accès API Graph et SharePoint.

## Exécution du projet

1. **Lancer le serveur Django** :
   ```sh
   python manage.py runserver
   ```
2. **Envoyer un fichier CSV via l'API**
3. **Vérifier le traitement sur SharePoint**
4. **Analyser les retours et logs pour suivre le workflow**

## Contribution

Les contributions sont les bienvenues ! Merci de suivre les bonnes pratiques Git et de créer des pull requests pour toute modification.

## Licence

Ce projet est sous licence Unlicense.

