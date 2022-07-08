from django.contrib import admin
from django.urls import path
from . import views

app_name = "book"

urlpatterns = [
    path("", views.BookListView.as_view(), name="home"),
    path("book/<slug:slug>/", views.BookDetailView.as_view(), name="detail"),
    path("new/", views.BookCreateView.as_view(), name="create"),
    path("book/<slug:slug>/update/", views.BookUpdateView.as_view(), name="update"),
    path("book/<slug:slug>/delete/", views.BookDeleteView.as_view(), name="delete"),
     path("search/", views.BookSearchView.as_view(), name="search"),
    path("genre/<str:genre>/", views.BookGenreView.as_view(), name="genre"),
    path("about/", views.ProfileView.as_view(), name="profile"),
    path("profile/", views.AboutView.as_view(), name="about"),
]



admin.site.site_header = "Cozy Library Dashboard"
admin.site.site_title = "Cozy Library"
admin.site.index_title = "Welcome to the Cozy Library"
