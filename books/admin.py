from django.contrib import admin

from .models import Book, Review, Category


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        "category",
        "price",
    )

    search_fields = ("title", "author")

    list_filter = ("category",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
