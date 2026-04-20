from django.urls import path

from cards import views

urlpatterns = [
    path('card/',views.CardCreateList.as_view(),name='cards'),
    path('card/<int:pk>/', views.CardRetrieveUpdateDestroy.as_view(),name='cardsDestroy')
]
