import requests
from requests.auth import HTTPBasicAuth

from flask import json


class SteelConnectAPI:

    api_url = "https://{}/api/scm.config/1.0/"

    def __init__(self, username, password, base_url, org_id):
        self.auth = HTTPBasicAuth(username, password)
        self.base_url = base_url
        self.org_id = org_id

    @staticmethod
    def format_data(data):
        return json.dumps(data, indent=4)

    def org_url(self):
        return SteelConnectAPI.api_url.format(self.base_url) + "org/{}/".format(self.org_id)

    def list_sites(self):
        url = self.org_url() + "sites"
        return requests.get(url, auth=self.auth)

    def list_wans(self):
        url = self.org_url() + "wans"
        return requests.get(url, auth=self.auth)

    def create_site(self, name, city, country_code):
        url = self.org_url() + "sites"
        data = {"name": name, "longname": name, "city": city, "country": country_code}
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)

    def create_uplink(self, site, uplink, wan):
        url = self.org_url() + "uplinks"
        data = {
            "id": "",
            "site": site,
            "wan": wan,
            "org": self.org_id,
            "name": uplink,
        }
        # post uplink
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)

    def create_WAN(self, name):
        url = self.org_url() + "wans"
        data = {"name": name}
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)

    def create_zone(self, name, site):
        url = self.org_url() + "zones"
        data = {
            "id": "",
            "name": name,
            "site": site
        }
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)