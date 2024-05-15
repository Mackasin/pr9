from django.urls import path
from firstapp import views

urlpatterns = [
    path(r'', views.HomePageView.as_view(), name='home'),
]
