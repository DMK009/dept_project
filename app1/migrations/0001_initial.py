# Generated by Django 3.2.9 on 2021-11-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyname', models.CharField(max_length=30)),
                ('deptname', models.CharField(choices=[['IT', 'It'], ['ELECTRICAL', 'Electrical'], ['MECHANICAL', 'Mechanical']], max_length=20)),
                ('doj', models.DateField()),
            ],
        ),
    ]