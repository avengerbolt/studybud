from django.shortcuts import render
from .models import Room
from .forms import RoomForm


# rooms = [
#     {'id':1, 'name':'Learn Python'},
#     {'id':2, 'name':'Learn Django'},
#     {'id':3, 'name':'Play with javascript'},
# ]

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    context={'rooms':rooms}
    return render(request, 'base/home.html',context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html', context)

def create_room(request):
    form = RoomForm()
    context = {'form':form}
    return render(request, 'base/room_form.html', context)
