# Generated by Django 3.1.2 on 2020-10-23 11:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='lent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=10)),
                ('inventory', models.IntegerField()),
                ('provider', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
