# Generated by Django 4.2.4 on 2023-08-20 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('servico', models.CharField(max_length=50)),
            ],
        ),
    ]
