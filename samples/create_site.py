import json

finland_helsinki_json_request = {
    "timestamp": "2017-04-28T04:25:19.21Z",
    "status": {
        "errorType": "success",
        "code": 200
    },
    "lang": "en",
    "result": {
        "fulfillment": {
            "speech": "Sorry Steel Connect is unavailable at the moment",
            "messages": [
                {
                    "type": 0,
                    "speech": "Sorry Steel Connect is unavailable at the moment"
                }
            ]
        },
        "metadata": {
            "intentName": "CreateSiteIntent",
            "webhookUsed": "true",
            "intentId": "a8eec3d5-d453-486f-bca5-ca454c12233d",
            "webhookForSlotFillingUsed": "false"
        },
        "parameters": {
            "SiteType": "shop",
            "Country": {
                "name": "Finland",
                "alpha-3": "FIN",
                "alpha-2": "FI",
                "numeric": 246
            },
            "States": "",
            "City": "Helsinki"
        },
        "speech": "",
        "action": "CreateSite",
        "source": "agent",
        "contexts": [],
        "actionIncomplete": False,
        "resolvedQuery": "Create shop in helsinki, finland",
        "score": 1.0
    },
    "id": "3c9a5197-77db-4de7-95a4-6b8806ed96e5",
    "sessionId": "a67d1455-dc63-4015-8848-0a8478382b2c"
}

finland_helsinki_parameters = {
            "SiteType": "shop",
            "Country": {
                "name": "Finland",
                "alpha-3": "FIN",
                "alpha-2": "FI",
                "numeric": 246
            },
            "States": "",
            "City": "Helsinki"
        }

finland_helsinki_success_speech_response = "Shop created in Helsinki, Finland"
finland_helsinki_400_speech_response = "Invalid parameters: Attribute 'name' must be unique"
finland_helsinki_400_api_response = {"error": {"message": "Attribute 'name' must be unique", "code": 400}}
finland_helsinki_500_speech_response = "Error: Could not create uplink"
finland_helsinki_500_api_response = json.dumps({"error": {"message": "Error creating site", "code": 500}})
finland_helsinki_404_speech_response = "Error: Could not connect to Steelconnect"

