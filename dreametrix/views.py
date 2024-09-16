from django.http import HttpResponse
from django.shortcuts import render

from dreametrix.models import Domain


# Create your views here.

def public_index(request):
    _domain = []
    domain = Domain.objects.all()
    ending = request.get_host().split(':')[1]
    for domain in domain:
        _domain.append(domain.domain+":"+ending)

    context = {'domain': _domain}
    return render(request, "main_domain.html", context=context)
