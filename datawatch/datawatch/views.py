import uuid
from django.shortcuts import render
from django.http import JsonResponse

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