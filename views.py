from django.shortcuts import render,redirect
# Create your views here.
from events.models import Events
from .forms import EventForm

def event_create_view(request):
	form  = EventForm(request.POST or None)
	if form.is_valid():
		form.save()
		form  = EventForm()
	context ={
	  'form': form
	}
	return render(request, 'events/event_create_view.html', context)

def event_details_view(request, id):
	obj = Events.objects.get(id=id)
	#context ={
	#    'Title' : obj.Title,
	#     'Coordinator' : obj.Coordinator,
	#}
	context ={
	  'object': obj
	}
	return render(request, "events/details.html", context)

def event_list_view(request):
	queryset = Events.objects.all()
	context ={
	      'object_list': queryset
	}
	return render(request, 'events/event_list_view.html', context)
