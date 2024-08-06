import json
import os
import sys

from src.utils import input_handler


class LanguageManager:
    @staticmethod
    def language_check():
        if not os.path.exists("settings/settings.json"):
            return False

        try:
            with open("settings/settings.json", "r") as settings_file:
                settings = json.load(settings_file)

        except json.decoder.JSONDecodeError:
            return False

        return settings.get("language", False)

    @staticmethod
    def language_selection():
        os.system("cls")

        print("Select language | Выберите язык\n\n1. English\n2. Русский\n0. Exit | Выход")
        user_input = input_handler.InputHandler.input_request(["1", "2", "0"])

        if user_input == "0":
            sys.exit()

        settings_dir = "settings/"

        if not os.path.exists(settings_dir):
            os.makedirs(settings_dir)

        with open(os.path.join(settings_dir, "settings.json"), "w") as settings_file:
            json.dump({"language": "en" if user_input == "1" else "ru"}, settings_file, indent=4)
