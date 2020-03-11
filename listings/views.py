from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices
from .models import Listing

def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)  # all()

    paginator = Paginator(listings, 3)  # 3 listings per page
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {
        "listings": paged_listings,
        
    }
    return render(request, "listings/listings.html", context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    queryset_list = Listing.objects.order_by("-list_date")

    # keyword, city, are names used in each input of search.html, if they 
    # are filled, the request.GET will have them in it
    # the i in front of icontains, iexact... stands for case insensitive

    # Keywords for description (like '%bla bla bla%')
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City (exact match)
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State (exact match)
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            if state != "State (All)":
                queryset_list = queryset_list.filter(state__iexact=state)

    # bedrooms (less than or equal match)
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            try:
                check_integer = int(bedrooms)
                queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
            except ValueError:
                pass  # ignore non numeric values and show them all

    # price (less than or equal match)
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            try:
                check_integer = int(price)
                queryset_list = queryset_list.filter(price__lte=price)
            except ValueError:
                pass  # ignore non numeric values and show them all

    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "listings": queryset_list,
        "values": request.GET,
    }
    return render(request, "listings/search.html", context)

