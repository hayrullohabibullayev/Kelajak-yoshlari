# Generated by Django 4.0.3 on 2022-04-15 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelajak_yoshlariapp', '0003_savollar_savollarga_javob_yozish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatmessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=5000)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
