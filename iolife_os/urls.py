from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render

# Views simples para renderizar os templates novos
def home_view(request): return render(request, 'flow/home.html')
def mylife_view(request): return render(request, 'life/dashboard.html')
def messages_view(request): return render(request, 'nexus/messages.html')
def notifications_view(request): return render(request, 'nexus/notifications.html')
def menu_view(request): return render(request, 'core/menu.html')
def profile_view(request): return render(request, 'core/profile.html')
def mind_view(request): return render(request, 'life/mind.html')
def diary_view(request): return render(request, 'life/diary.html')
def games_view(request): return render(request, 'nexus/games.html')
def marketplace_view(request): return render(request, 'nexus/marketplace.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('life/', mylife_view, name='mylife'),
    path('messages/', messages_view, name='messages'),
    path('notifications/', notifications_view, name='notifications'),
    path('menu/', menu_view, name='menu'),
    path('profile/', profile_view, name='profile'),
    path('mind/', mind_view, name='mind'),
    path('diary/', diary_view, name='diary'),
    path('games/', games_view, name='games'),
    path('marketplace/', marketplace_view, name='marketplace'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)