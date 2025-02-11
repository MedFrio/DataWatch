import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist  # Import the ObjectDoesNotExist exception
import requests  # Import the requests module
import json
import re


# URLs des APIs
GET_ANALYSES_URL = "https://prod-03.francecentral.logic.azure.com:443/workflows/4d993846064c4541beee90585c8b9650/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=wbTUey4uG3rr0k8G11VbbbKc4IgDet6xgBacptqwa7A"
GET_ANOMALIES_URL = "https://prod-04.francecentral.logic.azure.com:443/workflows/7431b38e9642480eb78a6d8802c1215f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Y4nvKb51Zx7RR-e8lK-Gds1sYxpL3s5g5MvZm0LYIFw"



def upload_file(request):
    if request.method == "POST":
        csv_file = request.FILES.get("csv_file")
        email = request.POST.get("email")

        if not csv_file or not email:
            return JsonResponse({"error": "Veuillez fournir un fichier CSV et une adresse e-mail."}, status=400)

        # Génération d'un numéro de ticket unique
        ticket_id = str(uuid.uuid4())[:8]  # ID court pour simplicité

        # Simuler le stockage temporaire (peut être remplacé par du cache)
        with open(f"/tmp/ticket_{ticket_id}.txt", "w") as f:
            f.write(f"Email: {email}\nFichier: {csv_file.name}\nStatut: En attente\n")

        return JsonResponse({"ticket_id": ticket_id})

    return render(request, "upload.html")
def accueil(request):
    return render(request, 'accueil.html')

def suivi_ticket(request):
    return render(request, 'suivi_ticket.html')


def check_ticket_status(request, ticket_id):
    """ Vérifie l'état d'un ticket via les APIs """
    try:
        # 1. Faire un POST avec des données JSON sur l'API d'analyses
        payload = {"ticket": ticket_id}
        headers = {'Content-Type': 'application/json'}

        response = requests.post(GET_ANALYSES_URL, data=json.dumps(payload), headers=headers)
        
        if response.status_code == 502:
            return JsonResponse({"status": "En cours", "message": "Analyse en cours de traitement."})

        if response.status_code == 200:
            # 2. Si analyse terminée, on récupère les résultats des analyses
            analysis_results = response.text
            analysis_data = process_analysis_results(analysis_results)

            # 3. Vérifier les anomalies
            anomalies_response = requests.post(GET_ANOMALIES_URL, data=json.dumps(payload), headers=headers)
            
            if anomalies_response.status_code == 502:
                return JsonResponse({"status": "Terminé", "message": "Analyse terminée, aucune anomalie détectée.", "analysis": analysis_data})
            
            if anomalies_response.status_code == 200:
                anomalies = anomalies_response.json()
                anomalies_data = process_anomalies(anomalies)
                return JsonResponse({"status": "Terminé", "message": "Analyse terminée, des anomalies ont été détectées !", "analysis": analysis_data, "anomalies": anomalies_data})

        # Si un autre cas imprévu
        return JsonResponse({"status": "Erreur", "message": "Erreur lors de la récupération des données."})

    except ObjectDoesNotExist as e:  # Handle specific database-related errors
        return JsonResponse({"status": "Erreur", "message": str(e)})
    except Exception as e:  # Catch any other general exceptions
        return JsonResponse({"status": "Erreur", "message": str(e)})


def process_analysis_results(results):
    """ Traite les résultats d'analyse et les formate en données compréhensibles """
    analysis_data = {}
    
    # Utiliser une expression régulière pour extraire les moyennes, écarts-types et médianes
    moyennes_pattern = r"Moyenne des prix : ([0-9\.]+) -  Moyenne des quantités : ([0-9\.]+) -  Moyenne des notes : ([0-9\.]+)"
    ecart_type_pattern = r"Écart-type des prix : ([0-9\.]+) -  Écart-type des quantités : ([0-9\.]+) -  Écart-type des notes : ([0-9\.]+)"
    medianes_pattern = r"Médiane des prix : ([0-9\.]+), Médiane des quantités : ([0-9]+), Médiane des notes : ([0-9\.]+)"
    
    # Chercher les correspondances avec les patterns
    moyennes_match = re.search(moyennes_pattern, results)
    ecart_type_match = re.search(ecart_type_pattern, results)
    medianes_match = re.search(medianes_pattern, results)
    
    # Extraire les valeurs si les correspondances existent
    if moyennes_match:
        moyennes = {
            "prix": float(moyennes_match.group(1)),
            "quantité": float(moyennes_match.group(2)),
            "note": float(moyennes_match.group(3))
        }
    else:
        moyennes = {"prix": None, "quantité": None, "note": None}
    
    if ecart_type_match:
        ecart_types = {
            "prix": float(ecart_type_match.group(1)),
            "quantité": float(ecart_type_match.group(2)),
            "note": float(ecart_type_match.group(3))
        }
    else:
        ecart_types = {"prix": None, "quantité": None, "note": None}
    
    if medianes_match:
        medianes = {
            "prix": float(medianes_match.group(1)),
            "quantité": int(medianes_match.group(2)),
            "note": float(medianes_match.group(3))
        }
    else:
        medianes = {"prix": None, "quantité": None, "note": None}
    
    # Stocker dans un dictionnaire
    analysis_data = {
        "moyenne": moyennes,
        "ecart_type": ecart_types,
        "mediane": medianes
    }

    return analysis_data

def process_anomalies(anomalies):
    """ Traite les anomalies et les formate en données compréhensibles """
    anomalies_data = []
    
    for anomaly in anomalies:
        anomalies_data.append({
            "produit": anomaly['produit'],
            "anomalie": anomaly['anomalie']
        })
    
    return anomalies_data