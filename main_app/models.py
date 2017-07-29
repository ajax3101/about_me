from django.db import models


# Create your models here.
class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Edu(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=32)
    region = models.CharField(verbose_name='Регион', max_length=32, blank=True)
    site = models.CharField(verbose_name='Сайт', max_length=64, blank=True)
    position = models.CharField(verbose_name='Должность', max_length=16)
    duties = models.TextField(verbose_name='Обязанности')
    period = models.PositiveIntegerField(verbose_name='Время работы', default=1)


class Skills(models.Model):
    group = models.CharField(verbose_name='Группа', max_length=32)
    categorized = models.CharField(verbose_name='Категория', max_length=32)

    def __str__(self):
        return 'Skills: {}'.format(self.id)


class Qualities(models.Model):
    name_q = models.CharField(verbose_name='Название', max_length=32)
    description_q = models.TextField(verbose_name='Описание')

    def __str__(self):
        return 'Qualities: {}'.format(self.name_q)