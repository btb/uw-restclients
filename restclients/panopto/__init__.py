"""
This is the interface for interacting with Panopto's private web service.
"""
from restclients.dao import Panopto_DAO
from restclients.exceptions import DataFailureException
import json


def get_resource(url):
    """
    Panopto GET method. Returns representation of the requested resource.
    """
    response = Panopto_DAO().getURL(url, {"Accept": "application/json"})

    if response.status != 200:
        raise DataFailureException(url, response.status, response.data)

    data = json.loads(response.data)

    return data
