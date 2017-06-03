import json

denver_shop_wan_json_request = {
  "id": "61673b50-19fb-44ab-876a-30cfb6403671",
  "timestamp": "2017-06-03T05:41:59.14Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "create a wan in the shop in Denver",
    "action": "",
    "actionIncomplete": False,
    "parameters": {
      "City": "Denver",
      "SiteTypes": "shop",
      "WAN": "WAN"
    },
    "contexts": [],
    "metadata": {
      "intentId": "9eb0e729-4722-40d3-99ab-da7228ff71b8",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "CreateWanIntent"
    },
    "fulfillment": {
      "speech": "",
      "messages": [
        {
          "type": 0,
          "speech": ""
        }
      ]
    },
    "score": 1
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "2d7d1886-5aa2-498a-8dca-10c2846ac079"
}

denver_shop_wan_parameters = {
      "City": "Denver",
      "SiteTypes": "shop",
      "WAN": "WAN"
    }

denver_shop_wan_success_speech_response = "WAN created in Denver"
denver_shop_wan_400_speech_response = "Invalid parameters: Attribute 'name' must be unique"
denver_shop_wan_400_api_response = {"error": {"message": "Attribute 'name' must be unique", "code": 400}}
denver_shop_wan_500_speech_response = "Error: Could not create wan"
denver_shop_wan_500_api_response = json.dumps({"error": {"message": "Error creating site", "code": 500}})
denver_shop_wan_404_speech_response = "Error: Could not connect to Steelconnect"

