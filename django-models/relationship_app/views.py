from django.shortcuts import render
from .models import Book
from django.contrib.auth import login
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'

UserCreationForm()", "relationship_app/register.html
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    next_page = '/'

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'


from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

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
    
def is_admin(user):
    return user.userprofile.role == 'Admin'

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'admin_view.html')






