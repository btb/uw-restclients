from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Shift
import dateutil.parser


class Shifts(WhenIWork):
    def get_shift(self, shift_id):
        """
        Get Existing Shift

        http://dev.wheniwork.com/#get-existing-shift
        """
        url = "/2/shifts/%s" % shift_id

        return self._shift_from_json(self._get_resource(url))

    def get_shifts(self):
        """
        List shifts

        http://dev.wheniwork.com/#listing-shifts
        """
        url = "/2/shifts"

        data = self._get_resource(url)
        shifts = []
        for shift in data["shifts"]:
            shift = self._shift_from_json(shift)
            shifts.append(shift)
        return shifts

    def update_shift(self, shift):
        """
        Modify an existing shift.

        http://dev.wheniwork.com/#create/update-shift
        """
        url = "/2/shifts/%s" % shift.shift_id

        data = self._put_resource(url, shift.json_data())
        return self._shift_from_json(data)

    def _shift_from_json(self, data):
        shift = Shift()
        shift.shift_id = data['id']
        shift.user_id = data['user_id']
        shift.location_id = data['location_id']
        shift.position_id = data['position_id']
        shift.site_id = data['site_id']
        if 'start_time' in data and data['start_time']:
            shift.start_time = dateutil.parser.parse(data['start_time'])
        if 'end_time' in data and data['end_time']:
            shift.end_time = dateutil.parser.parse(data['end_time'])
        shift.notes = data['notes']
        return shift
