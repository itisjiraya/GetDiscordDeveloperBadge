import gettext
import msvcrt
import os
import sys
from getpass import getpass
from typing import Optional, List
from src.utils import utils, licence_manager, language_manager


class InputHandler:
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
        print(
            self._(
                "Please provide the Discord bot token\nYou can find the instructions in the README.md and by pressing "
                "\"2\".\n\n1. Enter bot token\n2. Instructions\n3. Edit EULA\n0. Exit"))

        user_input = self.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            token = getpass("Enter bot token: (HIDDEN)").strip()

            if utils.utils_instance.validation_check(token=token):
                return NotImplemented

            else:
                print(self._("\n1. Try again\n0. Exit"))

                user_input = self.input_request(["1", "0"])

                if user_input == "1":
                    return self.token_request()

                sys.exit()

        elif user_input == "2":
            os.system("cls")
            with open(f"docs/README_{language_manager.LanguageManager.language_check()}.md", "r",
                      encoding="utf-8") as readme_file:
                print(readme_file.read())

            print("\nPress any key to continue...")
            msvcrt.getch()

            return self.token_request()

        elif user_input == "3":
            return licence_manager.license_manager_instance.license_confirmation()

        sys.exit()


input_handler_instance = InputHandler()
