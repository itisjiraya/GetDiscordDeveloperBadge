from urllib.request import Request, urlopen
from urllib.error import HTTPError
import gettext


class Utils:
    def __init__(self):
        self._ = gettext.gettext

    def validation_check(self, token: str = None) -> bool:
        if token is None:
            return False

        request = Request(url="https://discord.com/api/v10/users/@me",
                          headers={"Authorization": "Bot " + token, "User-Agent": "Mozilla/5.0"})

        try:
            with urlopen(request) as response:
                return response.status == 200

        except HTTPError as e:
            if e.code == 401:
                print(self._("Invalid bot token."))
                return False

            print(f"HTTP error occurred: {e.code}")
            return False

        except UnicodeEncodeError:
            print(self._("Invalid bot token."))
            return False


utils_instance = Utils()
