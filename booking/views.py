from django.shortcuts import render, redirect, get_object_or_404
from .models import Resource, Booking
from .forms import ResourceForm, BookingForm

def resource_list(request):
    # Форма добавления ресурса
    if request.method == 'POST' and 'add_resource' in request.POST:
        form = ResourceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()

    # Форма бронирования
    booking_form = BookingForm()
    if request.method == 'POST' and 'make_booking' in request.POST:
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('resource_list')

    # Удаление ресурса
    if request.method == 'POST' and 'delete_resource' in request.POST:
        resource_id = request.POST.get('delete_resource')
        resource = get_object_or_404(Resource, id=resource_id)
        resource.delete()
        return redirect('resource_list')

    resources = Resource.objects.all()
    bookings = Booking.objects.all()

    return render(request, 'booking/resource_list.html', {
        'resources': resources,
        'form': form,
        'booking_form': booking_form,
        'bookings': bookings,
    })
