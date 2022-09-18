from django.contrib import admin
from .models import Book,Category1,Category2,Category3 ,Review

class AdminBook(admin.ModelAdmin):
    list_display = ['title','author','book_available']

class AdminCategory1(admin.ModelAdmin):
    list_display = ['name']

class AdminCategory2(admin.ModelAdmin):
    list_display = ['name']

class AdminCategory3(admin.ModelAdmin):
    list_display = ['name']

class AdminReview(admin.ModelAdmin):
    list_display = ['created','user','comment']



admin.site.register(Category1, AdminCategory1)
admin.site.register(Category2, AdminCategory2)
admin.site.register(Category3, AdminCategory3)

admin.site.register(Book, AdminBook)
admin.site.register(Review, AdminReview)

# admin.site.register(Order)
