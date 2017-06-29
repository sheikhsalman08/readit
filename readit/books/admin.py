from django.contrib import admin
from .models import Author , Book

class BookAdmin(admin.ModelAdmin):
	fieldsets = [
		("Book Details",{"fields":["title","authors"]}),
		("review",{"fields":["is_favourite","review","reviewed_by","date_reviewed"]}),
	]
	readonly_fields = ("date_reviewed",)
	list_display = ("title","date_reviewed","is_favourite")
	list_editable = ("is_favourite",)
	list_display_links = ("title","date_reviewed")
	list_filter = ("is_favourite",)
	search_fields = ("title","authors__name",)

# Register your models here.
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
