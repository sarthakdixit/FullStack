from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.info, name='info'),
  path('info_agent', views.infoAgent, name='info_agent'),
  path('info_interior', views.infoInterior, name='info_interior'),
  path('saveToDB', views.saveToDB, name='save_toDB'),
  path('saveAgents', views.saveAgents, name='save_Agents'),
  path('saveInterior', views.saveInterior, name='save_Interior'),
  path('deleteToDB/<str:poll_id>', views.deleteToDB, name='delete_toDB'),
  path('deleteAgent/<str:poll_id>', views.deleteAgent, name='delete_agent'),
  path('deleteInterior/<str:poll_id>', views.deleteInterior, name='delete_interior'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)