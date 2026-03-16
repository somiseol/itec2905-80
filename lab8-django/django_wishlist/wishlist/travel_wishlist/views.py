'''
controllers are called views in django
'''


from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm


def place_list(request):

    if request.method == "POST":
        form = NewPlaceForm(request.POST)  # creating a form from data in the request
        place = form.save()  # creating a model object from form
        if form.is_valid():  # validation against db constraints
            place.save()  # saves place to db
            return redirect('place_list')  # reload homepage

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()  # used to create HTML
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def about(request):
    about = 'a website to create a wishlist of places'
    return render(request, 'travel_wishlist/about.html', {'author': 'Somi', 'about': about})


def places_visited(request):
    visited_places = Place.objects.filter(visited=True).order_by('name')
    return render(request, 'travel_wishlist/visited.html', {'visited_places': visited_places})
