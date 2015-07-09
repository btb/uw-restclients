from django.conf import settings
from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Position


class Positions(WhenIWork):
    def get_position(self, position_id):
        """
        Returns position data.

        http://dev.wheniwork.com/#get-existing-position
        """
        url = "/2/positions/%s" % position_id

        return self._position_from_json(self._get_resource(url)["position"])

    def get_positions(self):
        """
        Returns a list of positions.

        http://dev.wheniwork.com/#listing-positions
        """
        url = "/2/positions"

        data = self._get_resource(url)
        positions = []
        for entry in data['positions']:
            positions.append(self._position_from_json(entry))

        return positions

    def create_position(self, params={}):
        """
        Creates a position

        http://dev.wheniwork.com/#create/update-position
        """
        url = "/2/positions/"
        body = params

        data = self._post_resource(url, body)
        return self._position_from_json(data["position"])

    def _position_from_json(self, data):
        position = Position()
        position.id = data["id"]
        position.name = data["name"]
        return position
