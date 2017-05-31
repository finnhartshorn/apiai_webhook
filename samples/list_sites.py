case1_basic_request = {
  "id": "789842f4-26b8-4193-9290-b8b00e83e37e",
  "timestamp": "2017-05-30T02:19:45.592Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "List sites",
    "action": "ListSites",
    "actionIncomplete": False,
    "parameters": {},
    "contexts": [],
    "metadata": {
      "intentId": "e6eea4ea-a890-4117-ba1b-83bf227493aa",
      "webhookUsed": "true",
      "webhookForSlotFillingUsed": "false",
      "webhookResponseTime": 72,
      "intentName": "ListSites"
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
  "sessionId": "62e05bd1-9637-403b-ac7a-d46d1ed4f941"
}


case1_success_0_sites_return = {"items":[]}
case1_success_1_site_return = {"items":[{"name": "Berlin_Shop"}]}
case1_success_2_sites_return = {"items":[1, 2]}                         # TODO: Use actual data
case1_success_5_sites_return = {"items":[1, 2, 3, 4, 5]}
case1_404_return = None

case1_success_0_sites = "There are no sites in the Monash organisation"
case1_success_1_site = "There is one site in the Monash organisation, it is called Berlin_Shop"
case1_success_2_sites = "There are 2 sites in the Monash organisation, would you like to list all of them?"
case1_success_5_sites = "There are 5 sites in the Monash organisation, would you like to list all of them?"

case1_404 = "Error: Could not connect to Steelconnect"
