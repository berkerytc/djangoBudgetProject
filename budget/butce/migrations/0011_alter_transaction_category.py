# Generated by Django 4.0.5 on 2022-06-27 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('butce', '0010_alter_transaction_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(max_length=150, null=True),
        ),
    ]