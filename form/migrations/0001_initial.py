# Generated by Django 4.1.7 on 2023-05-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino'), ('O', 'Otro')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('direccion', models.CharField(max_length=30)),
                ('casa_apto', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=30)),
                ('departamento', models.CharField(max_length=30)),
                ('ciudad', models.CharField(max_length=30)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
