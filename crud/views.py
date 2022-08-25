from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Book
from .forms import BooksForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout, login
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required
# Create your views here.


def homepage(request):
    books_size = len(Book.objects.all())
    book_return = Book.objects.all().order_by("-id")
    return render(request, "crud/home.html", context={
        'book_size': books_size,
        'book_data': book_return
        })


def newbook_create(request):
    if request.method == "POST":
        form = request.POST
        data_dict = {
            "title": form["title"],
            "description": form["description"],
            "pages": form["pages"],
            "price": form["price"],
            "language": form["language"],
        }
        Book.objects.create(**data_dict)
        return redirect(reverse("crud:home"))
    if request.method == "GET":
        form = BooksForm()
    return render(request, "crud/create_new_book.html", context={'form': form})


def bookpage_read_delete(request, id):
    if request.method == "GET":
        book_return = get_object_or_404(Book, pk=id)
        return render(request, "crud/book.html", context={"book": book_return})
    if request.method == "POST":
        book = Book(id=id)
        book.delete()
        return redirect(reverse("crud:home"))
    
    
def book_update(request, id):
    book = Book.objects.filter(id=id)
    if request.method == "POST":
        for book in book:
            form = request.POST
            book.title = form["title"]
            book.description = form["description"]
            book.pages = form["pages"]
            book.price = form["price"]
            book.language = form["language"]
            book.save()
        
        return redirect(reverse("crud:home"))
    if request.method == "GET":
        form = BooksForm()
        
    return render(request, "crud/update_book.html", context={
        "book": book,
        "form": form
        })
    

def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'crud/register.html', context={"form": form})


def register_create(request):
    if request.method != "POST":
        return redirect(reverse('crud:register'))
    
    request.session['register_form_data'] = request.POST
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuario Registrado com Sucesso')
        del (request.session['register_form_data'])
        return redirect(reverse('crud:home'))
    else:
        return redirect(reverse('crud:register'))
    
    
def login_view(request):
    form = LoginForm()
    return render(request, 'crud/login.html', context={'form': form})

def login_create(request):
    if not request.POST:
        raise Http404()
    form = LoginForm(request.POST)
    if form.is_valid():
        authenticate_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', '')
        )
        if authenticate_user is not None:
            messages.success(request, 'You are logged in')
            login(request, authenticate_user)
        else:
            messages.error(request, 'Invalid Credential')
    else:
        messages.error(request, 'Error To validate')
    return redirect(reverse('crud:home'))


@login_required(login_url='crud:login_view')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('crud:home'))
    if request.POST.get('username') != request.user.username:
        return redirect(reverse('crud:home'))
    
    logout(request)
    return redirect(reverse('crud:home'))
        
    
        
        



