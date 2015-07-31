from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Shift
from restclients.wheniwork.locations import Locations
from restclients.wheniwork.sites import Sites
from restclients.wheniwork.positions import Positions
from restclients.wheniwork.users import Users
import dateutil.parser
from urllib import urlencode


class Shifts(WhenIWork):
    def get_shifts(self, params={}):
        """
        List shifts

        http://dev.wheniwork.com/#listing-shifts
        """
        url = "/2/shifts/?%s" % urlencode(params)

        data = self._get_resource(url)
        shifts = []
        for entry in data.get("locations", []):
            location = Locations()._location_from_json(entry)
            location.save()
        for entry in data.get("sites", []):
            site = Sites()._site_from_json(entry)
            site.save()
        for entry in data.get("positions", []):
            position = Positions()._position_from_json(entry)
            position.save()
        for entry in data.get("users", []):
            user = Users()._user_from_json(entry)
            user.save()
        for entry in data["shifts"]:
            shift = self._shift_from_json(entry)
            shift.save()
            shifts.append(shift)

        return shifts

    def create_shift(self, params={}):
        """
        Creates a shift

        http://dev.wheniwork.com/#create/update-shift
        """
        url = "/2/shifts/"
        body = params

        data = self._post_resource(url, body)
        shift = self._shift_from_json(data["shift"])
        shift.save()

        return shift

    def delete_shifts(self, shifts):
        """
        Delete existing shifts.

        http://dev.wheniwork.com/#delete-shift
        """
        url = "/2/shifts/?%s" % urlencode({'ids': ",".join(shifts)})

        data = self._delete_resource(url)
        for shift in Shift().objects.filter(id__in=shifts):
            shift.delete()

        return data

    def _shift_from_json(self, data):
        shift = Shift()
        shift.id = data['id']
        shift.user_id = data['user_id']
        shift.account_id = data['account_id']
        shift.location_id = data['location_id']
        shift.position_id = data['position_id']
        shift.site_id = data['site_id']
        if 'start_time' in data and data['start_time']:
            shift.start_time = dateutil.parser.parse(data['start_time'])
        if 'end_time' in data and data['end_time']:
            shift.end_time = dateutil.parser.parse(data['end_time'])
        shift.notes = data['notes']
        return shift
