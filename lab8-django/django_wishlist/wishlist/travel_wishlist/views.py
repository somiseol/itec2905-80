from django.shortcuts import render
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

# fetch data from the db and display it in the view
def place_list(request):
    # Place.objects is a Manager that runs queries against the table and returns QuerySet objects that represent a set of objects from the database
    places = Place.objects.filter(visited=False).order_by('name')  # only show places not visited
    new_place_form = NewPlaceForm()  # django will make a form object that will be rendered as HTML by the template engine
    return render(request, 'travel_wishlist/wishlist.html', { 'places': places, 'new_place_form': new_place_form })
