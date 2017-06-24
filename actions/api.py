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

    def create_site(self, name, city, country_code):
        url = self.org_url() + "sites"
        # data = {"id": "", "name": name, "org": "Monash", "longname": name, "uplinks": [""], "networks": [""],
        #         "street_address": "", "city": city, "country": country_code, "timezone": "", "size": 0, "uid": ""}
        data = {"name": name, "longname": name, "city": city, "country": country_code}
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)

    def create_uplink(self, site, uplink):
        url = self.org_url() + "sites"
        data = {
            "id": "",
            "site": site,
            "wan": "wan-Internet-0ee899d81ec323a4",
            "org": "Monash",
            "name": uplink,
        }
        # post uplink
        data = self.format_data(data)
        return requests.post(url, data=data, auth=self.auth)

