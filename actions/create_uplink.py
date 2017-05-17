import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests


def create_uplink(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteTypes"]
        city = parameters["City"]
        uplink_name = parameters["Uplinks"]

        # API Call Here
        url = 'https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/uplinks'
        data = {
          "id": "",
          "site": city + "_" + site_type,
          "wan": "wan-Internet-b47d7c36130a5ccf",
          "org": "Monash",
          "qos_bw_up": 0,
          "qos_up": 0,
          "static_ip_v4": "string",
          "static_gw_v4": "string",
          "static_ip_v6": "string",
          "static_gw_v6": "string",
          "uin": 0,
          "uid": 0,
          "node": "string",
          "name": uplink_name,
          "qos_bw_down": 0,
          "qos_down": 0,
          "port": "string",
          "vlan": 0,
          "type": "string",
          "sitelink_ipsel": "string",
          "sitelink_custom_ip": "string",
          "sitelink_prio": 0,
          "bgp_advertised_routes": "[1.2.3.4,5.7.8.9]",
          "bgp_learned_routes": "[1.2.3.4,5.7.8.9]",
          "bgp_enable": 0,
          "bgp_router_id": "1.2.3.4",
          "bgp_local_as": "string",
          "bgp_neigh_name": "BGP_NEIGHBOUR",
          "bgp_neigh_remote_as": 0,
          "bgp_neigh_ipv4": "1.2.3.4",
          "bgp_neigh_password": "PASSWORD",
          "bgp_neigh_keepalive_time": "60",
          "bgp_neigh_hold_time": "180"
        }
        request = json.dumps(data, indent=4)
        res = requests.post(url, data=request, auth=HTTPBasicAuth('Aubrey', 'Aubrey'))
        logging.debug(res)
        # Ends Here

        speech = "An uplink had created in site {}".format(site_type.capitalize())

        logging.debug(speech)

        return speech

    except KeyError as e:

        error_string = "Error processing createUplink intent. {0}".format(e)

        logging.error(error_string)

        return error_string

