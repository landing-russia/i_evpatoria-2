from django.shortcuts import render


def home(request):
    return render(request, 'excursions/index.html', {'section': 'excursions'})
