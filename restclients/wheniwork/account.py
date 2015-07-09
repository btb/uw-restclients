from restclients.wheniwork import WhenIWork
from restclients.models.wheniwork import Account


class Accounts(WhenIWork):
    def get_account(self, account_id=""):
        """
        Return primary account resource, or account for given wheniwork
        account id.

        http://dev.wheniwork.com/#listing-accounts
        http://dev.wheniwork.com/#get-existing-account
        """
        url = "/2/account/%s" % account_id
        return self._account_from_json(self._get_resource(url)["account"])

    def get_accounts(self):
        """
        Return list of accounts.

        http://dev.wheniwork.com/#listing-accounts
        """
        url = "/2/account"

        accounts = []
        for entry in self._get_resource(url):
            accounts.append(self._account_from_json(entry))

        return accounts

    def update_account(self, account):
        """
        Update the passed account. Returns the updated account.

        http://dev.wheniwork.com/#create/update-account
        """
        url = "/2/account/%s" % account.account_id
        body = {"account": {"name": account.name}}

        data = self._put_resource(url, body)
        return self._account_from_json(data)

    def _account_from_json(self, data):
        account = Account()
        account.id = data["id"]
        account.company = data["company"]
        account.master_id = data["master_id"]
        return account
