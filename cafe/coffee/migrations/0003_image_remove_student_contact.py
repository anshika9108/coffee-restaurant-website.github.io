# Generated by Django 4.1.3 on 2023-02-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_wanguser_alter_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='myimage')),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='contact',
        ),
    ]
