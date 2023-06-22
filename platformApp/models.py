from django.db import models
from datetime import datetime
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class LessonLecture(models.Model):
    title = models.CharField("Тема урока", max_length=255)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    content = HTMLField("Описание")

    def __str__(self):
        return self.title

    def get_absolute_url(self, pk):
        return reverse("lessonDetail", args=[self.pk])

    class Meta:
        db_table = 'lessons'
        verbose_name = "Лекция"
        verbose_name_plural = "Лекции"

class VideoMaterial(models.Model):
    lessonName = models.CharField("Тема урока", max_length=255)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    video = models.FileField("Видео файл (mp4)", upload_to="materials/video/")

    def __str__(self):
        return self.lessonName

    def get_absolute_url(self, pk):
        return reverse("videoMaterialDetail", args=[self.pk])

    class Meta:
        db_table = 'videomaterials'
        verbose_name = "Видео"
        verbose_name_plural = "Видео материалы"

class HomeWork(models.Model):
    title = models.CharField("Тема домашнего задания", max_length=255)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    content = HTMLField("Описание выполнения работы")

    def __str__(self):
        return self.title

    def get_absolute_url(self, pk):
        return reverse("homeWorkDetail", args=[self.pk])

    class Meta:
        db_table = 'homeworks'
        verbose_name = "Домашняя работа"
        verbose_name_plural = "Домашние задания"

class PushHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ученик/ца")
    homeWork = models.ForeignKey(HomeWork, on_delete=models.CASCADE, verbose_name="Задание #")
    solution = models.FileField("Файл", upload_to="materials/homeWorks/")

    def __str__(self):
        return self.student.username

    class Meta:
        verbose_name = "Отправленная работы"
        verbose_name_plural = "Отправленные работы"

class GradeHomework(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ученик/ца")
    homeWork = models.ForeignKey(HomeWork, on_delete=models.CASCADE, verbose_name="Задание #")
    grade = models.IntegerField("Оценка", max_length=255)
    postDate = models.DateTimeField("Дата и время", default=datetime.now)
    def __str__(self):
        return self.student.username

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"

class Presentaion(models.Model):
    lessonTheme = models.CharField("Тема урока", max_length=255)
    presentationUrl = models.CharField("Ссылка презентации", max_length=500)
    def __str__(self):
        return self.lessonTheme

    def get_absolute_url(self, pk):
        return reverse("presentationDetail", args=[self.pk])

    class Meta:
        db_table = 'presentations'
        verbose_name = "Презентация"
        verbose_name_plural = "Презентации"




class MainPage(models.Model):
    content = models.TextField("Описание главной страницы")
    firstBlock = models.CharField("1-блок", max_length=255, null=True, blank=True, default="")
    secondBlock = models.CharField("2-блок", max_length=255, null=True, blank=True, default="")
    thirdBlock = models.CharField("3-блок", max_length=255, null=True, blank=True, default="")
    fourthBlock = models.CharField("4-блок", max_length=255, null=True, blank=True, default="")
    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главная страница"

    def __str__(self):
        return self.content


class AboutPage(models.Model):
    content = models.TextField("Описание страницы о проекте")

    class Meta:
        verbose_name = "Cтраница О проекте"
        verbose_name_plural = "Cтраница О проекте"

    def __str__(self):
        return self.content


