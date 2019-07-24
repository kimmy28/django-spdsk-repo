from django.contrib import admin
from .models import Sampah, LokasiKecamatan, InputBS, AngkutanTrukSampah, InputOP

class SampahAdmin(admin.ModelAdmin):
    list_display = ('nama_sampah', 'kategori_sampah', 'keterangan',)
admin.site.register(Sampah, SampahAdmin)

class LokasiKecamatanAdmin(admin.ModelAdmin):
    list_display = ('nama_lokasi_kec', 'keterangan',)
admin.site.register(LokasiKecamatan, LokasiKecamatanAdmin)

class AngkutanTrukSampahAdmin(admin.ModelAdmin):
    list_display = ('nama_angkutan_truk', 'deskripsi_angkutan',)
admin.site.register(AngkutanTrukSampah, AngkutanTrukSampahAdmin)

class InputBSAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
admin.site.register(InputBS, InputBSAdmin)

class InputOPAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
admin.site.register(InputOP, InputOPAdmin)