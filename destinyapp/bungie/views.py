from django.http import HttpResponse


def index(request):
    return HttpResponse()


def weapon_list(request, weapon_id=None):
    if weapon_id:
        return HttpResponse("TODO: specific weapon: {}".format(weapon_id))
    return HttpResponse("TODO: All weapons")
