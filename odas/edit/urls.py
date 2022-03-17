from django.urls import path
from . import views
urlpatterns = [
    path('patient/', views.PatientEditPage.as_view(), name = "p_edit" ),
    path('patient/reports/<int:rep_no>', views.viewReport, name = "vr" ),
]