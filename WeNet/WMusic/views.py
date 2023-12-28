from django.shortcuts import redirect, render
from WMusic.models import Music

def index(request):
    musics = Music.objects.all()
    context = {'musics': musics}
    return render(request, 'WMusic/index.html', context)

def edit(request,id):
    if request.method == 'GET':
        music = Music.objects.filter(MusicId=id).first()
        context = {'music': music}
        return render(request, 'WMusic/edit.html', context)
    elif request.method == 'POST':
        music = Music.objects.filter(MusicId=id).first()
        music.MusicName = request.POST['MusicName']
        music.ProposedBy = request.POST['ProposedBy']
        music.Description = request.POST['Description']
        music.save()

        musics = Music.objects.all()
        context = {'musics': musics}
        return render(request, 'WMusic/index.html', context)

def delete(request,id):
    Music.objects.filter(MusicId=id).delete()
    musics = Music.objects.all()
    context = {'musics': musics}
    return render(request, 'WMusic/index.html', context)

from datetime import datetime

def add(request):
    if request.method == 'GET':
        return render(request, 'WMusic/add.html')
    elif request.method == 'POST':
        curId = 1
        if len(Music.objects.all()) > 0:
            curId = 1 + max(music.MusicId for music in Music.objects.all())
        

        new_music = Music.objects.create(MusicId=curId)

        new_music.DateAdded = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        new_music.MusicName = request.POST['MusicName']
        new_music.ProposedBy = request.POST['ProposedBy']
        new_music.Description = request.POST['Description']
        fl = request.FILES
        new_music.MusicFile = fl['MusicFile'] 

        new_music.save()
        # if not new_music.MusicFile: # If the user hasn't uploaded the file, 
        #     return redirect('some-error-page') # redirect to some error page or to the same page with an error message. Or do something else

        musics = Music.objects.all()
        context = {'musics': musics}
        return render(request, 'WMusic/index.html', context)

def details(request,id):
    music = Music.objects.filter(MusicId=id).first()
    context = {'music': music}
    return render(request, 'WMusic/details.html', context)