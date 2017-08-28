import requests
from requests.auth import HTTPBasicAuth
import requests_toolbelt.adapters.appengine

from flask import json

requests_toolbelt.adapters.appengine.monkeypatch()

class SteelConnectAuthFactory:

    def __init__(self, username, password, base_url, org_id):
        default_auth = HTTPBasicAuth(username, password)
        base_url = base_url
        org_id = org_id
        self.auth_store = {"default" : {"auth": default_auth, "base_url": base_url, "org_id": org_id}}

    def add_auth(self, google_email, org_id, sc_url, sc_username, sc_password):
        self.auth_store[google_email] =  {"org_id": org_id, "base_url": sc_url, "auth": HTTPBasicAuth(sc_username, sc_password)}

    def make_auth(self, email=None):
        auth_details = self.auth_store["default"]
        if email:
            auth_details = self.auth_store[email]
        return SteelConnectAPI(auth_details["auth"], auth_details["base_url"], auth_details["org_id"])



class SteelConnectAPI:

    api_url = "https://{}/api/scm.config/1.0/"

    def __init__(self, auth, base_url, org_id):
        self.auth = auth
        self.base_url = base_url
        self.org_id = org_id

    @staticmethod
    def format_data(data):
        return json.dumps(data, indent=4)

    @staticmethod
    def find_context_by_name(contexts, name):
        for context in contexts:
            if context["name"] == name:
                return context
        else:
            return None

    def org_url(self):
        return SteelConnectAPI.api_url.format(self.base_url) + "org/{}/".format(self.org_id)

    def list_sites(self):
        url = self.org_url() + "sites"
        return requests.get(url, auth=self.auth)

    def list_wans(self):
        url = self.org_url() + "wans"
        return requests.get(url, auth=self.auth)

    def list_zones(self):
        url = self.org_url() + "zones"
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