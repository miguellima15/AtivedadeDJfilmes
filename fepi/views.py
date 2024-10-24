from django.shortcuts import render
from django.http import HttpResponse

# Lista de filmes
movies = [
    {
        'id': 1,
        'title': 'Ultimato',
        'poster': 'img/ultimato.jpeg',
        'synopsis': 'Sinopse do filme Ultimato: Em uma corrida contra o tempo, um grupo de heróis se une para impedir a destruição do mundo por uma entidade sombria que busca poder absoluto.',
        'cast': ['Ator 1', 'Ator 2', 'Ator 3']
    },
    {
        'id': 2,
        'title': 'Carros',
        'poster': 'img/carros.jpeg',
        'synopsis': 'Sinopse do filme Carros: Relata a história de Lightning McQueen, um carro de corrida que, após um acidente, encontra-se perdido em uma cidade pequena e aprende o valor da amizade e da humildade.',
        'cast': ['Owen Wilson', 'Larry the Cable Guy', 'Bonnie Hunt']
    },
    {
        'id': 3,
        'title': 'Gigantes de Aço',
        'poster': 'img/gigante.jpeg',
        'synopsis': 'Sinopse do filme Gigantes de Aço: Em um futuro próximo, robôs de combate se tornaram populares, e um ex-lutador de boxe se une a seu filho para treinar um robô quebrado em busca da vitória no campeonato.',
        'cast': ['Hugh Jackman', 'Dakota Goyo', 'Evangeline Lilly']
    }
]

def home(request):
    return render(request, 'home.html', {'movies': movies})

def movie_detail(request, id):
    
    movie = next((movie for movie in movies if movie['id'] == id), None)
    
    if movie is None:
        return HttpResponse("Filme não encontrado", status=404)

    return render(request, 'movie_detail.html', {'movie': movie})
