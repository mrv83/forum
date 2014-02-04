from django.shortcuts import render_to_response
from registration.views import login_user
from myforum.views import themelist, create_new_theme, choose_themes

def home(request):
    login_user(request)
    themelist(request)
    return render_to_response('index.html')