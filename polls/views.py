from django.http import HttpResponse


def index(request):
    return HttpResponse("안녕하세요. 당신은 polls index에 있습니다.")
