# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Patient, TestData

class PatientListView(ListView):
    model = Patient
    template_name = 'patientdata/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patientdata/patient_detail.html'
    context_object_name = 'patient'

class TestDataListView(ListView):
    model = TestData
    template_name = 'patientdata/testdata_list.html'
    context_object_name = 'test_data'

    def get_queryset(self):
        return TestData.objects.select_related('patient_info')

from django.http import HttpResponse
import openpyxl

from django.contrib.auth.views import LoginView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class CustomLoginView(LoginView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def generate_excel(request):
    # Your data to be included in the Excel file
    data = [
        ['Patient', 'Phone Number', 'Unit', 'Shift', 'Visfatin Number', 'MDA Number', 'FMD Number'],
    ]

    for test_data in TestData.objects.all():  # Replace TestModel with your actual model name
        data.append([
            test_data.patient_info.name,
            test_data.patient_info.phone_number,
            test_data.unit,
            test_data.shift,
            test_data.visfatin_number,
            test_data.MDA_number,
            test_data.FMD_number
        ])

    # Create a new workbook and select the active worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write data to the worksheet
    for row_data in data:
        ws.append(row_data)

    # Create the HttpResponse object with Excel content type
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=test_data.xlsx'

    # Save the workbook to the HttpResponse
    wb.save(response)

    return response
