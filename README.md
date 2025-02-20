# DataWatch

## Description
Ce projet implémente un pipeline serverless pour l'analyse automatique de fichiers CSV. Il s'appuie sur Python (Django) pour la gestion du backend et intègre OneDrive et Power Automate pour le traitement des fichiers.

<p align="center">
  <img src="https://github.com/user-attachments/assets/fa6c359d-bb4b-4f9d-ae2a-54db750fefb8" width="400">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/865fcef7-c89d-410b-a7e6-6a90e2197218" width="400">
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/5e94bdf1-e8d3-452a-a23f-c9b241f5d3a5" width="400">
</p>

## Architecture du Projet

1. **Envoi des fichiers CSV** :
   - Les fichiers CSV sont envoyés via une API vers OneDrive.
   
2. **Traitement des fichiers** :
   - Power Automate détecte l'ajout de nouveaux fichiers et les traite selon les règles définies.
   
3. **Retour du traitement** :
   - Power Automate génère un retour et met à jour OneDrive avec les résultats du traitement.
   
4. **Analyse des résultats** :
   - Le backend en Django analyse la bibliothèque OneDrive pour détecter l'arrivée du retour.
   - En fonction des résultats, des actions spécifiques sont déclenchées.

## Technologies utilisées

- **Backend** : Python, Django
- **Stockage** : OneDrive (via API)
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
4. **Configurer les accès OneDrive et Power Automate**

## Exécution du projet

1. **Lancer le serveur Django** :
   ```sh
   python manage.py runserver
   ```
2. **Envoyer un fichier CSV via l'API**
3. **Vérifier le traitement sur OneDrive**
4. **Analyser les retours et logs pour suivre le workflow**

## Licence

Ce projet est sous licence Unlicense.

