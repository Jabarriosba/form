import datetime
from django import forms
from django.core.exceptions import ValidationError
from form.models import Registro
from django.forms.widgets import DateInput


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = (
            'sexo',
            'fecha_nacimiento',
            'nombre',
            'apellido',
            'email',
            'direccion',
            'casa_apto',
            'pais',
            'departamento',
            'ciudad',
            'descripcion')
        widgets = {
            'fecha_nacimiento': DateInput(attrs={'type': 'date'})
        }

    # metodo para validar si es mayor de 18 y si es una fecha valida
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        today = datetime.date.today()
        age = today.year - fecha_nacimiento.year - (
                (today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if age < 18:
            raise forms.ValidationError('Solo se permite el registro a mayores de 18 años')
        elif age > 100:
            raise forms.ValidationError('Solo se permiten fechas válidas')
        return fecha_nacimiento

    # metodo para validar solo 3 registros por ciudades
    def clean_ciudad(self):
        ciudad = self.cleaned_data['ciudad'].lower()  # convertir a minúsculas para validar ciudad
        if Registro.objects.filter(ciudad=ciudad).count() >= 3:
            raise ValidationError("Se supero el limite de Resgistro para esta ciudad")
        return ciudad
