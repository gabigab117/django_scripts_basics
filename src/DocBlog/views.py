from datetime import datetime

from django.shortcuts import render

def index(request):

    date = datetime.today()

    return render(request, "DocBlog/index.html", context={"prenom": "Patrick", "date": date})
    # request faite par notre ordi obligatoire !
    # bien le remettre en argument ici après render alors que HttpResponse non.

# pour insérer les données ds un template on utilise le context en paramètre. C'est un dictionnaire.
# On le récupère dans le fichier html avec {{  }}
