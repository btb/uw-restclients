from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Shift
import dateutil.parser
from urllib import urlencode


class Shifts(WhenIWork):
    def get_shift(self, shift_id):
        """
        Get Existing Shift

        http://dev.wheniwork.com/#get-existing-shift
        """
        url = "/2/shifts/%s" % shift_id

        return self._shift_from_json(self._get_resource(url))

    def get_shifts(self, params={}):
        """
        List shifts

        http://dev.wheniwork.com/#listing-shifts
        """
        url = "/2/shifts/?%s" % urlencode(params)

        data = self._get_resource(url)
        shifts = []
        for shift in data["shifts"]:
            shift = self._shift_from_json(shift)
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
        return self._shift_from_json(data["shift"])

    def update_shift(self, shift):
        """
        Modify an existing shift.

        http://dev.wheniwork.com/#create/update-shift
        """
        url = "/2/shifts/%s" % shift.shift_id

        data = self._put_resource(url, shift.json_data())
        return self._shift_from_json(data)

    def delete_shifts(self, shifts):
        """
        Delete existing shifts.

        http://dev.wheniwork.com/#delete-shift
        """
        url = "/2/shifts/?%s" % urlencode({ 'ids': ",".join(shifts) })

        data = self._delete_resource(url)
        return data

    def _shift_from_json(self, data):
        shift = Shift()
        shift.shift_id = data['id']
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
