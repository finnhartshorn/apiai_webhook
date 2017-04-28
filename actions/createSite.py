import logging


def createSite(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteType"]
        city = parameters["City"]
        country = parameters["Country"]["alpha-2"]
        country_name = parameters["Country"]["name"]
    except KeyError as e:
        logging.error("Error processing createSite intent. {0}".format(e))

    speech = "Recieved request to create {} in {}, {}".format(site_type, city, country)

    # TODO: Handle this in calling class, just return speech
    response = {
        "speech": speech,
        "displayText": speech,
        "source": "steelconnect"
    }

    logging.debug(speech)

    return response
