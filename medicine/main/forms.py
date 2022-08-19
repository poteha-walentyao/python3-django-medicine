from .models import Doctor, Division, Client
from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField


class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = ['name', 'count', 'type']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Введите название'}),
                   'count': TextInput(attrs={'class': 'input', 'placeholder': 'Введите количество мест'}),
                   'type': TextInput(attrs={'class': 'input', 'placeholder': 'Введите тип'})}


class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name', 'post', 'work_exp']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Введите имя'}),
                   'post': TextInput(attrs={'class': 'input', 'placeholder': 'Введите должность'}),
                   'work_exp': TextInput(attrs={'class': 'input', 'placeholder': 'Введите опыт'})}


class ClientForm(ModelForm):
    class Meta:
        model = Client
        division = ModelChoiceField(queryset=Division.objects.all(), empty_label='Выберите страну')
        doctor = ModelChoiceField(queryset=Doctor.objects.all(), empty_label='Выберите достопримечательность')
        fields = ['name', 'age', 'diagnosis', 'division', 'doctor']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Введите имя'}),
                   'age': TextInput(attrs={'class': 'input', 'placeholder': 'Введите возраст'}),
                   'diagnosis': TextInput(attrs={'class': 'input', 'placeholder': 'Введите диагноз'}),
                   }
