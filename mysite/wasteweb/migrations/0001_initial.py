# Generated by Django 2.2 on 2019-05-17 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AngkutanSampah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_angkutan', models.CharField(max_length=100)),
                ('deskripsi_angkutan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LokasiKecamatan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_lokasi_kec', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sampah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_sampah', models.CharField(max_length=100)),
                ('kategori_sampah', models.CharField(max_length=100)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InputOP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(max_length=100)),
                ('jam', models.TimeField(max_length=100)),
                ('jumlah', models.IntegerField(help_text='in kg')),
                ('nama_angkutan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.AngkutanSampah')),
                ('nama_lokasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.LokasiKecamatan')),
                ('nama_sampah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.Sampah')),
            ],
        ),
        migrations.CreateModel(
            name='InputBS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(max_length=100)),
                ('jumlah', models.IntegerField(help_text='in kg')),
                ('nama_lokasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.LokasiKecamatan')),
                ('nama_sampah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wasteweb.Sampah')),
            ],
        ),
    ]