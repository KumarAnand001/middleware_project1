class ExecutionFlowMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self,request):

        print('This Line printed at pre processing of request')
        response = self.get_response(request)
        print('This line printed at post processing of request')
        return response
    
from typing import Any
from django.http import HttpResponse
class AppMaintenanceMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        return HttpResponse('<h1>Currently Application Under Maintenance Please try after 2 days')
    
class ErrorMassegeMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        return response
    
    def process_exception(self, request, exception):

        s1 = '<h1> Currentlly we are facing some technical problem, Plz try after some time<h1>'
        s2 = '<h1> Raised Exception:{}<h1>'.format(exception.__class__.__name__)
        s3 = '<h1> Exception Description: {}<h1>'.format(exception)
        return HttpResponse(s1+s2+s3)
    
class FirstMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self,request):

        print('This Line printed by first Middleware at pre processing of request')
        response = self.get_response(request)
        print('This line printed by first Middleware at post processing of request')
        return response

class SecondMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self,request):

        print('This Line printed by Second Middleware at pre processing of request')
        response = self.get_response(request)
        print('This line printed by Second Middleware at post processing of request')
        return response

class ThirdMiddleware(object):

    def __init__(self, get_response):

        self.get_response = get_response

    def __call__(self,request):

        print('This Line printed by Third Middleware at pre processing of request')
        response = self.get_response(request)
        print('This line printed by Third Middleware at post processing of request')
        return response