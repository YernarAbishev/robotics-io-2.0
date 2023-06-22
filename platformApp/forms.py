from django import forms
from .models import *
from tinymce.models import HTMLField
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LessonLectureForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))
    class Meta:
        model = LessonLecture
        fields = ('title', 'content')

class VideoMaterialForm(forms.ModelForm):
    class Meta:
        model = VideoMaterial
        fields = ('lessonName', 'video')

class HomeWorkForm(forms.ModelForm):
    content = forms.CharField(label="Описание", widget=TinyMCE(attrs={'cols': 50, 'rows': 10}))
    class Meta:
        model = HomeWork
        fields = ('title', 'content')

class PushHomeworkForm(forms.ModelForm):
    class Meta:
        model = PushHomework
        fields = ('student', 'homeWork', 'solution')

class GradeHomeworkForm(forms.ModelForm):
    class Meta:
        model = GradeHomework
        fields = ('student', 'homeWork', 'grade')

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user