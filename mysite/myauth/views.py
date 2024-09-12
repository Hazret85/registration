from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import CreateView, UpdateView, DetailView, ListView

from .forms import ProductForm
from .models import Product
from django.contrib.auth.mixins import  LoginRequiredMixin, UserPassesTestMixin


# class RegisterView(CreateView):
#     form_class = UserCreationForm
#     template_name = 'myauth/register.html'
#     success_url = reverse_lazy('login')
#
#     def form_valid(self, form):
#         valid = super().form_valid(form)
#         username = form.cleaned_data.get('username')
#         messages.success(self.request, f'Ваш аккаунт создан: {username}!')
#         return valid


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myauth/register.html', {'form': form})


def profile(request):
    return render(request, 'myauth/profile.html')

class ProductListView(ListView):
    model = Product
    template_name = 'myauth/product_list.html'  # Укажите путь к вашему шаблону
    context_object_name = 'products'

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'myauth/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'myauth/product_form.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.created_by or self.request.user.is_superuser


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'myauth/product_detail.html'



class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')


def read_cookie_view(request):
    cookie_value = request.COOKIES.get('my_cookie', 'Значение по умолчанию')
    return HttpResponse(f'Cookie value: {cookie_value}')


def set_cookie_view(request):
    response = HttpResponse('Cookie установлено!')
    response.set_cookie('my_cookie', 'Some value')
    return response

def read_session_view(request):
    session_value = request.session.get('my_session_key', 'Значение по умолчанию')
    return HttpResponse(f'Session value: {session_value}')


def set_session_view(request):
    request.session['my_session_key'] = 'Some value'
    return HttpResponse('Session установлено!')
