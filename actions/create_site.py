import logging


def create_site(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    try:
        site_type = parameters["SiteType"]
        city = parameters["City"]
        country = parameters["Country"]["alpha-2"]
        country_name = parameters["Country"]["name"]

        speech = "{} created in {}, {}".format(site_type.capitalize(), city, country_name)

        logging.debug(speech)

        return speech

    except KeyError as e:

        error_string = "Error processing createSite intent. {0}".format(e)

        logging.error()

        return error_string

