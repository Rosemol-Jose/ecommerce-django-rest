from django.http import HttpResponse
import requests
from django.conf import settings

class ExceptionHandlingMiddleware(object):
    """
    Any exceptions in views will bequeried in stackoverflow and 3 top qna are fetched
    """
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self, request):
        response=self.get_response(request)
        return response
    # def process_view(self):
    #     pass
    def process_exception(self, request, exception):
        if settings.DEBUG:
            print("The error occured in processing views: ",exception)
            url = 'https://api.stackexchange.com/2.2/search'
            headers = {'User-Agent': 'PostmanRuntime/7.31.1'}
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',

            }

            r = requests.get(url, params=params, headers=headers)
            questions = r.json()



            for question in questions['items']:
                print("Here are 3 possible queries related to the rror")
                print(question['title'])
                print(question['link'])
                print('')

        return HttpResponse("Page cannot be displayed due to some error ")
