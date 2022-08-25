from django.urls import path
from .views import book_update, bookpage_read_delete, homepage, newbook_create, register, register_create
app_name = "crud"

urlpatterns = [
    path("", homepage, name="home"),
    path("book/<int:id>/", bookpage_read_delete, name="bookpage"),
    path("book/create/", newbook_create, name="createbook"),
    path("book/update/<int:id>/", book_update, name="updatebook"),
    path('writer/register', register, name="register"),
    path('writer/register_create', register_create, name="register_create"),
    path('writer/login', register, name="login"),
    path('writer/login_create', register_create, name="login_create")
    ]