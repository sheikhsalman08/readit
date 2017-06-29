# Paste into URLs.py - don't forget to import the Views!
url(r'^review/$', review_books, name='review-books'),
url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),


# Paste into Views.py - don't forget to import get_object_or_404!    
def review_books(request):
	"""
	List all of the books that we want to review.
	"""
	books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
	
	context = {
		'books': books,
	}
	
	return render(request, "list-to-review.html", context)
	
	
def review_book(request, pk):
	"""
	Review an individual book
	"""
	book = get_object_or_404(Book, pk=pk)
	
	context = {
		'book': book,
	}
	
	return render(request, "review-book.html", context)
	
