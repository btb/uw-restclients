from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Message
import dateutil.parser
from urllib import urlencode


class Messages(WhenIWork):
    def get_message(self, message_id):
        """
        Get Existing Message

        http://dev.wheniwork.com/#get-existing-message
        """
        url = "/2/messages/%s" % message_id

        return self._message_from_json(self._get_resource(url)["message"])

    def get_messages(self, params={}):
        """
        List messages

        http://dev.wheniwork.com/#listing-messages
        """
        url = "/2/messages/?%s" % urlencode(params)

        data = self._get_resource(url)
        messages = []
        for entry in data["messages"]:
            message = self._message_from_json(entry)
            message.save()
            messages.append(self._message_from_json(entry))

        return messages

    def create_message(self, params={}):
        """
        Creates a message

        http://dev.wheniwork.com/#create/update-message
        """
        url = "/2/messages/"
        body = params

        data = self._post_resource(url, body)
        return self._message_from_json(data["message"])

    def update_message(self, message):
        """
        Modify an existing message.

        http://dev.wheniwork.com/#create/update-message
        """
        url = "/2/messages/%s" % message.message_id

        data = self._put_resource(url, message.json_data())
        return self._message_from_json(data)

    def delete_messages(self, messages):
        """
        Delete existing messages.

        http://dev.wheniwork.com/#delete-existing-message
        """
        url = "/2/messages/?%s" % urlencode({'ids': ",".join(messages)})

        data = self._delete_resource(url)
        return data

    def _message_from_json(self, data):
        message = Message()
        message.id = data['id']
        message.account_id = data['account_id']
        message.user_id = data['user_id']
        message.request_id = data['request_id']
        message.swap_id = data['swap_id']
        message.conversation_id = data['conversation_id']
        message.title = data['title']
        message.content = data['content']
        message.created_at = dateutil.parser.parse(data['created_at'])
        message.updated_at = dateutil.parser.parse(data['updated_at'])
        message.type = data['type']
        return message
