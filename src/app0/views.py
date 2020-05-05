from django.http import HttpResponse

def index( request ):
	return HttpResponse( "It works!", content_type = "text/plain" )
