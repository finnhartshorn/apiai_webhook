import unittest
from unittest.mock import patch, MagicMock

import requests
import app

from flask import json
from samples.create_site import *


# class MockResponse(Mock):
#     def __init__(self, json_data, status_code):
#         super().__init__()
#         # self.
#         self.status_code = status_code
#         self.json_data = json_data
#
#     def json(self):
#         return self.json_data


class TestSuccessfulCreateSite(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch('requests.post')
    def test_finland_success(self, mock_post):
        mock_post.return_value = MagicMock(spec=requests.Response, status_code=200)
        result = app.create_site(finland_helsinki_parameters)
        mock_post.assert_called_once()
        self.assertEqual(finland_helsinki_success_speech_response, result)

    @patch('requests.post')
    def test_finland_400(self, mock_post):
        mock_post.return_value = MagicMock(spec=requests.Response, status_code=400)
        mock_post.return_value.json.return_value = finland_helsinki_400_api_response
        result = app.create_site(finland_helsinki_parameters)
        mock_post.assert_called_once()
        self.assertEqual(finland_helsinki_400_speech_response, result)

    @patch('requests.post')
    def test_finland_500(self, mock_post):
        mock_post.return_value = MagicMock(spec=requests.Response, status_code=500)
        result = app.create_site(finland_helsinki_parameters)
        mock_post.assert_called_once()
        self.assertEqual(finland_helsinki_500_speech_response, result)

    @patch('requests.post')
    def test_finland_404(self, mock_post):
        mock_post.return_value = MagicMock(spec=requests.Response, status_code=404)
        result = app.create_site(finland_helsinki_parameters)
        mock_post.assert_called_once()
        self.assertEqual(finland_helsinki_404_speech_response, result)

