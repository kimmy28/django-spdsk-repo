from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('error/', views.error, name='error'),
    path('tentang/', views.tentang, name='tentang'),
    path('kontak/', views.kontak, name='kontak'),
    path('report/', views.report, name='report'),
    path('opdata/', views.opdata, name='opdata'),
    path('bsdata/', views.bsdata, name='bsdata'),
    path('updateBSdata/<int:id>/', views.updateBSdata, name='updateBSdata'),
    path('updateOPdata/<int:id>/', views.updateOPdata, name='updateOPdata'),
    path('TambahBSForm_view/', views.TambahBSForm_view, name='TambahBSForm_view'),
    path('TambahOPForm_view/', views.TambahOPForm_view, name='TambahOPForm_view'),
    path('hapusBSdata/<int:id>/', views.hapusBSdata, name='hapusBSdata'),
    path('hapusOPdata/<int:id>/', views.hapusOPdata, name='hapusOPdata'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
app_name = 'wasteweb'

