from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def homePage(request):
    content = MainPage.objects.all()
    return render(request, "site/home.html", {
        'content': content
    })

def menuPage(request):
    return render(request, "site/menu.html")

def aboutPage(request):
    content = AboutPage.objects.all()
    return render(request, "site/about.html", {
        'content': content
    })

def lessonsPage(request):
    lessons = LessonLecture.objects.all()
    return render(request, "site/lessons.html", {
        'lessons': lessons
    })

def lessonDetail(request, pk):
    lesson = get_object_or_404(LessonLecture, pk=pk)
    lessonThemes = LessonLecture.objects.all()
    return render(request, "site/lesson-detail.html", {
        'lesson': lesson,
        'lessonThemes': lessonThemes
    })

def videoPage(request):
    videos = VideoMaterial.objects.all()
    return render(request, "site/video-materials.html", {
        'videos': videos
    })

def videoDetails(request, pk):
    video = get_object_or_404(VideoMaterial, pk=pk)
    videoPlaylist = VideoMaterial.objects.all()
    return render(request, "site/video-material-detail.html", {
        'video': video,
        'videoPlaylist': videoPlaylist
    })


def practiceMenu(request):
    return render(request, "site/practice-menu.html")

def homeWorks(request):
    homeWorks = HomeWork.objects.all()
    return render(request, "site/home-works.html", {
        'homeWorks': homeWorks
    })

def homeWorkDetail(request, pk):
    homeWork = get_object_or_404(HomeWork, pk=pk)
    homeWorks = HomeWork.objects.all()
    return render(request, "site/home-work-detail.html", {
        'homeWorks': homeWorks,
        'homeWork': homeWork
    })

'''
def userTickets(request):
    user = request.user
    userTickets = Ticket.objects.filter(user=user).order_by('-ticketDate')
    return render(request, "site/user-tickets.html", {
        'user': user,
        'userTickets': userTickets
    })
'''

def presentations(request):
    presentations = Presentaion.objects.all()
    return render(request, "site/presentations.html", {
        'presentations': presentations
    })

def presentationDetail(request, pk):
    presentation = get_object_or_404(Presentaion, pk=pk)
    presentations = Presentaion.objects.all()
    return render(request, "site/presentation-detail.html", {
        'presentation': presentation,
        'presentations': presentations
    })

def signUp(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно прошли регистрацию")
            return redirect("homePage")
        messages.error(request, "Что-то пошло не так :(")
    else:
        form = NewUserForm()
    return render(request, "user/sign-up.html", {
        'form': form
    })

def logIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Здравствуйте, {username}.")
                return redirect("homePage")
            else:
                messages.error(request, "Неверный логин или пароль")
        else:
            messages.error(request, "Неверный логин или пароль")
    else:
        form = AuthenticationForm()
    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    messages.info(request, "Вы вышли из системы")
    return redirect("homePage")

def profilePage(request):
    return render(request, "user/profile.html")
