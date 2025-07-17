from django.shortcuts import render
from django.views.generic import TemplateView

from books.models import Book

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        top_books = Book.objects.order_by('-rating')  # Top rated books
        context["featured_book"] = top_books.first()  # Pick the best one
        context["top_books"] = top_books[1:5]  # Next 4 top-rated books
        return context

class AboutPageView(TemplateView):
    template_name = "about.html"
