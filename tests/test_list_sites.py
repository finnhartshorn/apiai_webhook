import unittest
from mock import patch, MagicMock

import requests
import app

from samples.list_sites import *


class TestListSite(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    def test_success_0_sites(self):
        mock_api = MagicMock()
        mock_api.list_sites.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_api.list_sites.return_value.json.return_value = case1_success_0_sites_return
        result = app.list_sites(mock_api, case1_basic_request)
        self.assertTrue(mock_api.list_sites.called)
        self.assertEqual(case1_success_0_sites, result)

    def test_success_1_site(self):
        mock_api = MagicMock()
        mock_api.list_sites.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_api.list_sites.return_value.json.return_value = case1_success_1_site_return              # TODO: Use actual data
        result = app.list_sites(mock_api, case1_basic_request)
        self.assertTrue(mock_api.list_sites.called)
        self.assertEqual(case1_success_1_site, result)

    def test_success_2_sites(self):
        mock_api = MagicMock()
        mock_api.list_sites.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_api.list_sites.return_value.json.return_value = case1_success_2_sites_return
        result = app.list_sites(mock_api, case1_basic_request)
        self.assertTrue(mock_api.list_sites.called)
        self.assertEqual(case1_success_2_sites, result)

    def test_success_5_sites(self):
        mock_api = MagicMock()
        mock_api.list_sites.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_api.list_sites.return_value.json.return_value = case1_success_5_sites_return
        result = app.list_sites(mock_api, case1_basic_request)
        self.assertTrue(mock_api.list_sites.called)
        self.assertEqual(case1_success_5_sites, result)

    def test_failure_404(self):
        mock_api = MagicMock()
        mock_api.list_sites.return_value = MagicMock(spec=requests.Response, status_code=404)
        mock_api.list_sites.return_value.json.return_value = case1_404_return
        result = app.list_sites(mock_api, case1_basic_request)
        self.assertTrue(mock_api.list_sites.called)
        self.assertEqual(case1_404, result)
