from django.urls import path
from django.utils.regex_helper import normalize
from .views import LeadDetailView,LeadListView,LeadDetailView,LeadCreateView,LeadDeleteView,LeadUpdateView


app_name = "leads"

urlpatterns = [
    path('',LeadListView.as_view(),name="lead-list"), 
    path('<int:pk>/',LeadDetailView.as_view(),name="lead-detail"),
    path('<int:pk>/update/',LeadUpdateView.as_view(),name="lead-update"),
    path('<int:pk>/delete/',LeadDeleteView.as_view(),name="lead-delete"),
    path('create/',LeadCreateView.as_view(),name="lead-create"),
    
]