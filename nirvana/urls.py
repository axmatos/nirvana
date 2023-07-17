from django.urls import path

from nirvana import views

urlpatterns = [
    path('api1/', views.api1, name='api1'),
    path('api2/', views.api2, name='api2'),
    path('api3/', views.api3, name='api3'),
    path('api/', views.api_aggregator, name='api'),
]
