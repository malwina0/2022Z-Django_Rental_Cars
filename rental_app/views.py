from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import CreateCarForm, RentACarForm, PriceCalculatorForm
from .models import Car


def home(request):
    context = {
        "title": "Malwina Car Rental"
    }
    return render(request, 'home.html', context)


def cars_list(request):
    cars = Car.objects.all()
    context = {
        "cars": cars
    }
    return render(request, "cars.html", context)


def car_retrieve(request, pk):
    car = Car.objects.get(id=pk)
    context = {
        "car": car
    }
    return render(request, "car.html", context)


def car_update(request, pk):
    car = Car.objects.get(id=pk)
    form = CreateCarForm(instance=car)

    if request.method == "POST":
        form = CreateCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect(f"/cars/{pk}/")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    context = {
        "form": form
    }
    return render(request, "car_update.html", context)


def car_delete(request, pk):
    car = Car.objects.get(id=pk)
    car.delete()
    return redirect("/cars")


def rent_a_car(request):
    if request.method == "POST":
        form = RentACarForm(request.POST, request.FILES)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, message='Your form has been send. In next 12 hours we will send you email with '
                                              'confirmation.')
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RentACarForm()

    context = {"form": form,
               "title": "Make a reservation"}
    return render(request, template_name='rent_a_car.html', context=context)


def contact(request):
    context = {
        "title": "Contact"
    }
    return render(request, 'contact.html', context)


def calculate_cost(request):
    if request.method == "POST":
        form = PriceCalculatorForm(request.POST, request.FILES)
        if form.is_valid():
            days = (form.cleaned_data['date_to'] - form.cleaned_data['date_from']).days
            car_price = form.cleaned_data['car'].price
            coupon = form.cleaned_data['coupon']
            price = days * car_price * coupon
            messages.info(request, message=f'Price: {price}')
            return redirect('/price')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = PriceCalculatorForm()

    context = {"form": form,
               "title": "Price calculator"}
    return render(request, template_name='price_calculator.html', context=context)