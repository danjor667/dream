from django.http import HttpResponse
from django.shortcuts import render
from django_tenants.utils import tenant_context

from dreametrix.models import Domain
from school.models import Student, Teacher


# Create your views here.


def index_tenant(request):
    # host = request.get_host().split(':')[0]
    # domain = Domain.objects.filter(domain=host)[0]
    # tenant = domain.tenant
    #
    # with tenant_context(tenant):
    #     students = Student.objects.all()
    #     teachers = Teacher.objects.all()
    #     context = {"student": students, "teacher": teachers}




    return HttpResponse("your not meant to be here")
