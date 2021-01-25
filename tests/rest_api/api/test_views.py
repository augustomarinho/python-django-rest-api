from datetime import date

from rest_framework.test import APITestCase
from rest_framework.utils import json


class DateAPITests(APITestCase):

    def test_get(self):
        """
        Test for validating REST API current date
        :return:
        """
        today = date.today().strftime("%d/%m/%Y")

        response = self.client.get("/api/currentdate", format='json')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response)
        self.assertEqual(json.loads(response.content)["currentDate"], today)
