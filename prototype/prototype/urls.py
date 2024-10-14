"""
URL configuration for prototype project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp.views import ArticleListView, ArticleDetailView, ArticleCreateView, HomePageView, sign_up 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', HomePageView.as_view(), name='home'),  # HomePageView for homepage
    path('articles/', ArticleListView.as_view(), name='article_list'),  # Article list
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),  # Article detail
    path('article/new/', ArticleCreateView.as_view(), name='article_create'),  # Create new article
    path('signup/', sign_up, name='signup'),
]
