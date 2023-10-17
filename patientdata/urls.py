from django.urls import path
from . import views
from .views import generate_excel

urlpatterns = [
    path('patients/', views.PatientListView.as_view(), name='patient-list'),
    path('patients/<int:pk>/', views.PatientDetailView.as_view(), name='patient-detail'),
    path('', views.TestDataListView.as_view(), name='test-data-list'),
    path('generate-excel/', generate_excel, name='generate-excel'),

]

