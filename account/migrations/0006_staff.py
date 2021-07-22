# Generated by Django 3.2.5 on 2021-07-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_user_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('position', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Public Health Officer', 'Public Health Officer'), ('Cleaner', 'Cleaner'), ('Security', 'Security'), ('Driver', 'Driver'), ('Counselor', 'Counselor'), ('Nutritionist', 'Nutritionist')], max_length=100)),
                ('employment_date', models.DateTimeField()),
                ('shift', models.CharField(choices=[('Day', 'Day'), ('Night', 'Night')], max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
