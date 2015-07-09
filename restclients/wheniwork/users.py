from django.conf import settings
from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import User
from urllib import urlencode


class Users(WhenIWork):
    def get_user(self, user_id):
        """
        Returns user profile data.

        http://dev.wheniwork.com/#get-existing-user
        """
        url = "/2/users/%s" % user_id

        return self._user_from_json(self._get_resource(url)["user"])

    def get_users(self, params={}):
        """
        Returns a list of users.

        http://dev.wheniwork.com/#listing-users
        """
        url = "/2/users/?%s" % urlencode(params)

        data = self._get_resource(url)
        users = []
        for entry in data["users"]:
            users.append(self._user_from_json(entry))

        return users

    def _user_from_json(self, data):
        user = User()
        user.id = data["id"]
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.email = data["email"] if "email" in data else None
        user.employee_code = data["employee_code"]

        return user
