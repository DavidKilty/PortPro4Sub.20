from django.contrib import admin
from django.urls import path, include
from home.views import Index  


urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', Index.as_view(), name='home'),  
    path('tips/', include('Tip.urls')), 
]
from django.urls import path
from .views import search_tip_jar, profile_detail

urlpatterns = [
    path('search/', search_tip_jar, name='search_tip_jar'),
    path('profile/<str:tip_jar_id>/', profile_detail, name='profile_detail'),
]

from django.contrib import admin
from django.urls import path, include
from home import views as home_views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', home_views.search_tip_jar, name='search_tip_jar'),
    path('profile/<str:tip_jar_id>/', home_views.profile_detail, name='profile_detail'),
    path('accounts/', include('allauth.urls')),
    path('', home_views.home_view, name='home'),  # Add this line to handle the root URL
]
