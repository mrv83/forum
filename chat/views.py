from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.paginator import Paginator,  PageNotAnInteger, EmptyPage
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.shortcuts import render
from django.forms.models import model_to_dict
from forum.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required
from chat.models import ChatChannels, ActiveUsers, ChatBannedUser, ChatMessages, ChatModerators
import datetime

def chat(request):
    channel = 1
    allchannels = ChatChannels.objects.values_list("id", "channelname")
    messages = ChatMessages.objects.all().filter(chatchannel = channel)
    if messages.count()>100:
        channelmessages = messages[messages.count()-100:messages.count()]
    else:
        channelmessages = messages
    return render_to_response('chat_channels.html', {'allchannels': allchannels, 'messages': messages,
                                                     'channel': channel}, context_instance=RequestContext(request))

def create_channel(request):
    if request.method == 'POST':
        channel_name = request.POST.get('new_channel_name_input')
        channel_password = request.POST.get('new_channel_password_input')
        new_channel = ChatChannels()
        all_channel_name = ChatChannels.objects.values_list("channelname", flat=True)
        if channel_name not in all_channel_name:
            new_channel.channelname = channel_name
# Here must be add invition for choozen people
            if channel_password != "":
                new_channel.channelpassword = channel_password
            new_channel.user = request.user
            new_channel.save()
            new_moderator = ChatModerators()
            new_moderator.chatchannel = new_channel
            new_moderator.user = request.user
            new_moderator.save()
        return render_to_response('chat_channels.html', context_instance=RequestContext(request))
    else:
#        opponents = Opponents.object.all(filter(user = request.user))
        allusers = User.objects.all()
        return render_to_response('create_channel.html', {'allusers': allusers},
                                  context_instance=RequestContext(request))

def channel_list(request):
    pass

def channel_X(request, channel):
    if request.method == "POST":
        pass
    else:
        allchannels = ChatChannels.objects.values_list("id", "channelname")
        messages = ChatMessages.objects.all().filter(chatchannel=channel)
        if messages.count()>100:
            channelmessages = messages[messages.count()-100:messages.count()]
        else:
            channelmessages = messages
        return render_to_response('chat_channels.html', {'allchannels': allchannels, 'messages': messages,
                                                     'channel': int(channel)}, context_instance=RequestContext(request))

def add_message(request):
    if request.is_ajax():
        newmessage = ChatMessages()
        dt = request.POST.get('dt')
        st = request.POST.get('st')
        cn = request.POST.get('cn')
        user = request.user
        newmessage.user = user
        newmessage.chatchannel = ChatChannels.objects.get(pk=cn)
        newmessage.textmessage = st
#        newmessage.themecreateddata = datetime
        newmessage.save()
        return HttpResponse('1')