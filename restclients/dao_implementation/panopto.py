"""
Contains Panopto DAO implementations.
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

    RESTCLIENTS_PANOPTO_DAO_CLASS = 'restclients.dao_implementation.panopto.File'
    """
    def getURL(self, url, headers):
        return get_mockdata_url("panopto", "file", url, headers)


class Live(object):
    """
    This DAO provides real data.  It requires the following configuration:

    RESTCLIENTS_PANOPTO_HOST="https://[...].hosted.panopto.com"
    RESTCLIENTS_PANOPTO_COOKIE=".ASPXAUTH=[...]"
    """
    pool = None
    ignore_security = getattr(settings,
                              'RESTCLIENTS_PANOPTO_IGNORE_CA_SECURITY',
                              False)

    verify_https = True
    if ignore_security:
        verify_https = False

    def getURL(self, url, headers):
        host = settings.RESTCLIENTS_PANOPTO_HOST
        cookie = settings.RESTCLIENTS_PANOPTO_COOKIE

        headers["Cookie"] = cookie

        if Live.pool is None:
            Live.pool = self._get_pool()
        return get_live_url(Live.pool, 'GET',
                            host, url, headers=headers,
                            service_name='panopto')

    def _get_pool(self):
        host = settings.RESTCLIENTS_PANOPTO_HOST
        socket_timeout = 15  # default values
        if hasattr(settings, "RESTCLIENTS_PANOPTO_SOCKET_TIMEOUT"):
            socket_timeout = settings.RESTCLIENTS_PANOPTO_SOCKET_TIMEOUT
        return get_con_pool(host,
                            verify_https=Live.verify_https,
                            socket_timeout=socket_timeout)
