# Generated by Django 2.2.1 on 2019-05-10 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20190510_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(choices=[('Politics', 'Politics'), ('Science', 'Science'), ('Food', 'Food'), ('Technology', 'Technology'), ('Fashion', 'Fashion'), ('Advice', 'Advice'), ('Other', 'Other')], default='Other', max_length=3),
        ),
    ]
