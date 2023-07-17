import json

from django.http import JsonResponse

from nirvana import strategies


def coalesce_values(values: list, strategy='average') -> int:
    """Coalesces the list values using the selected `strategy`."""
    selected_strategy = getattr(strategies, strategy)
    return selected_strategy(values)


def get_json_dict(deductible, stop_loss, oop_max):
    """Returns a JSON dict that can be used as a response object."""
    return {'deductible': deductible, 'stop_loss': stop_loss, 'oop_max': oop_max}


def api1(request):
    """View for the api1 endpoint."""
    json_dict = get_json_dict(1000, 10000, 5000)
    return JsonResponse(json_dict)


def api2(request):
    """View for the api2 endpoint."""
    json_dict = get_json_dict(1200, 13000, 6000)
    return JsonResponse(json_dict)


def api3(request):
    """View for the api3 endpoint."""
    json_dict = get_json_dict(1000, 10000, 6000)
    return JsonResponse(json_dict)


def api_aggregator(request):
    """View for the api aggregator endpoint."""
    api_list = [api1, api2, api3]
    deductible_list = []
    stop_loss_list = []
    oop_max_list = []

    for api in api_list:
        response = api(request)
        content = json.loads(response.content)
        deductible_list.append(content['deductible'])
        stop_loss_list.append(content['stop_loss'])
        oop_max_list.append(content['oop_max'])

    deductible = coalesce_values(deductible_list)
    stop_loss = coalesce_values(stop_loss_list)
    oop_max = coalesce_values(oop_max_list)

    json_dict = get_json_dict(deductible, stop_loss, oop_max)
    return JsonResponse(json_dict)
