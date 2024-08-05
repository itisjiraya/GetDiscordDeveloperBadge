import json
import os
import msvcrt
import sys
from getpass import getpass
from src.utils import agreement
from typing import Optional, List
import gettext


class Utils:
    def __init__(self):
        self._ = gettext.gettext

    @staticmethod
    def input_request(available_answers: Optional[List[str]] = None) -> str:
        """
        Requests user input from the console and returns it as a string.

        This method waits for a single character input. If the `available_answers` parameter is provided, the method
        will only return a value if matches one of the specified valid answers. If `available_answers` is not provided
        or is an empty list, the method will accept any character input.

        :param available_answers: An optional list of valid answers. If provided, the method will only return a value
                                 that matches one of the answers in this list. If not provided or if the list is empty,
                                 any character input will be accepted.

        :return: The user's input as a string, which will either be a valid answer from `available_answers` or character
                 if no valid answers are specified.
        """
        if not available_answers:  # Accept any character input if no valid answers are specified.
            while True:
                try:
                    return msvcrt.getch().decode()  # Wait for a character input and decode it.
                except UnicodeDecodeError:  # Ignore non-string inputs (e.g., arrow keys).
                    continue

        while True:
            try:
                user_input = msvcrt.getch().decode()  # Wait for a character input and decode it.
                if user_input in available_answers:  # Check if the input is one of the valid answers.
                    return user_input  # Return the valid input.
            except UnicodeDecodeError:  # Ignore non-string inputs (e.g., arrow keys).
                continue

    def token_request(self):
        """
        Requests the Discord bot token from the console.

        This method presents the user with options to either enter the bot token manually, view instructions,
        edit the End User License Agreement (EULA), or exit the program. The user can choose from the following options:

        - '1': Enter the bot token manually.
        - '2': View instructions for obtaining the token.
        - '3': Edit the EULA.
        - '0': Exit the program.

        :return: The Discord bot token as a string if the user chooses to enter it manually.
                 If the user selects options '2', '3', or '0', the method will not return a token.
        """
        os.system("cls")  # Clear the console screen for better readability.
        print("Please provide the Discord bot token\nYou can find the instructions in the README.md and by pressing "
              "'2'.\n\n1. Enter bot token\n2. Instructions\n3. Edit EULA\n0. Exit")

        user_input = self.input_request(["1", "2", "3", "0"])  # Get user input for the desired action.

        if user_input == "1":
            secret = getpass("Enter bot token: (HIDDEN)").strip()  # Prompt for the bot token, keeping it hidden.
            print(secret)
            return self.validation_check(secret=secret)  # Validate and return the entered token.

        elif user_input == "2":
            # TODO: Implement instructions with relevant links.
            return NotImplemented  # Placeholder for future implementation.

        elif user_input == "3":
            return agreement.agreement_instance.license_confirmation()  # Handle EULA editing.

        elif user_input == "0":
            sys.exit()  # Exit the program.

        else:
            return self.token_request()

    def validation_check(self, secret: str):
        # TODO: Method logic
        return NotImplemented

    def language_selection(self) -> None:
        """
        Selects the language of the program and saves it to a JSON file.

        This method displays a menu with options to select the language. The user's input is validated and the
        appropriate action is taken based on the input. The selected language is saved to a JSON file.

        :return: None
        """
        os.system("cls")  # Clear the console screen for better readability.
        print("Select language | Выберите язык\n\n1. English\n2. Русский\n0. Exit | Выход")

        user_input = self.input_request(["1", "2", "0"])  # Get user input for the desired action.

        settings_dir = "./settings/"
        if not os.path.exists(settings_dir):
            os.makedirs(settings_dir)

        if user_input == "1":
            with open(os.path.join(settings_dir, "settings.json"), "w") as settings_file:
                json.dump({"language": "en"}, settings_file, indent=4)
                return

        elif user_input == "2":
            with open(os.path.join(settings_dir, "settings.json"), "w") as settings_file:
                json.dump({"language": "ru"}, settings_file, indent=4)
                return

        sys.exit()  # Exit the program.


utils_instance = Utils()
