import unittest
from unittest.mock import patch, MagicMock

import requests
import app

from samples.list_sites import *


class TestSuccessfulCreateSite(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch('requests.get')
    def test_success_0_sites(self, mock_get):
        mock_get.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_get.return_value.json.return_value = case1_success_0_sites_return
        result = app.list_sites(case1_basic_request)
        mock_get.assert_called_once()
        self.assertEqual(case1_success_0_sites, result)

    @patch('requests.get')
    def test_success_1_site(self, mock_get):
        mock_get.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_get.return_value.json.return_value = case1_success_1_site_return              # TODO: Use actual data
        result = app.list_sites(case1_basic_request)
        mock_get.assert_called_once()
        self.assertEqual(case1_success_1_site, result)

    @patch('requests.get')
    def test_success_2_sites(self, mock_get):
        mock_get.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_get.return_value.json.return_value = case1_success_2_sites_return
        result = app.list_sites(case1_basic_request)
        mock_get.assert_called_once()
        self.assertEqual(case1_success_2_sites, result)

    @patch('requests.get')
    def test_success_5_sites(self, mock_get):
        mock_get.return_value = MagicMock(spec=requests.Response, status_code=200)
        mock_get.return_value.json.return_value = case1_success_5_sites_return
        result = app.list_sites(case1_basic_request)
        mock_get.assert_called_once()
        self.assertEqual(case1_success_5_sites, result)

    @patch('requests.get')
    def test_failure_404(self, mock_get):
        mock_get.return_value = MagicMock(spec=requests.Response, status_code=404)
        mock_get.return_value.json.return_value = case1_404_return
        result = app.list_sites(case1_basic_request)
        mock_get.assert_called_once()
        self.assertEqual(case1_404, result)
