from django.conf import settings
from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Location


class Locations(WhenIWork):
    def get_location(self, location_id):
        """
        Returns location data.

        http://dev.wheniwork.com/#get-existing-location
        """
        url = "/2/locations/%s" % location_id

        return self._location_from_json(self._get_resource(url)["location"])

    def get_locations(self):
        """
        Returns a list of locations.

        http://dev.wheniwork.com/#listing-locations
        """
        url = "/2/locations"

        data = self._get_resource(url)
        locations = []
        for entry in data['locations']:
            locations.append(self._location_from_json(entry))

        return locations

    def create_location(self, params={}):
        """
        Creates a location

        http://dev.wheniwork.com/#create/update-location
        """
        url = "/2/locations/"
        body = params

        data = self._post_resource(url, body)
        return self._location_from_json(data["location"])

    def _location_from_json(self, data):
        location = Location()
        location.id = data["id"]
        location.name = data["name"]
        location.address = data["address"]
        return location
