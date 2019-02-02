from django.urls import path
from .views import HomePageView, ChartData

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('api/chart/data/', ChartData.as_view())
]
