from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1',include('cards.urls')),
    path('api/v1',include('packs.urls'))
]
