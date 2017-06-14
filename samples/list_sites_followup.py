specify_number_first_two = {
  "id": "57ed89e3-ec8e-469d-b9d7-b160207aca43",
  "timestamp": "2017-06-01T04:31:47.155Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "List the first two",
    "action": "ListSites.ListSites-custom",
    "actionIncomplete": False,
    "parameters": {
      "number": "2",
      "position": "first"
    },
    "contexts": [
      {
        "name": "readsitelist",
        "parameters": {
          "number": "2",
          "position": "first",
          "number.original": "two",
          "position.original": "first"
        },
        "lifespan": 4
      },
      {
        "name": "listsites-followup",
        "parameters": {
          "number": "2",
          "position": "first",
          "number.original": "two",
          "position.original": "first"
        },
        "lifespan": 1
      }
    ],
    "metadata": {
      "intentId": "ec08bbcb-b5a3-416f-b070-59439bfd39d9",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "ListSites - custom"
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
  "sessionId": "1c1c237a-9c92-49dd-98b1-9cb473331497"
}

specify_all = {
  "id": "8ab93edd-1aa9-4491-9910-f08daa14c2a1",
  "timestamp": "2017-06-04T18:15:56.939Z",
  "lang": "en",
  "result": {
    "source": "agent",
    "resolvedQuery": "yes",
    "action": "ListSites.ListSites-yes",
    "actionIncomplete": False,
    "parameters": {},
    "contexts": [
      {
        "name": "readsitelist",
        "parameters": {},
        "lifespan": 4
      },
      {
        "name": "listsites-followup",
        "parameters": {},
        "lifespan": 1
      }
    ],
    "metadata": {
      "intentId": "5908978c-d440-48c9-a87c-cad641108ef3",
      "webhookUsed": "false",
      "webhookForSlotFillingUsed": "false",
      "intentName": "ListSites - yes"
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
  "sessionId": "1c1c237a-9c92-49dd-98b1-9cb473331497"
}