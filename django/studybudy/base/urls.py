from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_page, name="loginpage"),
    path("logout", views.logout_page, name="logoutpage"),
    path("register", views.register_page, name="register"),
    path("", views.home, name="home"),
    path("createroom", views.create_room, name="createroom"),
    path("updateroom/<str:pk>/", views.update_room, name="updateroom"),
    path("deleteroom/<str:pk>/", views.delete_room, name="deleteroom"),
    path("room/<str:pk>/", views.room, name="room"),
]
