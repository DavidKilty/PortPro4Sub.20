from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Tip


class Index(TemplateView):
    template_name = 'home/index.html'  

def home(request):
    return render(request, 'home/index.html')
from django.shortcuts import render, get_object_or_404
from .models import Profile

def search_tip_jar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            profile = get_object_or_404(Profile, tip_jar_id=query)
            return render(request, 'profile_detail.html', {'profile': profile})
    return render(request, 'search.html')

from django.shortcuts import render, get_object_or_404
from .models import Profile, Tip
from .forms import TipForm

def profile_detail(request, tip_jar_id):
    profile = get_object_or_404(Profile, tip_jar_id=tip_jar_id)
    if request.method == "POST":
        form = TipForm(request.POST, sender=request.user, receiver=profile)
        if form.is_valid():
            form.save()
    else:
        form = TipForm(sender=request.user, receiver=profile)
    
    return render(request, 'profile_detail.html', {'profile': profile, 'form': form})

from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html') 
    

