from django.shortcuts import render, get_object_or_404
from app.models import MusicGenre, Musician, Product


def main_page(request):
    return render(request, 'main_page.html')


def category_page(request):
    return render(request, 'category_page.html', )


def rock_page(request):
    queen = Musician.objects.get(name='Queen')
    system_of_down = Musician.objects.get(name='System of a Down')
    linkin_park = Musician.objects.get(name='Linkin Park')
    context = {
               'queen': queen,
               'system_of_down': system_of_down,
               'linkin_park': linkin_park,

               }
    return render(request, 'rock_page.html', context)


def hip_hop_page(request):
    return render(request, 'hip-hop_page.html', )


def pop_page(request):
    return render(request, 'pop_page.html', )


def jazz_page(request):
    return render(request, 'jazz_page.html')


def electronic_page(request):
    return render(request, 'electronic_page.html')


def linkin_park_page(request):
    return render(request, 'linkin_park_page.html')


def queen_page(request, product_slug):
    artist = Musician.objects.get(slug=product_slug)
    context = {'artist': artist}
    return render(request, 'queen_page.html', context)


def system_of_down_page(request):
    return render(request, 'system_of_down_page.html')


def two_pac_page(request):
    return render(request, '2_pac_page.html')


def kendrick_lamar_page(request):
    return render(request, 'kendrick_lamar_page.html')


def eminem_page(request):
    return render(request, 'eminem_page.html')


def adele_page(request):
    return render(request, 'adele_page.html')


def rihanna_page(request):
    return render(request, 'rihanna_page.html')


def beyonce_page(request):
    return render(request, 'beyonce_page.html')


def frank_sinatra_page(request):
    return render(request, 'frank_sinatra_page.html')


def ray_charles_page(request):
    return render(request, 'ray_charles_page.html')


def louis_armstrong_page(request):
    return render(request, 'louis_armstrong_page.html')


def avicii_page(request):
    return render(request, 'avicii_page.html')


def daft_punk_page(request):
    return render(request, 'daft_punk_page.html')


def moby_page(request):
    return render(request, 'moby_page.html')
