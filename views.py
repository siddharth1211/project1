from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import apidocForm
from .models import apiData
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import openpyxl
from django.conf import settings
from django.core import serializers
from .serializers import apiSerializer
import os
import json

def home(request):
    form = apidocForm(request.POST, request.FILES, None)
    d1 = {}
    data = []
    if request.method == 'POST' and request.FILES['file']:
        if form.is_valid():
            form.save()
            print(form.files)
            upload = request.FILES['file']
            file_url = os.path.join(settings.MEDIA_ROOT, 'files')
            print(file_url)
            file_url1 = os.path.join(file_url, upload.name)
            print(file_url1)
            wb1 = openpyxl.load_workbook(file_url1)
            ws1 = wb1.active
            for row in ws1.iter_rows():
                 t1 = [col.value for col in row][:4]
                 d1 = {'cpn': t1[0], 'cpd': t1[1], 'irn': t1[2], 'qp': t1[3]}
                 data.append(d1)
            del data[0]
            for i in data:
                try:
                   serializer = apiSerializer(data=i)
                   if serializer.is_valid():
                         serializer.save()
                   print(serializer.data)
                except ValueError:
                    print("data not correct")
#            json_data = json.dumps(data)
            return redirect("home")
    else:
        form = apidocForm()

    return render(request, 'home.html', {'form': form, 'data': data})


def get_data(request):
    x = apiData.objects.all()
    t1 = []
    d1 = {}
    for i in x:
        # d1['id'] = i.id
        # d1['cpn'] = i.cpn
        # d1['cpd'] = i.cpd
        # d1['irn'] = i.irn
        # d1['qp'] = i.qp
        item = {'id': i.id, 'cpn': i.cpn, 'cpd': i.cpd, 'irn': i.irn, 'qp': i.qp}
        t1.append(item)
    print(t1)
    return JsonResponse({'qs': t1})
# Create your views here.