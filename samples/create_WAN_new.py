import json

create_mpls_wan = {
  "id": "e3299418-aa05-4c96-b2b7-0e17c637b4fa",
  "timestamp": "2017-08-09T07:59:10.373Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "Create an MPLS",
    "action": "",
    "actionIncomplete": False,
    "parameters": {
      "WAN": "",
      "WANType": "MPLS"
    },
    "contexts": [],
    "metadata": {
      "intentId": "c8554705-522f-44f4-864c-3b2cf85f0724",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 169,
      "intentName": "CreateWAN"
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
    "score": 0.7400000095367432
  },
  "status": {
    "code": 200,
    "errorType": "success"
  },
  "sessionId": "ccd9e7e8-086a-4f30-95b6-de3abf0562b0"
}

mpls_success_speech_response = "MPLS created"
mpls_404 = "Error: Could not connect to Steelconnect"
mpls_400_api_response = {"error": {"message": "Attribute 'name' must be unique", "code": 400}}
mpls_400_expected = "Invalid parameters: Attribute 'name' must be unique"
mpls_500_api_response = json.dumps({"error": {"message": "Failed to create wan", "code": 500}})
mpls_500_expected = "Error: Could not create WAN"