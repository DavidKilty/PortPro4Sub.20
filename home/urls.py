from django.urls import path
from home import views as home_views  # Import your views

urlpatterns = [
    path('', home_views.home, name='home'),  # Root URL
    path('search/', home_views.search_tip_jar, name='search_tip_jar'),
    path('profile/<str:tip_jar_id>/', home_views.profile_detail, name='profile_detail'),
    path('tips/', home_views.tip_list, name='tip_list'),  # Tip list view
]