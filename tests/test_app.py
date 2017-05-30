import unittest
from unittest.mock import patch, MagicMock
import requests
import app
import actions

from flask import json
from samples.create_site import finland_helsinki_json_request
from samples.list_sites import case1_basic_request


class TestParseAction(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch("app.create_site")
    def test_create_site_run(self, create_site):
        create_site.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(finland_helsinki_json_request))
        create_site.assert_called_once()

    @patch("app.list_sites")
    def test_list_sites_run(self, list_sites):
        list_sites.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(case1_basic_request))
        list_sites.assert_called_once()
