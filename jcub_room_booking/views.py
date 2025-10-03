from django.shortcuts import render

def index(request):
    return render(request, "jcub_room_booking/index.html")
