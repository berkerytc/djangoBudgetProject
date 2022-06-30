# Generated by Django 4.0.5 on 2022-06-20 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('butce', '0004_rename_amount_cuzdan_budget_alter_cuzdan_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('cuzdan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='butce.cuzdan')),
            ],
        ),
    ]