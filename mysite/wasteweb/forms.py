from django.conf import settings
from django import forms
from django.forms import ModelForm
from .models import Sampah, LokasiKecamatan, AngkutanTrukSampah, InputBS, InputOP


class TambahBSForm(ModelForm):
    """
    Render the basic crud create form
    """
    nama_sampah = forms.ModelChoiceField(queryset=Sampah.objects.all())

    nama_lokasi = forms.ModelChoiceField(queryset=LokasiKecamatan.objects.all())

    tanggal = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control', 'placeholder': 'Tanggal'}))

    jumlah = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Masukkan jumlah sampah'}))

    class Meta:
        model = InputBS
        fields = ('nama_sampah', 'nama_lokasi', 'tanggal', 'jumlah')

class TambahOPForm(ModelForm):
    """
    Render the basic crud create form
    """
    nama_sampah = forms.ModelChoiceField(queryset=Sampah.objects.all())

    nama_lokasi = forms.ModelChoiceField(queryset=LokasiKecamatan.objects.all())

    nama_angkutan_truk = forms.ModelChoiceField(queryset=AngkutanTrukSampah.objects.all())

    tanggal = forms.DateField(
        widget=forms.SelectDateWidget(attrs={
            'class': 'form-control', 'placeholder': 'Tanggal'}))

    jam = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'class': 'form-control', 'placeholder': 'Jam'}))

    jumlah = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control',
                                     'placeholder': 'Masukkan jumlah sampah'}))

    class Meta:
        model = InputOP
        fields = ('nama_sampah', 'nama_lokasi', 'nama_angkutan_truk', 'tanggal', 'jam', 'jumlah')