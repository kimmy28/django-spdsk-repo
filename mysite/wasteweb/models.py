from django.db import models

class Sampah(models.Model):
    nama_sampah = models.CharField(max_length=100)
    kategori_sampah = models.CharField(max_length=100)
    keterangan = models.TextField()
    def __str__(self):
        return self.nama_sampah

class LokasiKecamatan(models.Model):
    nama_lokasi_kec = models.CharField(max_length=100)
    keterangan = models.TextField()
    def __str__(self):
        return self.nama_lokasi_kec

class AngkutanTrukSampah(models.Model):
    nama_angkutan_truk = models.CharField(max_length=100)
    deskripsi_angkutan = models.TextField()
    def __str__(self):
        return self.nama_angkutan_truk

class InputBS(models.Model):
    nama_sampah = models.ForeignKey(Sampah, on_delete=models.CASCADE)
    nama_lokasi = models.ForeignKey(LokasiKecamatan, on_delete=models.CASCADE)
    tanggal = models.DateField(max_length=100)
    jumlah = models.IntegerField()

class InputOP(models.Model):
    nama_sampah = models.ForeignKey(Sampah, on_delete=models.CASCADE)
    nama_lokasi = models.ForeignKey(LokasiKecamatan, on_delete=models.CASCADE)
    nama_angkutan_truk = models.ForeignKey(AngkutanTrukSampah, on_delete=models.CASCADE)
    tanggal = models.DateField(max_length=100)
    jam = models.TimeField(max_length=100)
    jumlah = models.IntegerField()
