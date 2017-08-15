import unittest
from mock import patch, MagicMock

import requests
import app

from samples.create_WAN import *

class TestSuccessfulCreateWan(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch('requests.post')
    def test_mpls_wan_success(self, mock_post):
        mock_api = MagicMock()
        mock_api.create_WAN.return_value = MagicMock(spec=requests.Response, status_code=200)
        result = app.create_WAN(mock_api, create_mpls_wan["result"]["parameters"], [])
        self.assertTrue(mock_api.create_WAN.called)
        self.assertEqual(mpls_success_speech_response, result)

    def test_failure_404(self):
        mock_api = MagicMock()
        mock_api.create_WAN.return_value = MagicMock(spec=requests.Response, status_code=404)
        result = app.create_WAN(mock_api, create_mpls_wan["result"]["parameters"], [])
        self.assertTrue(mock_api.create_WAN.called)
        self.assertEqual(mpls_404, result)

    def test_failure_400(self):
        mock_api = MagicMock()
        mock_api.create_WAN.return_value = MagicMock(spec=requests.Response, status_code=400)
        mock_api.create_WAN.return_value.json.return_value = mpls_400_api_response
        result = app.create_WAN(mock_api, create_mpls_wan["result"]["parameters"], [])
        self.assertTrue(mock_api.create_WAN.called)
        self.assertEqual(mpls_400_expected, result)

    def test_failure_500(self):
        mock_api = MagicMock()
        mock_api.create_WAN.return_value = MagicMock(spec=requests.Response, status_code=500)
        mock_api.create_WAN.return_value.json.return_value = mpls_500_api_response
        result = app.create_WAN(mock_api, create_mpls_wan["result"]["parameters"], [])
        self.assertTrue(mock_api.create_WAN.called)
        self.assertEqual(mpls_500_expected, result)
