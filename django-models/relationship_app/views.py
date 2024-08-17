from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import user_passes_test

from .models import Book, Library
UserCreationForm()", "relationship_app/register.html


# Book-related views
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Library-related views
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User authentication views
class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomLogoutView(LogoutView):
    next_page = '/'


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


# Role-based access control
def is_admin(user):
    return user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.userprofile.role == 'Librarian'


def is_member(user):
    return user.userprofile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')











