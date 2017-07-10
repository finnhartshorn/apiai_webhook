import json

melbourne_shop_json_request = {
  "id": "46897f02-20ab-4af6-9539-798f4a252185",
  "timestamp": "2017-07-10T07:01:02.177Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "Create an uplink called directlink in-between Melbourne Shop and RouteVPN wan",
    "action": "CreateUplink",
    "actionIncomplete": False,
    "parameters": {
      "City": "Melbourne",
      "SiteTypes": "shop",
      "Uplinks": "directlink",
      "Wans": "RouteVPN"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f47796b8-5382-453e-be83-4afaaf0efd33",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 2286,
      "intentName": "CreateUplinkIntent"
    },
    "fulfillment": {
      "speech": "An uplink had created in site Melbourne_shop",
      "source": "steelconnect",
      "displayText": "An uplink had created in site Melbourne_shop",
      "messages": [
        {
          "type": 0,
          "speech": "An uplink had created in site Melbourne_shop"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "e9314ec4-1ba3-4bed-a376-ddb9711dc17f"
}

melbourne_shop_parameters = {
      "City": "Melbourne",
      "SiteTypes": "shop",
      "Uplinks": "directlink",
      "Wans": "RouteVPN"
}

tokyo_branch_parameters = {
  "id": "46897f02-20ab-4af6-9539-798f4a252185",
  "timestamp": "2017-07-10T07:01:02.177Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "Create an uplink called directlink in-between Melbourne Shop and RouteVPN wan",
    "action": "CreateUplink",
    "actionIncomplete": False,
    "parameters": {
      "City": "Tokyo",
      "SiteTypes": "branch",
      "Uplinks": "directlink",
      "Wans": "RouteVPN"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f47796b8-5382-453e-be83-4afaaf0efd33",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 2286,
      "intentName": "CreateUplinkIntent"
    },
    "fulfillment": {
      "speech": "An uplink had created in site Melbourne_shop",
      "source": "steelconnect",
      "displayText": "An uplink had created in site Melbourne_shop",
      "messages": [
        {
          "type": 0,
          "speech": "An uplink had created in site Melbourne_shop"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "e9314ec4-1ba3-4bed-a376-ddb9711dc17f"
}

hahawan_parameters = {
  "id": "46897f02-20ab-4af6-9539-798f4a252185",
  "timestamp": "2017-07-10T07:01:02.177Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "Create an uplink called directlink in-between Melbourne Shop and RouteVPN wan",
    "action": "CreateUplink",
    "actionIncomplete": False,
    "parameters": {
      "City": "Melbourne",
      "SiteTypes": "shop",
      "Uplinks": "directlink",
      "Wans": "hahawan"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f47796b8-5382-453e-be83-4afaaf0efd33",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 2286,
      "intentName": "CreateUplinkIntent"
    },
    "fulfillment": {
      "speech": "An uplink had created in site Melbourne_shop",
      "source": "steelconnect",
      "displayText": "An uplink had created in site Melbourne_shop",
      "messages": [
        {
          "type": 0,
          "speech": "An uplink had created in site Melbourne_shop"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "e9314ec4-1ba3-4bed-a376-ddb9711dc17f"
}

melbourne_shop_success_speech_response = "An  uplink called directlink had created in site Melbourne_shop to RouteVPN"
melbourne_shop_400_speech_response = "Invalid parameters: Invalid param: site"
melbourne_shop_400_api_response = {"error": {"message": "Invalid param: site", "code": 400}}
melbourne_shop_500_speech_response = "Error: Could not create uplink"
melbourne_shop_500_api_response = json.dumps({"error": {"message": "Error creating uplink", "code": 500}})
melbourne_shop_404_speech_response = "Error: Could not connect to Steelconnect"
invalid_site_speech_response = "Invalid site Tokyo_branch"
invalid_wan_speech_response = "Invalid wan hahawan"