from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('add/',views.AddView.as_view(), name='add'), # http://127.0.0.1:8000/add/
    path('update/<int:pk>/',views.UpdateView.as_view(), name='update'),# http://127.0.0.1:8000/update/
    path('delete/<int:pk>/',views.DeleteView.as_view(), name='delete'),# http://127.0.0.1:8000/delete/
]
