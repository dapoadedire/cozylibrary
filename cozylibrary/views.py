from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.db.models import Q

# Create your views here.
from . import models


class BookListView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "book_list.html"
    login_url = '/accounts/login/'
    redirect_field_name = 'book:home'
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().filter(status="published").order_by("-views")


class BookDetailView(LoginRequiredMixin, DetailView):
    model = models.Book
    context_object_name = "book"
    template_name = "book_detail.html"
    login_url = '/accounts/login/'


class BookCreateView(LoginRequiredMixin, UserPassesTestMixin,  CreateView):
    model = models.Book
    fields = "__all__"
    template_name = "book_create.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("book:detail", kwargs={"slug": self.object.slug})


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Book
    fields = "__all__"
    template_name = "book_edit.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

    def get_success_url(self):
        return reverse_lazy("book:detail", kwargs={'slug':self.object.slug})


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = models.Book
    template_name = "book_delete.html"
    success_url = reverse_lazy("book:home")


    def test_func(self):
        return self.request.user.is_superuser


class BookGenreView(LoginRequiredMixin, ListView):
    model = models.Book
    context_object_name = "books"
    template_name = "book_genre.html"
    paginate_by = 4
    login_url = '/accounts/login/'

    def get_queryset(self):
        return models.Book.objects.all().filter(genre__icontains=self.kwargs["genre"]).order_by("-views")


class BookSearchView(LoginRequiredMixin, ListView):
    template_name = 'book_search.html'
    model = models.Book 
    login_url = '/accounts/login/'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = models.Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(genre__icontains=query) | Q(description__icontains=query)
        )
        return object_list
        


class AboutView(View):
    
    def get(self, request):
        return render(request, "about.html")


class ProfileView(View):
    def get(self, request):
        return render(request, "profile.html")



def custom_page_not_found_view(request, exception = None):
    return render(request, "errors/404.html", {}, status=404)

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {}, status=500)

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {}, status=403)

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {}, status=400)