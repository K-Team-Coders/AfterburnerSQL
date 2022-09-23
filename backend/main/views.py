from django.http import HttpResponse

from rest_framework.views import APIView

from loguru import logger

class testView(APIView):
    def get(self, request):
        logger.debug(request.body)
        return HttpResponse(status=200)
