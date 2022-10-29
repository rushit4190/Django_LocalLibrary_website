from django.contrib import admin

# Register your models here.

from .models import Book, BookInstance, Genre, Language,Author

#admin.site.register(Book)
#admin.site.register(BookInstance)
admin.site.register(Language)
admin.site.register(Genre)
#admin.site.register(Author)

class BooksInline(admin.TabularInline):
    """Defines format of inline book insertion (used in AuthorAdmin)"""
    model = Book
    extra = 0


# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # to change view of input form of Author model
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    inlines = [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

# to add associated records info along with the main info. For e.g we added BookInstance information inline to our Book detail by specifying inlines in your BookAdmin.
class BookInstanceInline(admin.TabularInline):
    model = BookInstance

    extra = 0

# Register the Admin classes for Book using the decorator
# @admin.register(Book) this does exactly the same thing as the admin.site.register() syntax
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')

    inlines = [BookInstanceInline]
    pass

# Register the Admin classes for BookInstance using the decorator
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower','due_back', 'id')
    list_filter = ('status', 'due_back')

    # to add "sections" to group related model information within the detail form
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

