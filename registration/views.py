from django.http import HttpResponse
from django.shortcuts import render_to_response
from registration.models import Person
from registration.forms import RegisterUser, RegisterPerson
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime, calendar
from forum.settings import MEDIA_ROOT

def handle_uploaded_file(f):
    fullpath = MEDIA_ROOT+'avatars/'+f.name
    destination = open(fullpath, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

# Login/logout of users
def login_user(request):
    if request.user.is_authenticated():
        if ('username' in request.REQUEST) and ('password' in request.REQUEST):
            pass
        else:
            logout(request)
    else:
        if ('username' in request.REQUEST) and ('password' in request.REQUEST):
            username = request.REQUEST['username']
            password = request.REQUEST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def reg_new_user(request):
    user = User()
    person = Person()
    if request.method == "POST":
        uform = RegisterUser(data=request.POST)
        pform = RegisterPerson(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            person = pform.save(commit=False)
            person.user = user
            person.save()
            return HttpResponse("It's work!")
    else:
        uform = RegisterUser()
        pform = RegisterPerson()
        return render_to_response('reg_form.html', {'uform': uform, 'pform': pform},
                                  context_instance=RequestContext(request))

@login_required
def profile(request):
    user = request.user
    person = request.user.get_profile()
    now = datetime.datetime.now()
    y_list = [i for i in range(int(now.year), int(now.year)-100, -1)]
    m_list = [(i, calendar.month_name[i]) for i in range(1, 13)]
    d_list = [i for i in range(1, 32)]

    if request.method == "POST":
        email = request.POST.get('email_input')
        if email != '':
            user.email = email
        fname = request.POST.get('fname_input')
        if fname != '':
            user.first_name = fname
        lname = request.POST.get('lname_input')
        if lname != '':
            user.last_name = lname
        user.save()
        year = request.POST.get("year_input")
        month = request.POST.get("month_input")
        if len(month) == 1:
            month = '0'+month
        day = request.POST.get("day_input")
        if len(day) == 1:
            day = '0'+day
        person.birthday = year+"-"+month+"-"+day
        mobilenum = request.POST.get("tel_input")
        if mobilenum != "":
            person.mobilenum = mobilenum
        fromuser = request.POST.get("from_input")
        if fromuser != "":
            person.fromuser = fromuser
        slogan = request.POST.get("slogan_input")
        if slogan != "":
            person.slogan = slogan



        person.save()
        return render_to_response('profile.html', {'u': request.user, 'p': person, 'y_list': y_list, 'm_list': m_list,
                                                   'd_list': d_list}, context_instance=RequestContext(request))
    else:

        return render_to_response('profile.html', {'u': request.user, 'p': person, 'y_list': y_list, 'm_list': m_list,
                                                   'd_list': d_list}, context_instance=RequestContext(request))
