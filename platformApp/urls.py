from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('menu/', views.menuPage, name='menuPage'),
    path('about/', views.aboutPage, name='aboutPage'),
    path('lessons/', views.lessonsPage, name='lessonsPage'),
    path('lesson/view/<int:pk>/', views.lessonDetail, name='lessonDetail'),
    path('video-materials/', views.videoPage, name='videoPage'),
    path('video/view/<int:pk>/', views.videoDetails, name='videoDetails'),
    path('presentations/', views.presentations, name='presentations'),
    path('presentation/view/<int:pk>/', views.presentationDetail, name='presentationDetail'),
    path('practice/menu/', views.practiceMenu, name='practiceMenu'),
    path('homeworks/', views.homeWorks, name='homeWorks'),
    path('homework/view/<int:pk>', views.homeWorkDetail, name='homeWorkDetail'),
    path('system/sign-up/', views.signUp, name='signUp'),
    path('system/login/', views.logIn, name='logIn'),
    path('system/user/profile/', views.profilePage, name='profilePage'),
    path('system/logout/', views.logoutUser, name='logoutUser'),
    path('user/change-password/',
         auth_views.PasswordChangeView.as_view(template_name='user/change-password.html', success_url='/'),
         name='change_password'),
]