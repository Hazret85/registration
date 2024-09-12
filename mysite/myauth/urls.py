from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    CustomLogoutView,
    read_cookie_view,
    set_cookie_view,
    read_session_view,
    set_session_view,
    register,
    profile,
    ProductCreateView,
    ProductUpdateView, ProductListView,
)


urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='myauth/login.html',
        redirect_authenticated_user=True
    ), name='login'),

    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),

    path('products/', ProductListView.as_view(), name='product_list'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),

    path('cookie/read/', read_cookie_view, name='read_cookie'),
    path('cookie/set/', set_cookie_view, name='set_cookie'),

    path('session/read/', read_session_view, name='read_session'),
    path('session/set/', set_session_view, name='set_session'),
]
