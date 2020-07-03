from django.contrib import admin
from .models import Author, Genre, Book, BookInstance,Post,Choice,contactdata,predict

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'location', 'created_at')
    pass
admin.site.register(Post,PostAdmin)
admin.site.register(Choice)
admin.site.register(Genre)
admin.site.register(predict)
'''
class contactdata(admin.contactdata):
    list_display = ('name', 'email', 'subjet', 'ath')
    pass
admin.site.register(Author, AuthorAdmin)
'''
admin.site.register(contactdata)
# admin.site.register(Book)
# admin.site.register(BookInstance)
#admin.site.register(Author)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    pass
admin.site.register(Author, AuthorAdmin)

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    pass

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter =('status','due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    pass
