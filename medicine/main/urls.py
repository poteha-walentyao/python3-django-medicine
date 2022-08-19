from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('division', views.index_division),
    path('doctor', views.index_doctor),
    path('client', views.index_client),
    path('post_client', views.index_post_client),
    path('update/<int:id>', views.index_update)
]
