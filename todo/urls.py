from django.urls import path
from todo import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("lists/", views.TodoListView.as_view(), name='todo-list'),
]

htmx_url_patterns = [
    path('check_username/', views.check_username, name='check-username'),
    path('add-list/', views.add_list, name='add-list'),
    path('delete-list/<int:pk>/', views.delete_list, name='delete-list'),
]

urlpatterns += htmx_url_patterns