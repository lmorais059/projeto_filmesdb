from django.shortcuts import redirect, render
from .models import Filme
from .forms import FilmeSearchForm
from django.contrib.auth.forms import UserCreationForm

def home(request):
    
    ultimos_filmes = Filme.objects.order_by('-id_filme')[:10]
    return render(request, 'pages/home.html', {'filmes': ultimos_filmes})

def filmes(request):
    #return render(request, 'pages/filmes.html')
    if request.method == 'POST':
        novo_filme = Filme()
        novo_filme.id_filme = request.POST.get('id_filme')
        novo_filme.nome = request.POST.get('nome')
        novo_filme.diretor = request.POST.get('diretor')
        novo_filme.ano = request.POST.get('ano')
        novo_filme.sinopse = request.POST.get('sinopse')
        novo_filme.imagem = request.POST.get('imagem')
        novo_filme.save()
        return render(request, 'pages/filmes.html', {'filmes': Filme.objects.all()})
    else:
        filmes = Filme.objects.all()
        return render(request, 'pages/filmes.html', {'filmes': filmes})
    
def delete_filme(request, id_filme):
    filme = Filme.objects.get(id_filme=id_filme)
    filme.delete()
    return render(request, 'pages/filmes.html', {'filmes': Filme.objects.all()})

def detalhes_filme(request, id_filme):
    filme = Filme.objects.get(id_filme=id_filme)
    return render(request, 'pages/detalhes_filme.html', {'filme': filme})

def editar_filme(request, id_filme):
    filme = Filme.objects.get(pk=id_filme)
    if request.method == 'POST':
        filme.nome = request.POST.get('nome')
        filme.diretor = request.POST.get('diretor')
        filme.ano = request.POST.get('ano')
        filme.sinopse = request.POST.get('sinopse')
        filme.imagem = request.POST.get('imagem')
        filme.trailer_url = request.POST.get('trailer_url')
        # Atualize os campos da sinopse e da imagem conforme necessário
        filme.save()
        return redirect('filmes')  # Redirecione de volta para a lista de filmes após a edição
    return render(request, 'pages/editar_filme.html', {'filme': filme})

def classificar_filme(request, id_filme):
    filme = Filme.objects.get(pk=id_filme)
    if request.method == 'POST':
        filme.rating = request.POST.get('rating')
        filme.save()
        return redirect('filmes')  # Redirecione de volta para a lista de filmes após a classificação
    return render(request, 'pages/classificar_filme.html', {'filme': filme})


def adicionar_comentario(request, id_filme):
    filme = Filme.objects.get(pk=id_filme)
    if request.method == 'POST':
        comentario = request.POST.get('comentario')
        filme.comentario = comentario
        filme.save()
        return redirect('filmes')  # Redirecione de volta para a lista de filmes após a adição do comentário
    return render(request, 'pages/adicionar_comentario.html', {'filme': filme})

def trailers(request):
    filmes_com_trailer = Filme.objects.exclude(trailer_url__isnull=True).exclude(trailer_url__exact='')
    return render(request, 'pages/trailers.html', {'filmes_com_trailer': filmes_com_trailer})

def search_filmes(request):
    if request.method == 'POST':
        form = FilmeSearchForm(request.POST)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            diretor = form.cleaned_data['diretor']
            nome_filme = form.cleaned_data['nome_filme']
            ano = form.cleaned_data['ano']
            filmes = Filme.objects.all()
            if rating:
                filmes = filmes.filter(rating=rating)
            if diretor:
                filmes = filmes.filter(diretor__icontains=diretor)
            if nome_filme:
                filmes = filmes.filter(nome__icontains=nome_filme)
            if ano:
                filmes = filmes.filter(ano=ano)
            return render(request, 'pages/search_filmes_result.html', {'filmes': filmes})
    else:
        form = FilmeSearchForm()
    return render(request, 'pages/search_filmes.html', {'form': form})

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redireciona para a página de login após o registro bem-sucedido
    else:
        form = UserCreationForm()
    return render(request, 'pages/registro.html', {'form': form})

def error_404(request, exception=None):
    return render(request, 'pages/404.html', status=404)