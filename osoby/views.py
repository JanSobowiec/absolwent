from django.http import HttpResponse

def index(request):
    return HttpResponse("2137")



def about(request):
    return HttpResponse("Uwaga dzieci papież leci 🇻🇦")