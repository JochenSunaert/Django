# Cleaned up imports
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import Article
from .forms import ArticleForm, SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("Form is valid")  # Debug line
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')
        else:
            print(form.errors)  # Debug line to show form errors
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Generic List View
class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'  # Name for the list in the template

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'  # Ensure this path is correct
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('home')  # Redirect to article list after successful creation

    def form_valid(self, form):
        # Automatically assign the current user as the author of the article
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.all()  # Fetch all articles
        context['username'] = self.request.user.username  # Add username to the context
        context['first_name'] = self.request.user.first_name  # Add first name to the context
        context['last_name'] = self.request.user.last_name

        return context
