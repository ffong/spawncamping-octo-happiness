from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, wonderful world. You're at the index.")