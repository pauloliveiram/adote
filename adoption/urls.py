from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_pets, name='list_pets'),
    path('adoption_request/<int:id_pet>', views.adoption_request, name='adoption_request'),
    path('see_adoption_request/', views.see_adoption_request, name='see_adoption_request'),
    path('process_adoption_request/<int:id_request>', views.process_adoption_request, name='process_adoption_request'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('api_adoptions_by_breed/', views.api_adoptions_by_breed, name='api_adoptions_by_breed'),
]
