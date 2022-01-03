# Generated by Django 4.0 on 2022-01-03 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idno', models.IntegerField(unique=True)),
                ('photo', models.FileField(upload_to='productimagess/')),
            ],
        ),
    ]