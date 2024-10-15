from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Operator, CountryData
from django.http import JsonResponse


def opeartors(request):
    return render(request, 'opeartors.html', {'Operators': Operator.objects.all()})


# def operator_detail(request, pk):
#     operator_instance = Operator.objects.get(id=pk)
#     return render(request, 'operator_detail.html', {
#         'operator': operator_instance
#     })

def operator_detail(request, pk):
    operator_instance = get_object_or_404(Operator, id=pk)
    country_data = CountryData.objects.filter(operator=operator_instance)
    
    return render(request, 'operator_detail.html', {
        'operator': operator_instance,
        'country_data': country_data
    })

def get_country_data(request, operator_id, country_code):
    try:
        # Fetch the relevant CountryData instance based on operator and country
        country_data = CountryData.objects.get(operator_id=operator_id, country=country_code)
        
        # Prepare the data to return, including multiple networks
        data = {
            'kyc_policy': country_data.kyc_policy,
            'networks': [network.network_name for network in country_data.networks.all()]
        }
        return JsonResponse(data)
    except CountryData.DoesNotExist:
        return JsonResponse({}, status=404)