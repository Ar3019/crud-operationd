from .import views
from django.urls import path
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.loginView, name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.details_form, name= 'detailform'),
    path('<int:id>/', views.details_form, name= 'detailsupdate'),
    path('details/delete/<int:id>/', views.details_delete, name = 'details_delete'),
    path('list/',views.details_list, name='detail'),


]