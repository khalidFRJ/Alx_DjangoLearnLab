from django.urls import path
from .views import list_books, LibraryDetailView
views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


from .views import CustomLoginView, CustomLogoutView, SignUpView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register'),
]

from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

# urls.py

from django.urls import path
from .views import admin_view

urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
]


# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]

add_book/", "edit_book/


