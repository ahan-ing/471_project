from .models import Place, Division, Package

def all_places(request):
    places = Place.objects.filter(add_to_nav = True)
    return {'all_places': places}

def all_divisions(request):
    divisions = Division.objects.all()
    return {"all_divisions":divisions}

def all_packages(request):
    packages = Package.objects.all()
    return {'all_package':packages}