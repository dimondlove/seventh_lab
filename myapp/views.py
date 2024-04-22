from django.shortcuts import render
from myapp.models import Student


def index(request):
    """yurec = Student.objects.create(lastname="Руднев", name="Юрий", patronymic="Александрович", birth_year=2002, group="У-226")
    budini = Student.objects.create(lastname="Будков", name="Валерий", patronymic="Валерьевич", birth_year=2002, group="У-234")
    vadim = Student(lastname="Холодов", name="Вадим", patronymic="Сергеевич", birth_year=2002, group="У-226")
    vadim.save()
    kirpich = Student.objects.get_or_create(lastname="Колеменко", name="Андрей", patronymic="Михайлович", birth_year=2002, group="У-205")"""
    students = Student.objects.all()
    return render(request, "index.html", {"students": students})
