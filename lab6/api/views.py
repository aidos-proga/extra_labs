from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from . import models


def ReadCompany(request):
    company_list = models.Company.objects.all()
    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'city': i.city,
        'address': i.address
    } for i in company_list]
    return JsonResponse(data=data, safe=False)


def RetrieveCompany(request, **kwargs):
    company = models.Company.objects.get(id=int(kwargs['id']))
    data = [{
        'id': company.id,
        'name': company.name,
        'description': company.description,
        'city': company.city,
        'address': company.address
    }]
    return JsonResponse(data=data, safe=False)


def ReadVacancy(request):
    vacancy_list = models.Vacancy.objects.all()
    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'salary': i.salary,
        'company': i.company.name
    } for i in vacancy_list]
    return JsonResponse(data=data, safe=False)


def RetrieveVacancy(request, **kwargs):
    vacancy = models.Vacancy.objects.get(id=int(kwargs['id']))
    data = [{
        'id': vacancy.id,
        'name': vacancy.name,
        'description': vacancy.description,
        'salary': vacancy.salary,
        'company': vacancy.company.name
    }]
    return JsonResponse(data=data, safe=False)


def ByCompany(request, **kwargs):
    vacancies = models.Vacancy.objects.filter(company_id=int(kwargs['id']))
    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'salary': i.salary,
        'company': i.company.name
    } for i in vacancies]

    return JsonResponse(data=data, safe=False)


def TopTenVacancy(request, **kwargs):
    vacancies = models.Vacancy.objects.order_by('-salary')[:10]

    data = [{
        'id': i.id,
        'name': i.name,
        'description': i.description,
        'salary': i.salary,
        'company': i.company.name
    } for i in vacancies]

    return JsonResponse(data=data, safe=False)