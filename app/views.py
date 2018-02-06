from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .common.event_parser import get_events
from .common.ical_converter import events_to_ical
from .models import Schedule

def index(request):
    if (request.method == "POST"):
        schedule = request.POST.get('schedule')
        events = get_events(schedule)
        ical_schedule = Schedule.create(events_to_ical(events))
        ical_schedule.save()
        return redirect('get', schedule_id=ical_schedule.uuid)
    return render(request, 'app/index.html')

def get(request, schedule_id):
    schedule = get_object_or_404(Schedule, pk=schedule_id)
    return HttpResponse(schedule.text)
