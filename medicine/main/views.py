from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render
from .forms import DivisionForm, DoctorForm, ClientForm
from .models import Division, Doctor, Client


def index(request):
    return render(request, 'main/index.html')


def index_division(request):
    if request.method == 'POST':
        form = DivisionForm(request.POST)
        if form.is_valid():
            pre_save = form.save(commit=False)
            name = form.cleaned_data.get('name')
            flag = 0
            bd_division = Division.objects.all()
            for division in bd_division:
                if division.name == name:
                    flag = 1
            if flag == 0:
                pre_save.save()
        error = 'Неправильно введены данные'
    form = DivisionForm()
    error = ''
    context = {
        'form': form,
        'error': error
    }

    return render(request, 'main/division.html', context)


def index_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            pre_save = form.save(commit=False)
            name = form.cleaned_data.get('name')
            flag = 0
            bd_doctor = Doctor.objects.all()
            for doctor in bd_doctor:
                if doctor.name == name:
                    flag = 1
            if flag == 0:
                pre_save.save()
        error = 'Неправильно введены данные'
    form = DoctorForm()
    error = ''
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/doctor.html', context)


def index_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
        error = 'Неправильно введены данные'
    form = ClientForm()
    error = ''
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/client.html', context)


def index_update(request, id):
    try:
        all_division = Division.objects.all()
        all_doctor = Doctor.objects.all()
        client = Client.objects.get(id=id)
        if request.method == "POST":
            client.name = request.POST.get("name")
            client.age = request.POST.get("age")
            client.diagnosis = request.POST.get("diagnosis")
            client.division = Division.objects.get(id=request.POST.get("division"))
            client.doctor = Doctor.objects.get(id=request.POST.get("doctor"))
            client.save()
            return HttpResponseRedirect("/post_client")
        else:
            return render(request, 'main/update.html', {'client': client,
                                                        'all_division': all_division,
                                                        'all_doctor': all_doctor})
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Не найдена запись</h2>")


def index_post_client(request):
    client = Client.objects.all()
    return render(request, 'main/post_client.html', {'client': client})
