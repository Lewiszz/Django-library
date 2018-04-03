from django.contrib import admin

from .models import Author, Genre, Book, BookInstance

#admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
#admin.site.register(BookInstance)

# Show additional info on all instances of this book
class BooksInline(admin.TabularInline):
    model = Book
    #exclude = ['id']
    extra = 0

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    #fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]

# Show additional info on all instances of this book
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    #exclude = ['id']
    #extra = 0

# Register the Admin classes for Book using the decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'borrower', 'due_back')
    list_filter = ('status', 'due_back')
        
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'borrower', 'due_back')
        }),
    )