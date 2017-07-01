import json

melbourne_shop_json_request = {
  "id": "cc96c1c2-a738-4e3d-8764-83ec0a05e30d",
  "timestamp": "2017-05-17T13:02:48.827Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "create a link in Melbourne shop",
    "action": "CreateUplink",
    "actionIncomplete": False,
    "parameters": {
      "City": "Melbourne",
      "geo-city": "",
      "SiteTypes": "shop",
      "Uplinks": "uplink"
    },
    "contexts": [],
    "metadata": {
      "intentId": "f47796b8-5382-453e-be83-4afaaf0efd33",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 49,
      "intentName": "CreateUplinkIntent"
    },
    "fulfillment": {
      "speech": "Error: This feature has not been implemented yet",
      "source": "steelconnect",
      "displayText": "Error: This feature has not been implemented yet",
      "messages": [
        {
          "type": 0,
          "speech": "Error: This feature has not been implemented yet"
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "781b0f15-ed6f-461a-8cb0-7cbf2fd85f0b"
}

melbourne_shop_parameters = {
      "City": "Melbourne",
      "geo-city": "",
      "SiteTypes": "shop",
      "Uplinks": "uplink"
}

melbourne_shop_success_speech_response = "An uplink had created in site Melbourne_shop"
melbourne_shop_400_speech_response = "Invalid parameters: Invalid param: site"
melbourne_shop_400_api_response = {"error": {"message": "Invalid param: site", "code": 400}}
melbourne_shop_500_speech_response = "Error: Could not create uplink"
melbourne_shop_500_api_response = json.dumps({"error": {"message": "Error creating uplink", "code": 500}})
melbourne_shop_404_speech_response = "Error: Could not connect to Steelconnect"