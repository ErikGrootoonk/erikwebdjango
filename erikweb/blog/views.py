from django.shortcuts import render, get_object_or_404
from .models import Post, Book
from django.db.models import Q

def post_list(request):
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/post_detail.html', {'post': post})

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

def book_list(request):
    q = request.GET.get('q', '').strip()          # generic search (titel/author)
    taal = request.GET.get('taal', '').strip()    # exact language match
    # Optional: separate fields for first/last name
    achternaam = request.GET.get('achternaam', '').strip()
    voornaam = request.GET.get('voornaam', '').strip()

    books = Book.objects.all()

    if q:
        books = books.filter(
            Q(titel__icontains=q) |
            Q(voornaam__icontains=q) |
            Q(achternaam__icontains=q) |
            Q(beschrijving__icontains=q)
        )

    if taal:
        books = books.filter(taal__iexact=taal)

    if achternaam:
        books = books.filter(achternaam__icontains=achternaam)

    if voornaam:
        books = books.filter(voornaam__icontains=voornaam)

    # Optional: simple ordering via param, with safelist
    order = request.GET.get('order', '').strip()
    allowed_orders = {'titel', 'achternaam', 'voornaam', '-titel', '-achternaam', '-voornaam'}
    if order in allowed_orders:
        books = books.order_by(order)

    context = {
        'books': books,
        'q': q,
        'taal': taal,
        'achternaam': achternaam,
        'voornaam': voornaam,
        'order': order,
    }
    return render(request, 'blog/books.html', context)