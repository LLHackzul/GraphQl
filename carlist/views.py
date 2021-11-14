from django.shortcuts import render
from .forms import CarForm
# Create your views here.
def car_new(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            Car = form.save(commit=False)
            Car.save()
    else:
        form = CarForm()
    return render(request, 'carlist/car_new.html', {'form': form})