from django.db import models


class Division(models.Model):
    name = models.TextField('Отдел')
    count = models.TextField('Количество мест')
    type = models.TextField("Тип")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class Doctor(models.Model):
    name = models.TextField('Имя')
    post = models.TextField('Должность')
    work_exp = models.TextField('Опыт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Врач'
        verbose_name_plural = 'Врачи'


class Client(models.Model):
    name = models.TextField('Имя')
    age = models.TextField('Возраст')
    diagnosis = models.TextField('Диагноз')
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пациент'
        verbose_name_plural = 'Пациенты'
