from . import views
from django.urls import path

app_name = "foods"

urlpatterns = [
    path("home/", views.home, name="home"),
    # path('<int:store_pk>/detail', views.detail, name='detail'),
    path('detail', views.detail, name='detail'),
]
