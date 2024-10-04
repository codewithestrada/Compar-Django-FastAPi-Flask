from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import Events
from .forms import EventoForm

# Create your views here.


def get_events(request):
    event = Events.objects.all()
    return render(request, 'events/get_events.html', {'event': event})


def get_by_id(request, id):
    event = get_object_or_404(Events, id=id)
    return render(request, 'events/get_by_id.html', {'event': event})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizador = request.user
            event.save()
            return redirect('get_events')
    else:
        form = EventoForm()
    return render(request, 'events/create_event.html', {'form': form})
