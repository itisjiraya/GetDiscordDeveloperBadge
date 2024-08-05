import json
import os
import msvcrt
import sys
from urllib.request import Request, urlopen
from getpass import getpass
from src.utils import agreement
from typing import Optional, List
import gettext


class Utils:
    def __init__(self):
        self._ = gettext.gettext

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
        print("Please provide the Discord bot token\nYou can find the instructions in the README.md and by pressing "
              "\"2\".\n\n1. Enter bot token\n2. Instructions\n3. Edit EULA\n0. Exit")

        user_input = self.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            token = getpass("Enter bot token: (HIDDEN)").strip()
            if self.validation_check(token=token):
                print("НОрм")

        elif user_input == "2":
            print(self._("Press any key to continue..."))
            msvcrt.getch()
            return self.token_request()

        elif user_input == "3":
            return agreement.agreement_instance.license_confirmation()

        elif user_input == "0":
            sys.exit()

        else:
            return self.token_request()

    @staticmethod
    def validation_check(token: str) -> bool:
        request = Request(url="https://discord.com/api/v10/users/@me",
                          headers={"Authorization": "Bot " + token, "User-Agent": "Mozilla/5.0"})
        try:
            with urlopen(request) as response:
                return print(response.status == 200)

        except Exception as e:
            print(f"Error validating token: {e}")
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
