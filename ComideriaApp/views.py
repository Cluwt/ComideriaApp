from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Views do Web App Comideria:


# View responsável por abrir o Sistema, renderizando a página de Home.
def appHome(request):
    # Carrega o template do HTML:
    template = loader.get_template("appHome.html")

    # Aviso da página de dashboard carregada:
    print("Página home do Web App Comideria foi carregada com sucesso!")

    # Renderiza o template:
    return HttpResponse(template.render())
    