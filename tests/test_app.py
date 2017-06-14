import unittest
from unittest.mock import patch, MagicMock
import requests
import app
import actions

from flask import json
from samples.create_site import finland_helsinki_json_request
from samples.list_sites import case1_basic_request
from samples.list_sites_followup import specify_number_first_two, specify_all


class TestParseAction(unittest.TestCase):
    def setUp(self):
        self.app = app.app.test_client()

    @patch("app.create_site")
    def test_create_site_run(self, create_site):
        create_site.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(finland_helsinki_json_request))
        self.assertTrue(create_site.called)

    @patch("app.list_sites")
    def test_list_sites_run(self, list_sites):
        list_sites.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(case1_basic_request))
        self.assertTrue(list_sites.called)

    @patch("app.list_sites_followup")
    def test_list_sites__followup_specific_run(self, list_sites_followup):
        list_sites_followup.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(specify_number_first_two))
        self.assertTrue(list_sites_followup.called)

    @patch("app.list_sites_followup")
    def test_list_sites_followup_all_run(self, list_sites_followup):
        list_sites_followup.return_value = "All is well"
        self.app.post("/webhook/", headers={'Content-Type': 'application/json'}, data=json.dumps(specify_all))
        self.assertTrue(list_sites_followup.called)

