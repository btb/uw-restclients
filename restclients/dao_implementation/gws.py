"""
Contains GWS DAO implementations.
"""
from django.conf import settings
from restclients.mock_http import MockHTTP
from restclients.dao_implementation.live import get_con_pool, get_live_url
from restclients.dao_implementation.mock import get_mockdata_url

class File(object):
    """
    The File DAO implementation returns generally static content.  Use this
    DAO with this configuration:

    RESTCLIENTS_GWS_DAO_CLASS = 'restclients.dao_implementation.gws.File'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("gws", "file", url, headers)

    def putURL(self, url, headers, body):
        response = MockHTTP()

        if "If-Match" not in headers:
            response.status = 412
            return response

        if body is not None:
            response.status = 200
            response.headers = {"X-Data-Source": "GWS file mock data",
                                "Content-Type": headers["Content-Type"]}
            response.data = body
        else:
            response.status = 400                                                   
            response.data = "Bad Request: no POST body"

        return response

    def deleteURL(self, url, headers):
        response = MockHTTP()
        response.status = 200
        return response

class Live(object):
    """
    This DAO provides real data.  It requires further configuration, e.g.

    RESTCLIENTS_GWS_CERT_FILE='/path/to/an/authorized/cert.cert',
    RESTCLIENTS_GWS_KEY_FILE='/path/to/the/certs_key.key',
    RESTCLIENTS_GWS_HOST='https://iam-tools.u.washington.edu:443',
    """
    pool = None

    def getURL(self, url, headers):
        if Live.pool == None:
            Live.pool = self._get_pool() 

        return get_live_url(Live.pool, 'GET', 
                            settings.RESTCLIENTS_GWS_HOST,
                            url, headers=headers)

    def putURL(self, url, headers, body):
        if Live.pool == None:
            Live.pool = self._get_pool()

        return get_live_url(Live.pool, 'PUT',
                            settings.RESTCLIENTS_GWS_HOST,
                            url, headers=headers, body=body)

    def deleteURL(self, url, headers):
        if Live.pool == None:
            Live.pool = self._get_pool()

        return get_live_url(Live.pool, 'DELETE',
                            settings.RESTCLIENTS_GWS_HOST,
                            url, headers=headers)

    def _get_pool(self):
        return get_con_pool(settings.RESTCLIENTS_GWS_HOST,
                            settings.RESTCLIENTS_GWS_KEY_FILE,
                            settings.RESTCLIENTS_GWS_CERT_FILE,
                            max_pool_size=settings.RESTCLIENTS_GWS_MAX_POOL_SIZE)
