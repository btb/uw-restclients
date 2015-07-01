"""
Contains When I Work DAO implementations.
"""

from restclients.dao_implementation.live import get_con_pool, get_live_url
from restclients.dao_implementation.mock import get_mockdata_url, \
    post_mockdata_url, delete_mockdata_url, put_mockdata_url
from django.conf import settings
from os.path import abspath, dirname


class File(object):
    """
    The File DAO implementation returns generally static content.  Use this
    DAO with this configuration:

    RESTCLIENTS_WHENIWORK_DAO_CLASS =
    'restclients.dao_implementation.wheniwork.File'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("wheniwork", "file", url, headers)

    def putURL(self, url, headers, body):
        response = put_mockdata_url("wheniwork", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/wheniwork/file" +
                       url + ".PUT")

        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def postURL(self, url, headers, body):
        response = post_mockdata_url("wheniwork", "file", url, headers, body)
        if response.status == 400:
            return response

        path = abspath(dirname(__file__) + "/../resources/wheniwork/file" +
                       url + ".POST")
        try:
            handle = open(path)
            response.data = handle.read()
            response.status = 200
        except IOError:
            response.status = 404

        return response

    def deleteURL(self, url, headers):
        return delete_mockdata_url("wheniwork", "file", url, headers)


class Live(object):
    """
    This DAO provides real data.  It requires the following configuration:

    RESTCLIENTS_WHENIWORK_HOST="api.wheniwork.com"
    RESTCLIENTS_WHENIWORK_TOKEN="..."
    """
    pool = None
    ignore_security = getattr(settings,
                              'RESTCLIENTS_WHENIWORK_IGNORE_CA_SECURITY',
                              False)

    verify_https = True
    if ignore_security:
        verify_https = False

    def getURL(self, url, headers):
        host = settings.RESTCLIENTS_WHENIWORK_HOST
        token = settings.RESTCLIENTS_WHENIWORK_TOKEN

        headers["W-Token"] = "%s" % token

        if Live.pool is None:
            Live.pool = self._get_pool()
        return get_live_url(Live.pool, 'GET',
                            host, url, headers=headers,
                            service_name='wheniwork')

    def putURL(self, url, headers, body):
        host = settings.RESTCLIENTS_WHENIWORK_HOST
        token = settings.RESTCLIENTS_WHENIWORK_TOKEN

        headers["W-Token"] = "%s" % token

        if Live.pool is None:
            Live.pool = self._get_pool()
        return get_live_url(Live.pool, 'PUT',
                            host, url, headers=headers, body=body,
                            service_name='wheniwork')

    def postURL(self, url, headers, body):
        host = settings.RESTCLIENTS_WHENIWORK_HOST
        token = settings.RESTCLIENTS_WHENIWORK_TOKEN

        headers["W-Token"] = "%s" % token

        if Live.pool is None:
            Live.pool = self._get_pool()
        return get_live_url(Live.pool, 'POST',
                            host, url, headers=headers, body=body,
                            service_name='wheniwork')

    def deleteURL(self, url, headers):
        host = settings.RESTCLIENTS_WHENIWORK_HOST
        token = settings.RESTCLIENTS_WHENIWORK_TOKEN

        headers["W-Token"] = "%s" % token

        if Live.pool is None:
            Live.pool = self._get_pool()
        return get_live_url(Live.pool, 'DELETE',
                            host, url, headers=headers,
                            service_name='wheniwork')

    def _get_pool(self):
        host = settings.RESTCLIENTS_WHENIWORK_HOST
        socket_timeout = 15  # default values
        if hasattr(settings, "RESTCLIENTS_WHENIWORK_SOCKET_TIMEOUT"):
            socket_timeout = settings.RESTCLIENTS_WHENIWORK_SOCKET_TIMEOUT
        return get_con_pool(host,
                            verify_https=Live.verify_https,
                            socket_timeout=socket_timeout)
