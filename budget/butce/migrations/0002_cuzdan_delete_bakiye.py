# Generated by Django 4.0.5 on 2022-06-20 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuzdan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('budget', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bakiye',
        ),
    ]