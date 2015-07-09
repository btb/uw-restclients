from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Request
from restclients.wheniwork.users import Users
from restclients.wheniwork.messages import Messages
import dateutil.parser
from urllib import urlencode


class Requests(WhenIWork):
    def get_request(self, request_id):
        """
        Get Existing Request

        http://dev.wheniwork.com/#get-existing-request
        """
        url = "/2/requests/%s" % request_id

        return self._request_from_json(self._get_resource(url)["request"])

    def get_requests(self, params={}):
        """
        List requests

        http://dev.wheniwork.com/#listing-requests
        """
        url = "/2/requests/?%s" % urlencode(params)

        data = self._get_resource(url)
        requests = []
        for entry in data["users"]:
            user = Users()._user_from_json(entry)
            user.save()
        for entry in data["requests"]:
            request = self._request_from_json(entry)
            request.save()
            requests.append(request)
        for entry in data["messages"]:
            message = Messages()._message_from_json(entry)
            message.save()

        return requests

    def create_request(self, params={}):
        """
        Creates a request

        http://dev.wheniwork.com/#create/update-request
        """
        url = "/2/requests/"
        body = params

        data = self._post_resource(url, body)
        return self._request_from_json(data["request"])

    def update_request(self, request):
        """
        Modify an existing request.

        http://dev.wheniwork.com/#create/update-request
        """
        url = "/2/requests/%s" % request.request_id

        data = self._put_resource(url, request.json_data())
        return self._request_from_json(data)

    def delete_requests(self, requests):
        """
        Delete existing requests.

        http://dev.wheniwork.com/#delete-existing-request
        """
        url = "/2/requests/?%s" % urlencode({'ids': ",".join(requests)})

        data = self._delete_resource(url)
        return data

    def _request_from_json(self, data):
        request = Request()
        request.id = data['id']
        request.account_id = data['account_id']
        request.user_id = data['user_id']
        request.creator_id = data['creator_id']
        request.status = data['status']
        request.type = data['type']
        request.start_time = dateutil.parser.parse(data['start_time'])
        request.end_time = dateutil.parser.parse(data['end_time'])
        request.created_at = dateutil.parser.parse(data['created_at'])
        request.updated_at = dateutil.parser.parse(data['updated_at'])
        request.canceled_by_id = data['canceled_by']
        request.hours = str(data['hours'])
        return request
