# allows us to send a response to the user
from django.http import HttpResponse


def homepage(request):
    return HttpResponse('homepage')


# request parameter allows us to provide information about the request that was made by the user
def about(request):
    # sends a response to the request
    return HttpResponse('about')
