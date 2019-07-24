
from django.http import Http404
from django.shortcuts import render,
from django.http import HttpResponse
from .decorators import operator_login_required
from .decorators import banksampah_login_required
from .models import InputBS, InputOP

from django.conf import settings
from django.http import JsonResponse
from django.utils.text import slugify
from django.db.models import Q

import json
import pytz
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
# Call myroot properties
from .forms import TambahBSForm, TambahOPForm
from datetime import datetime, timedelta
from itertools import chain

def dict_alert_msg(form_is_valid, alert_title, alert_msg, alert_type):
    """
    Function to call internal alert message to the user with the required
    paramaters: form_is_valid[True/False all small letters for json format],
    alert_title='string', alert_msg='string',
    alert_type='success, error, warning, info'
    """
    data = {
        'form_is_valid': form_is_valid,
        'alert_title': alert_title,
        'alert_msg': alert_msg,
        'alert_type': alert_type
    }
    return data


def convert_to_local_datetime(dt_value):
    MY_DT_FORMAT = '%Y-%m-%d %H:%M:%S'
    dt = dt_value
    created_date_str = dt.strftime(MY_DT_FORMAT)  # convert to string
    created_date = dt.strptime(created_date_str, MY_DT_FORMAT)

    # timeago in python library to get user's local time
    now = datetime.now() + timedelta(seconds=60 * 3.4)
    event_date = timeago.format(created_date, now)

    return str(event_date)



def index(request):
    return render(request, 'wasteweb/index.html')

def tentang(request):
    return render(request, 'wasteweb/tentang.html')

def kontak(request):
    return render(request, 'wasteweb/kontak.html')

def login(request):
    return render(request, 'accounts/login/')

def logout(request):
    return render(request, 'accounts/logout/')

def error(request):
    return render(request, 'wasteweb/404.html')

def report(request):
    if request.method == "GET":

        q1 = InputOP.objects.all().order_by('-id')[:50]
        q2 = InputBS.objects.all().order_by('-id')[:50]  # fetch the latest 50 rows
        db_data = chain(q1,q2)

        return render(request, 'wasteweb/report.html',
                      {
                          'title': 'Input Data Sampah Kota Semarang',
                          'meta_desc': 'Sistem Informasi Pengelolaan Data Sampah Kota Semarang',
                          'db_data': db_data,
                      })
    else:
        return HttpResponse('/wasteweb/error/', context_instance=RequestContext(request))

@banksampah_login_required
def TambahBSForm_view(request):
        form = TambahBSForm(request.POST or None)
        if form.is_valid():
            form.save()  # insert new row
            return redirect('/wasteweb/bsdata')
        return render(request, 'wasteweb/tambah_bs.html', {'form': form})

@operator_login_required
def TambahOPForm_view(request):
    form = TambahOPForm(request.POST or None)
    if form.is_valid():
        form.save()  # insert new row
        return redirect('/wasteweb/opdata')
    return render(request, 'wasteweb/tambah_op.html', {'form': form})

@banksampah_login_required
def bsdata(request):
    if request.method == "GET":

        db_data = InputBS.objects.all().order_by('-id')[:50]  # fetch the latest 50 rows

        return render(request, 'wasteweb/bsdata.html',
                      {
                          'title': 'Input Data Sampah Kota Semarang',
                          'meta_desc': 'Sistem Informasi Pengelolaan Data Sampah Kota Semarang',
                          'db_data': db_data
                       })
    else:
        return HttpResponse('/wasteweb/error/', context_instance=RequestContext(request))

@operator_login_required
def opdata(request):
    if request.method == "GET":

        db_data = InputOP.objects.all().order_by('-id')[:50]  # fetch the latest 50 rows

        return render(request, 'wasteweb/opdata.html',
                      {
                          'title': 'Input Data Sampah Kota Semarang',
                          'meta_desc': 'Sistem Informasi Pengelolaan Data Sampah Kota Semarang',
                          'db_data': db_data
                       })
    else:
        return HttpResponse('/wasteweb/error/', context_instance=RequestContext(request))

@banksampah_login_required
def hapusBSdata(request, id):
    hapusbs = InputBS.objects.get(id=id)
    hapusbs.delete()
    return redirect('/wasteweb/bsdata')
    return render(request, 'wasteweb/hapusBSdata.html', {'hapusbs': hapusbs})

@operator_login_required
def hapusOPdata(request, id):
    hapusop = InputOP.objects.get(id=id)
    hapusop.delete()
    return redirect('/wasteweb/opdata')
    return render(request, 'wasteweb/hapusOPdata.html', {'hapusop': hapusop})

@banksampah_login_required
def updateBSdata(request, id):
    if request.method == "GET":

        # Get the selected row information
        db_data = InputBS.objects.filter(id=id)

        if db_data:

            # Edit form data
            edit_data = InputBS.objects.get(id=id)
            formEdit = TambahBSForm(instance=edit_data)

            return render(request, 'wasteweb/updateBSdata.html',
                          {
                              'title': 'Update Input Data Sampah Kota Semarang',
                              'meta_desc': 'Sistem Informasi Pengelolaan Data Sampah Kota Semarang',
                              'id': id,
                              'formEdit': formEdit
                          })
        else:
            raise Http404()

    data = dict()
    if request.method == "POST":

        # Get the  form modified data
        form_edit = TambahBSForm(request.POST)
        id = request.POST.get('id')

        if form_edit.is_valid():

            # Check if the row still not deleted
            if InputBS.objects.filter(id=id).exists():

                # Get the form edit instance
                update_data = InputBS.objects.get(id=id)

                # Now, supply the form data to an instance
                form_edit = TambahBSForm(request.POST, instance=update_data)
                form_edit.save()  # Finally save the form data

            return redirect('/wasteweb/bsdata')
            return render(request, 'wasteweb/updateBSdata.html', {'form_edit': form_edit})


@operator_login_required
def updateOPdata(request, id):
    if request.method == "GET":

        # Get the selected row information
        db_data = InputOP.objects.filter(id=id)

        if db_data:

            # Edit form data
            edit_data = InputOP.objects.get(id=id)
            formEdit = TambahOPForm(instance=edit_data)

            return render(request, 'wasteweb/updateopdata.html',
                          {
                              'title': 'Update Input Data Sampah Kota Semarang',
                              'meta_desc': 'Sistem Informasi Pengelolaan Data Sampah Kota Semarang',
                              'id': id,
                              'formEdit': formEdit
                          })
        else:
            raise Http404()

    data = dict()
    if request.method == "POST":

        # Get the  form modified data
        form_edit = TambahOPForm(request.POST)
        id = request.POST.get('id')

        if form_edit.is_valid():

            # Check if the row still not deleted
            if InputOP.objects.filter(id=id).exists():

                # Get the form edit instance
                update_data = InputOP.objects.get(id=id)

                # Now, supply the form data to an instance
                form_edit = TambahOPForm(request.POST, instance=update_data)
                form_edit.save()  # Finally save the form data

            return redirect('/wasteweb/opdata')
            return render(request, 'wasteweb/updateOPdata.html', {'form_edit': form_edit})


@banksampah_login_required
def bsdata_search_text_view(request):
    if request.method == "POST":
        fsearch = request.POST.get('fsearch')

        # Filter data by using __icontains built-in Django function
        data_lists = InputBS.objects.filter(
                        (Q(nama_sampah__icontains=fsearch) |
                        Q(nama_lokasi__icontains=fsearch) |
                        Q(tanggal__icontains=fsearch) |
                        Q(jumlah__icontains=fsearch))).order_by('-id')[:50]

        fh_data = dict()
        fh_list = []

        for fh in data_lists:
            url = settings.BASE_URL + slugify(fh.nama_sampah) + "-" + str(fh.id)
            trun_nama_lokasi = fh.nama_lokasi[:100] + '...'

            # Convert UTC datetime from db to user's local datetime.
            submitted_date = convert_to_local_datetime(fh.submitted)

            edit_url = settings.BASE_URL + "updateBSdata/" + str(fh.id) + "/change/"

            fh_list.append(
                    {'nama_sampah': (fh.nama_sampah),
                     'nama_lokasi': trun_nama_lokasi,
                     'tanggal': fh.tanggal,
                     'jumlah': fh.jumlah,
                     'submitted': submitted_date,
                     'id': fh.id,
                     'url': url,
                     'edit_url': edit_url
                     })

        fh_data = fh_list
        json_data = json.dumps(fh_data)
        return JsonResponse(json_data, safe=False)

@operator_login_required
def opdata_search_text_view(request):
    if request.method == "POST":
        fsearch = request.POST.get('fsearch')

        # Filter data by using __icontains built-in Django function
        data_lists = InputOP.objects.filter(
                        (Q(nama_sampah__icontains=fsearch) |
                        Q(nama_lokasi__icontains=fsearch) |
                        Q(nama_angkutan_truk__icontains=fsearch) |
                        Q(tanggal__icontains=fsearch) |
                        Q(jam__icontains=fsearch) |
                        Q(jumlah__icontains=fsearch))).order_by('-id')[:50]

        fh_data = dict()
        fh_list = []

        for fh in data_lists:
            url = settings.BASE_URL + slugify(fh.nama_sampah) + "-" + str(fh.id)
            trun_nama_lokasi = fh.nama_lokasi[:100] + '...'

            # Convert UTC datetime from db to user's local datetime.
            submitted_date = convert_to_local_datetime(fh.submitted)

            edit_url = settings.BASE_URL + "updateOPdata/" + str(fh.id) + "/change/"

            fh_list.append(
                    {'nama_sampah': (fh.nama_sampah),
                     'nama_lokasi': trun_nama_lokasi,
                     'nama_angkutan_truk': fh.nama_angkutan_truk,
                     'tanggal': fh.tanggal,
                     'jam': fh.jam,
                     'jumlah': fh.jumlah,
                     'submitted': submitted_date,
                     'id': fh.id,
                     'url': url,
                     'edit_url': edit_url
                     })

        fh_data = fh_list
        json_data = json.dumps(fh_data)
        return JsonResponse(json_data, safe=False)

@banksampah_login_required
def bsdata_search_dr_view(request):
    if request.method == "POST":

        # Get the date range values from the user input
        mStartDate = request.POST.get('mStartDate')
        mEndDate = request.POST.get('mEndDate')

        # Format date
        date_format = '%Y-%m-%d'

        unaware_start_date = datetime.strptime(mStartDate, date_format)
        aware_start_date = pytz.utc.localize(unaware_start_date)

        unaware_end_date = datetime.strptime(mEndDate, date_format
                                             ) + timedelta(days=1)
        aware_end_date = pytz.utc.localize(unaware_end_date)

        # Display data, using __range from Django's built-in functionality
        data_lists = InputBS.objects.filter(
                            submitted__range=(aware_start_date,
                                              aware_end_date)
                            ).order_by('-id')[:50]

        fh_data = dict()
        fh_list = []

        for fh in data_lists:
            url = settings.BASE_URL + slugify(fh.nama_sampah) + "-" + str(fh.id)
            trun_nama_lokasi = fh.nama_lokasi[:100] + '...'

            # Convert UTC datetime from db to user's local datetime.
            submitted_date = convert_to_local_datetime(fh.submitted)

            edit_url = settings.BASE_URL + "updateBSdata/" + str(fh.id) + "/change/"

            fh_list.append(
                    {'nama_sampah': (fh.nama_sampah),
                     'nama_lokasi': trun_nama_lokasi,
                     'tanggal': fh.tanggal,
                     'jumlah': fh.jumlah,
                     'submitted': submitted_date,
                     'id': fh.id,
                     'url': url,
                     'edit_url': edit_url
                     })

        fh_data = fh_list
        json_data = json.dumps(fh_data)
        return JsonResponse(json_data, safe=False)

@operator_login_required
def opdata_search_dr_view(request):
    if request.method == "POST":

        # Get the date range values from the user input
        mStartDate= request.POST.get('mStartDate')
        mEndDate= request.POST.get('mEndDate')

        # Format date
        date_format = '%Y-%m-%d'

        unaware_start_date = datetime.strptime(mStartDate, date_format)
        aware_start_date = pytz.utc.localize(unaware_start_date)

        unaware_end_date = datetime.strptime(mEndDate, date_format
                                             ) + timedelta(days=1)
        aware_end_date = pytz.utc.localize(unaware_end_date)

        # Display data, using __range from Django's built-in functionality
        data_lists = InputOP.objects.filter(
                            submitted__range=(aware_start_date,
                                              aware_end_date)
                            ).order_by('-id')[:50]

        fh_data = dict()
        fh_list = []

        for fh in data_lists:
            url = settings.BASE_URL + slugify(fh.nama_sampah) + "-" + str(fh.id)
            trun_nama_lokasi = fh.nama_lokasi[:100] + '...'

            # Convert UTC datetime from db to user's local datetime.
            submitted_date = convert_to_local_datetime(fh.submitted)

            edit_url = settings.BASE_URL + "updateBSdata/" + str(fh.id) + "/change/"

            fh_list.append(
                    {'nama_sampah': (fh.nama_sampah),
                     'nama_lokasi': trun_nama_lokasi,
                     'nama_angkutan_truk': fh.nama_angkutan_truk,
                     'tanggal': fh.tanggal,
                     'jam': fh.jam,
                     'jumlah': fh.jumlah,
                     'submitted': submitted_date,
                     'id': fh.id,
                     'url': url,
                     'edit_url': edit_url
                     })

        fh_data = fh_list
        json_data = json.dumps(fh_data)
        return JsonResponse(json_data, safe=False)