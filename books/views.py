from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

from .models import Book, Category
from .forms import ReviewForm
# Create your views here.

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    paginate_by = 6
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    login_url = "account_login"

    def get_queryset(self):
        queryset = Book.objects.all()
        category_slug = self.request.GET.get("category")
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category"] = self.request.GET.get('category')
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.author = request.user
            review.save()
            return redirect("book_detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)


class BookDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related("reviews__author",)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context
    

class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get("q")
        return context
