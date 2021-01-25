from rest_framework.utils import json
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import date


class DateAPI(APIView):

    def get(self, request):
        today = date.today()
        resp = {'currentDate': today.strftime("%d/%m/%Y")}

        return Response(resp)
