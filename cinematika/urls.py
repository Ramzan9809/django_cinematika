from django.contrib import admin
from django.urls import path
from films import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/films/', views.film_list_create_api_view),
    path('api/v1/films/<int:id>/', views.film_detail_api_view)
]