from django.shortcuts import redirect
from .models import StudentClass
import csv, io
# Create your views here.


def create_studnet(request):
    if request.method == 'POST' and request.FILES['file']:
        files = request.FILES['file']
        data = files.read().decode('UTF-8')

        data_stream = io.StringIO(data)
        next(data_stream)
        for col in csv.reader(data_stream, delimiter=',', quotechar="|"):
            StudentClass.objects.create(
                standard = col[0],
                shift = col[1],
                section = col[2]
            )
    return redirect('index')