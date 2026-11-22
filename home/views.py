
from django.http import HttpResponse

menu = """
<nav>
    <a href="/">Principal</a> |
    <a href="/sobre/">Sobre</a> |
    <a href="/contato/">Contato</a> |
    <a href="/ajuda/">Ajuda</a>
</nav>
"""

def index(request):
    return HttpResponse(menu + "<h1>Página Principal</h1>")

def sobre(request):
    return HttpResponse(menu + "<h1>Sobre</h1><p>Informações sobre o nosso sistema.</p>")

def contato(request):
    return HttpResponse(menu + "<h1>Contato</h1><p>Esta é a página de contato.</p>")

def ajuda(request):
    return HttpResponse(menu + "<h1>Ajuda</h1><p>Esta é a página de ajuda.</p>")
