import json
import os
import msvcrt
import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from getpass import getpass
from src.utils import agreement
from typing import Optional, List
import gettext


class Utils:
    def __init__(self):
        self._ = gettext.gettext

    @staticmethod
    def language_check():
        if not os.path.exists("settings/settings.json"):
            return None

        with open("settings/settings.json", "r") as settings_file:
            settings = json.load(settings_file)

            return settings.get("language")

    @staticmethod
    def input_request(available_answers: Optional[List[str]] = None) -> str:
        if not available_answers:
            while True:
                try:
                    return msvcrt.getch().decode()
                except UnicodeDecodeError:
                    continue

        while True:
            try:
                user_input = msvcrt.getch().decode()
                if user_input in available_answers:
                    return user_input
            except UnicodeDecodeError:
                continue

    def token_request(self):
        os.system("cls")
        print(
            self._(
                "Please provide the Discord bot token\nYou can find the instructions in the README.md and by pressing "
                "\"2\".\n\n1. Enter bot token\n2. Instructions\n3. Edit EULA\n0. Exit"))

        user_input = self.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            token = getpass("Enter bot token: (HIDDEN)").strip()

            if self.validation_check(token=token):
                return NotImplemented

            else:
                print(self._("\n1. Try again\n0. Exit"))

                user_input = self.input_request(["1", "0"])

                if user_input == "1":
                    return self.token_request()

                sys.exit()

        elif user_input == "2":
            os.system("cls")
            with open(f"docs/README_{self.language_check()}.md", "r", encoding="utf-8") as readme_file:
                print(readme_file.read())

            print("\nPress any key to continue...")
            msvcrt.getch()

            return self.token_request()

        elif user_input == "3":
            return agreement.agreement_instance.license_confirmation()

        sys.exit()

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

    def language_selection(self) -> None:
        os.system("cls")
        print("Select language | Выберите язык\n\n1. English\n2. Русский\n0. Exit | Выход")

        user_input = self.input_request(["1", "2", "0"])

        if user_input == "0":
            sys.exit()

        settings_dir = "./settings/"
        if not os.path.exists(settings_dir):
            os.makedirs(settings_dir)

        if user_input == "1":
            with open(os.path.join(settings_dir, "settings.json"), "w") as settings_file:
                json.dump({"language": "en"}, settings_file, indent=4)
                return

        with open(os.path.join(settings_dir, "settings.json"), "w") as settings_file:
            json.dump({"language": "ru"}, settings_file, indent=4)


utils_instance = Utils()
