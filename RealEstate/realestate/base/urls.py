from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.getIndex, name='index'),
    path('flat', views.flat, name='flat'),
    path('villa/', views.villa, name='villa'),
    path('plot/', views.plot, name='plot'),
    path('commercial/', views.commercial, name='commercial'),
    path('farm/', views.farm, name='farm'),
    path('interior/', views.interior, name='interior'),
    path('agents/', views.agents, name='agents'),
    path('fulldata/<str:id>', views.fullData, name='fulldata'),
    path('interior/showInterior/<str:id>', views.showInterior, name='showInterior'),
    path('agents/showAgents/<str:id>', views.showAgents, name='showAgents'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)