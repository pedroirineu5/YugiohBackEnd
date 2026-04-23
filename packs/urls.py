from . import views
from django.urls import path

urlpatterns = [
    path('packs/', views.PacksCreateListView.as_view(), name='pack_get'),
    path('packs/<int:pk>',views.PacksRetrieveUpdateDestroy.as_view(), name='packs_id'), 
]