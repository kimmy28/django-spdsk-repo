# Generated by Django 2.2 on 2019-05-17 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasteweb', '0007_auto_20190518_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='AngkutanSampah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_angkutan_truk', models.CharField(max_length=100)),
                ('deskripsi_angkutan', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='inputop',
            name='nama_angkutan_truk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.AngkutanSampah'),
        ),
        migrations.DeleteModel(
            name='AngkutanTrukSampah',
        ),
    ]
