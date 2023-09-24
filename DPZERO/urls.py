from DPZERO.views import Register,TokenResponse,Storage
from django.urls import path
urlpatterns=[
    path('api/register/',Register.as_view()),
    path('api/token/',TokenResponse.as_view()),
    path('api/storage/',Storage.as_view()),
    path('api/storage/<str:pk>',Storage.as_view()),

]