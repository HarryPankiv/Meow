from django.shortcuts import render, get_object_or_404
from django.shortcuts import render_to_response

#from .models import Article
#from .forms import RoomForm
from django.shortcuts import redirect
from django.http import HttpResponse

import json



# Create your views here.

def start_page(request):
    #rooms = Room.objects.all()
    context = {
        'rooms': "dota",
    }
    return render(request, 'news_explorer/default.html', context)