import unittest
from unittest.mock import patch, MagicMock

import requests
import app

from flask import json
from samples.create_uplink import *
from actions.api import SteelConnectAPI


# class MockResponse(Mock):
#     def __init__(self, json_data, status_code):
#         super().__init__()
#         # self.
#         self.status_code = status_code
#         self.json_data = json_data
#
#     def json(self):
#         return self.json_data


class TestCreateUplinks(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_melbourne_shop_success(self):
        mock_api = MagicMock()
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=200)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_success_speech_response, result)

    # def test_finland_400(self):
    #     mock_api = MagicMock()
    #     mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=400)
    #     mock_api.create_uplink.return_value.json.return_value = melbourne_shop_400_api_response
    #     result = app.create_uplink(mock_api, melbourne_shop_parameters)
    #     self.assertTrue(mock_api.create_uplink.called)
    #     self.assertEqual(melbourne_shop_400_speech_response, result)

    def test_melbourne_shop_500(self):
        mock_api = MagicMock()
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=500)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_500_speech_response, result)

    def test_melbourne_shop_404(self):
        mock_api = MagicMock()
        mock_api.create_uplink.return_value = MagicMock(spec=requests.Response, status_code=404)
        result = app.create_uplink(mock_api, melbourne_shop_parameters)
        self.assertTrue(mock_api.create_uplink.called)
        self.assertEqual(melbourne_shop_404_speech_response, result)

