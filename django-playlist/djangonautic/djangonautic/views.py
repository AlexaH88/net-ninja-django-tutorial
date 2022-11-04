# allows us to send a response to the user
from django.http import HttpResponse
# allows us to render an html template in the browser
from django.shortcuts import render


def homepage(request):
    # basic example of returning information
    # return HttpResponse('homepage')

    # return a rendered html template
    return render(request, 'homepage.html')


# request parameter allows us to provide information about the request that was made by the user
def about(request):
    # basic example of returning information
    # sends a response to the request
    # return HttpResponse('about')

    return render(request, 'about.html')
