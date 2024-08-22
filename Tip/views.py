from django.shortcuts import render
from .models import Tip

def tip_list(request):
    tips = Tip.objects.all()  # Query to get all tips from the database
    return render(request, 'tip_list.html', {'tips': tips})

