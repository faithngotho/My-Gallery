from django.shortcuts import render
from .models import Image, Location, Category
from django.http import Http404

# Create your views here.
def index(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    return render(request,'index.html',{'images':images,'locations':locations})

def get_category(request):
   category_results = Category.objects.all()
   location_results = Location.objects.all()
   return render(request, 'index.html', {'category_results': category_results, 'location_results': location_results})


def get_location(request):
   category_results = Category.objects.all()
   location_results = Location.objects.all()
   return render(request, 'location.html', { 'category_results': category_results, 'location_results': location_results})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Image.search_results(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
