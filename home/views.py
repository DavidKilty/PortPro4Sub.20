from django.shortcuts import render, get_object_or_404
from .models import Profile, Tip
from .forms import TipForm
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'  

def home(request):
    balance = None
    if request.user.is_authenticated:
        try:
            profile = Profile.objects.get(user=request.user)
            balance = profile.total_tips_received
        except Profile.DoesNotExist:
            balance = None
    return render(request, 'home/index.html', {'balance': balance})

def search_tip_jar(request):
    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            profile = get_object_or_404(Profile, tip_jar_id=query)
            return render(request, 'profile_detail.html', {'profile': profile})
    return render(request, 'search.html')

def profile_detail(request, tip_jar_id):
    profile = get_object_or_404(Profile, tip_jar_id=tip_jar_id)
    if request.method == "POST":
        form = TipForm(request.POST, sender=request.user, receiver=profile)
        if form.is_valid():
            form.save()
    else:
        form = TipForm(sender=request.user, receiver=profile)
    
    return render(request, 'profile_detail.html', {'profile': profile, 'form': form})

def tip_list(request):
    tips = Tip.objects.all()  # Query to get all tips from the database
    return render(request, 'tip_list.html', {'tips': tips})
