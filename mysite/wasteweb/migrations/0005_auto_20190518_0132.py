# Generated by Django 2.2 on 2019-05-17 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wasteweb', '0004_inputanop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputanop',
            name='jumlah',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inputbs',
            name='jumlah',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='inputop',
            name='jumlah',
            field=models.IntegerField(),
        ),
    ]
