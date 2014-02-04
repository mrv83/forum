from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from myforum.forms import NewTheme, NewMessage, NSmile
from myforum.models import Themes, ForumMessages, IconSmiles
from django.core.paginator import Paginator,  PageNotAnInteger, EmptyPage
from forum.settings import MEDIA_ROOT
from django.contrib.auth.decorators import login_required

@login_required
def create_new_theme(request):
    theme = Themes()
    if request.method == "POST":
        nthemes = NewTheme(data=request.POST)
        if nthemes.is_valid():
            theme = nthemes.save(commit=False)
            theme.authuser = request.user
            theme.save()
            return redirect("choozen_theme", theme.id)
    else:
        nthemes = NewTheme()
        return render_to_response('newthemes.html', {'nthemes': nthemes}, context_instance=RequestContext(request))

def page_list(n_page, count_page):
    ind = 0
    if n_page < 6:
        ind = ind + n_page
    else:
        ind = ind + 6
    if count_page - n_page < 6:
        ind = ind + count_page - n_page
    else:
        ind = ind + 5
    p_list = ['' for i in range(0, ind)]

    count = 0
    if n_page < 6:
        for i in range(0, n_page):
            p_list[i] = i+1
            count = i
    else:
        p_list[0] = 1
        p_list[1] = '...'
        for i in range(n_page-4, n_page):
            p_list[6 - n_page + i] = i+1
        count = 5

    if count_page - n_page < 6:
        for i in range(n_page, count_page):
            count = count + 1
            p_list[count] = i+1
    else:
        for i in range(n_page, n_page+4):
            count = count + 1
            p_list[count] = i+1
        p_list[count] = '...'
        p_list[count+1] = count_page
    return (p_list)


def themelist(request):
    themes_list = Themes.objects.all()
    paginator = Paginator(themes_list, 15)
#    p_list = ['' for i in range(paginator.num_pages)]
    page = request.GET.get('page')
    try:
        pthemes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        pthemes = paginator.page(1)
    except EmptyPage:
        pthemes = paginator.page(paginator.num_pages)

    p_l = page_list(pthemes.number, paginator.num_pages)

    return render_to_response('list.html', {"pthemes": pthemes, "p_list": p_l}, context_instance=RequestContext(request))

def choose_themes(request, themes_id):
    ptheme = Themes.objects.get(pk = themes_id)
    message = ForumMessages()
    messages_list = ForumMessages.objects.filter(messtheme = themes_id)
    paginator = Paginator(messages_list, 15)
    page = request.GET.get('page')
    try:
        pmessages = paginator.page(page)
    except PageNotAnInteger:
        pmessages = paginator.page(1)
    except EmptyPage:
        pmessages = paginator.page(paginator.num_pages)

    if request.method == "POST":
        newmess = request.POST.get('newmess')
        if newmess != "":
            message = ForumMessages()
            message.messtext = newmess
            message.messuser = request.user
            message.messtheme = ptheme
            messintheme = ForumMessages.objects.filter(messtheme = themes_id)
            message.messnum = messintheme.count() + 1
            message.save()
            messages_list = ForumMessages.objects.filter(messtheme = themes_id)
            paginator = Paginator(messages_list, 15)
            page = request.GET.get('page')
            try:
                pmessages = paginator.page(paginator.num_pages)
            except PageNotAnInteger:
                pmessages = paginator.page(1)
            except EmptyPage:
                pmessages = paginator.page(paginator.num_pages)

            p_l = page_list(pmessages.number, paginator.num_pages)
            return render_to_response('forum.html',
                                      {"pmessages": pmessages, "ptheme": ptheme, "p_list": p_l},
                              context_instance=RequestContext(request))
    else:
        p_l = page_list(pmessages.number, paginator.num_pages)
        return render_to_response('forum.html',
                                  {"pmessages": pmessages, "ptheme": ptheme, "p_list": p_l},
                              context_instance=RequestContext(request))


# '''def newsetsmiles(request):
#     smiles_list = IconSmiles.objects.all()
#     return render_to_response('newsmiles.html', dict(smiles_list=smiles_list), context_instance=RequestContext(request))
#
# def smileitem_edit(request, iconsmiles_id):
#     choozen_smile = IconSmiles.objects.get(pk = iconsmiles_id)
#     if request.method == "POST":
#         form=NSmile(request.POST, request.FILES, instance=choozen_smile)
#         if form.is_valid():
#             return redirect("newsetupsmiles")
#         else:
#             return render_to_response('smileitem.html', {'form': form, 'choozen_smile': choozen_smile}, context_instance=RequestContext(request))
#     else:
#         form=NSmile(instance=choozen_smile)
#         return render_to_response('smileitem.html', {'form': form, 'choozen_smile': choozen_smile}, context_instance=RequestContext(request))
# #        return HttpResponse("It's work!!!!")
#
# def delsmiles(request):
#     if request.method == "POST":
#         ind = request.POST.get('index')
#         IconSmiles.objects.get(pk = int(ind)).delete()
#         return redirect("newsetupsmiles")
#     else:
#         return HttpResponse("It wrong request!!!!")
#
# def addsmiles(request):
#     if request.method == "POST":
#         form=NSmile(request.POST, request.FILES)
#         if form.is_valid():
#             choozen_smile = form.save()
#             return redirect("smileitem_edit", choozen_smile.id)
#         else:
#             return render_to_response('addsmile.html', {'form': form}, context_instance=RequestContext(request))
#     else:
#         form=NSmile()
#         return render_to_response('addsmile.html', {'form': form}, context_instance=RequestContext(request))
# '''

def handle_uploaded_file(f):
    fullpath = MEDIA_ROOT+'smileicon/'+f.name
    destination = open(fullpath, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def setsmiles(request):
    if request.POST:
        count = int(request.POST.get('form_count'))
# Read <input type="file"... , upload files and push name of this file in array
#         class file_object(object):
#             ind = 0
#             fname = ''
#        f_list = [file_object() for i in range(count)]
        f_list = ['' for i in range(count)]
        arrkey = request.FILES.keys()
        for key in arrkey:
            index = key
            index = int(index.replace("filesmile",""))
            f = request.FILES[key]
            f_list[index] = 'smileicon/'+f.name
            handle_uploaded_file(f)

# Read other POST data
        view_list = request.POST.getlist('viewsmile')
        id_list = request.POST.getlist('idsmile')
        for x in range(0, count):
            id_list[x] = int(id_list[x])

#Delete deleted record
        Elements=IconSmiles.objects.values_list("id", flat=True)
        for elm in Elements:
            if elm not in id_list:
                IconSmiles.objects.get(pk=elm).delete()

        for x in range(0, count):
#update existed record
            if id_list[x] != 0:
#by file
                if f_list[x] != "":
                    objISmiles = IconSmiles.objects.get(pk=id_list[x])
                    objISmiles.smileicon = f_list[x].fname
                    objISmiles.save()
#by view
                smileview_list=IconSmiles.objects.values_list("smileview", flat=True)
                if (view_list[x] not in smileview_list)and(view_list[x] != ""):
                    objISmiles = IconSmiles.objects.get(pk=id_list[x])
                    objISmiles.smileview= view_list[x]
                    objISmiles.save()
#if record not exist
            else:
                smileview_list=IconSmiles.objects.values_list("smileview", flat=True)
                if (f_list[x] !='')and(view_list[x] not in smileview_list)and(view_list[x] != ""):
                    objISmiles = IconSmiles()
                    objISmiles.smileicon = f_list[x]
                    objISmiles.smileview = view_list[x]
                    objISmiles.save()

        items = IconSmiles.objects.all()
        return render_to_response('smiles.html', dict(forms=items), context_instance=RequestContext(request))
    else:
        items = IconSmiles.objects.all()
        return render_to_response('smiles.html', dict(forms=items), context_instance=RequestContext(request))
