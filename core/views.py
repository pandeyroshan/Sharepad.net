from django.shortcuts import render,redirect
from .models import ChatRoom,TextBook
# Create your views here.

def index(request):
    if request.method == 'POST':
        all_room = ChatRoom.objects.all()
        room_object = None
        for room in all_room:
            if room.chatroom_id == request.POST.get('chatroom'):
                room_object = room
        if not room_object:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            room_object = ChatRoom.objects.create(ip_address=ip,chatroom_id=request.POST.get('chatroom'))
            room_object.save()
            URL = 'my_room/'+str(room_object.chatroom_id)
            return redirect(URL)
    return render(request,'core/index.html')

def open_room(request,room_id):
    try:
        room = ChatRoom.objects.get(chatroom_id=room_id)
        files = TextBook.objects.filter(chatroom=room)
        context = {
            'room' : room,
            'files' : files
        }
        return render(request,'core/book.html',context)
    except:
        return render(request,'core/404.html')


def test(request):
    return render(request,'core/book.html')


def add_file(request,id):
    if request.method == 'POST':
        file = TextBook.objects.create(chatroom=ChatRoom.objects.get(id=request.POST.get('room_id')),book_name=request.POST.get('filename'))
        file.save()
        URL = '/my_room/'+str(ChatRoom.objects.get(id=request.POST.get('room_id')).chatroom_id)
        print(URL)
        return redirect(URL)
    context = {
        'room' : ChatRoom.objects.get(id=id)
    }
    return render(request,'core/add_file.html',context)

def delete_room(request,id):
    ChatRoom.objects.get(id=id).delete()
    return redirect('/')