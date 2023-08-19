from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from homepage.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import datetime


def autocomplete(request):
    term = request.GET.get('term', '')

    suggestions = {
        'Barishal': '/barishal',
        'Dhaka': '/dhaka',
        'Barishal city': '/barishal-city',
        'Pirojpur': '/pirojpur',
        'Kuakata': '/kuakata',
        'Bhola': '/bhola',
        'Jhalakathi': '/jhalakathi',
        'Patuakhali': '/patuakhali',
        'Mymensingh': '/mymensingh',
        'Sylhet': '/sylhet',
        'Rajshahi': '/rajshahi',
        'Chittagong': '/chittagong',
        'Rangpur': '/rangpur',
        'Khulna': '/khulna',
        'Pyraband': '/pyraband',
    }

    results = []
    for suggestion, url in suggestions.items():
        if term.lower() in suggestion.lower():
            results.append({'label': suggestion, 'value': url})

    data = {
        'results': results
    }

    return JsonResponse(data)


def search(request):
    if request.method == "POST":
        place = request.POST.get('place')
        results = Place.objects.filter(name__icontains = place)
        print(results)
        return render(request, 'division_details.html', {'places':results})
    return redirect('homepage')



def index(request):
    packages = Package.objects.all()
    return render(request, 'index.html', {'packages': packages})
    # return HttpResponse("This is homepge")


def loginpg(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Incorrect password or username')

    return render(request, "login.html")


def register(request):
    form = CreateUserform()
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created successfully")
            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def logoutpg(request):
    logout(request)
    return redirect('login')

@login_required(login_url=('login'))

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,
                          desc=desc)
        contact.save()
        messages.success(request, 'Submitted. Thank You.')
    return render(request, 'contact.html')


def book_now(request):
    return render(request, 'book_now.html')


def confirmation_view(request):
    return render(request, 'confirmation.html')


def ticket(request):
    return render(request, 'ticket.html')


def search_tour_packages(request):
    if request.method == 'POST':
        form = PlaceSearchForm(request.POST)
        if form.is_valid():
            min_price = form.cleaned_data['min_price']
            max_price = form.cleaned_data['max_price']

            if min_price > max_price:
                form.add_error(
                    None, "Minimum price must be less than or equal to the maximum price.")
            else:
                # Perform the database query to find tour packages within the desired price range
                tour_packages = Package.objects.filter(
                    price__gte=min_price, price__lte=max_price)
                if tour_packages.exists():
                    return render(request, 'search_results.html', {'tour_packages': tour_packages})
                else:
                    no_results_msg = "No tour packages found within the specified price range."
                    return render(request, 'search_results.html', {'no_results_msg': no_results_msg})

    else:
        form = PlaceSearchForm()

    return render(request, 'search_form.html', {'form': form})


def divison_details(request, id):
    division = Division.objects.get(id=id)
    places = Place.objects.filter(division=division)
    return render(request, 'division_details.html', {'places': places})


def place_details(request, id):
    place = Place.objects.get(id=id)
    place_culture_photos = PlaceCulture.objects.filter(place=place)
    place_foods = PlaceFood.objects.filter(place=place)
    place_videos = PlaceVideo.objects.filter(place=place)
    hotelslist = []

    hotels = Hotel.objects.filter(place=place)
    guides = Guide.objects.filter(place=place)
    packages = Package.objects.filter(place=place)

    for hotel in hotels:
        hotelinfo = {'info': hotel,
                     'photos': HotelPhoto.objects.filter(hotel=hotel)}
        hotelslist.append(hotelinfo)

    details = {
        'place': place, 'place_culture_photos': place_culture_photos,
        'place_foods': place_foods, 'place_videos': place_videos,
        'hotels': hotelslist, 'guides': guides, 'packages': packages
    }
    return render(request, 'place_details.html', details)


def package_details(request, id):
    package = Package.objects.get(id=id)
    return render(request, 'package_details.html', {"package": package})


def guide_register(request):
    form = GuidesRegisterForm()
    if request.method == "POST":
        form = GuidesRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect('homepage')
        else:
            form = GuidesRegisterForm(request.POST)

    return render(request, 'register_guides.html', {'form': form})

@login_required(login_url=('login'))

def book_package(request, id):
    package = Package.objects.get(id=id)
    user = request.user
    form = PackageBookingForm()
    duration = int(package.duration.split(" ")[0])
    if request.method == 'POST':
        form = PackageBookingForm(request.POST)
        data = form.save(commit=False)
        delta = (data.end_date - data.start_date)
        
        if Booking.objects.filter(package=package):
            messages.warning(
                request, "You Already Booked this package cant book again")
        elif delta.days > duration:
            messages.warning(request, "Package Durations exceed")
        else:
            package.remaining_seats = package.seats - data.persons
            if package.remaining_seats <= 0:
                messages.warning(request, 'No More Seat Available')
            else:
                print(package.remaining_seats)
                package.save()
                booking = Booking(package=package, user=user,
                                  persons=data.persons, number=data.number, start_date = data.start_date,
                                  end_date = data.end_date)
                booking.save()
                messages.success(request, "Package Booked Succefully")
    return render(request, 'package_book.html', {'available': package.remaining_seats, 'form': form})


def add_package(request):
    form = AddPackageForm()
    if request.method == "POST":
        form = AddPackageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Package Added Successfully")
        else:
            form = AddPackageForm(request.POST, request.FILES)
    return render(request, 'addpackage.html', {'form': form})


def guides_list(request):
    guides_list = Guide.objects.all()
    return render(request, 'guides_list.html', {'guides': guides_list})


def delete_guide(request, id):
    guide = Guide.objects.get(id=id)
    guide.delete()
    return redirect('guides_list')


def blog(request):
    blogs = Blog.objects.filter(is_approved = True)
    return render(request, 'blog.html', {'blogs': blogs})

def approve_blog(request):
    blogs = Blog.objects.filter(is_approved = False)
    return render(request, 'pending_blogs.html', {"blogs":blogs})

def approved_blog(request, id):
    blog = Blog.objects.get(id=id)
    blog.is_approved = True
    blog.save()
    return redirect('approve_blogs')

def play_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render(request, 'blog_video.html' , {'blog':blog})


def add_blog(request):
    form = AddBlogForm()
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.author_name = request.user
            data.save() 
            return redirect('homepage')
    return render(request, 'add_blog.html', {'form':form})



def review(request, id):
    package = Package.objects.get(id=id)
    reviews = Review.objects.filter(package=package)
    return render(request, 'review.html', {'reviews':reviews})

@login_required(login_url=('login'))
def add_review(request, id):
    package = Package.objects.get(id = id)
    user = request.user
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.package = package
            data.user = user
            data.save()
            return redirect('review', id)
    return render(request, "add_review.html", {"form":form})

