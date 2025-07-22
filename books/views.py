from django.shortcuts import render, redirect
from django.contrib import messages
from django.core import serializers
from django.urls import reverse_lazy
from django.db.models import Q
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin,
)

from .models import Book, Category, Review
from .forms import ReviewForm
# Create your views here.

class BookListView(LoginRequiredMixin,ListView):
    model = Book
    paginate_by = 8
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
        books = Book.objects.select_related('category').all()
        context["book_data_json"] = serializers.serialize("json", books, use_natural_foreign_keys=True)
        return context


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
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.author = request.user
            review.save()
            messages.success(request, "Review submitted successfully!")
            return redirect("book_detail", pk=self.object.pk)
        context = self.get_context_data()
        context["form"] = form
        return self.render_to_response(context)



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


class EditReviewView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "books/edit_review.html"

    def form_valid(self, form):
        messages.success(self.request, "Review updated successfully!")
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.book.get_absolute_url()

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author


class DeleteReviewView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "books/delete_review.html"

    def get_success_url(self):
        messages.success(self.request, "Review deleted successfully!")
        return self.object.book.get_absolute_url()

    def test_func(self):
        review = self.get_object()
        return self.request.user == review.author
