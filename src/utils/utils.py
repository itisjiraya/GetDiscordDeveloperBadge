import os
import msvcrt
import sys
from getpass import getpass
from agreement import _agreement
from typing import Optional, List

class Utils:
    """
    class
    """
    def __inits__(self):
        self.clear_screen = os.system("cls")
        
    def input_request(self, available_answers: Optional[List[str]] = None) -> str:
        if available_answers is None:
            return msvcrt.getch().decode()

        while True:
            user_input = msvcrt.getch().decode()
            if user_input in available_answers:
                break

        return user_input

    def token_request(self):
        os.system("cls")
        print("Please provide the Discord bot token\nYou can find the instructions in the README.md and by pressing '2'.\n1. Enter bot token\n2. Instructions\n3. Edit EULA\n0. Exit")

        user_input = self.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            secret = getpass("Enter bot token: (HIDDEN)")
            return self.validation_check(secret=secret)

        elif user_input == "2":
            # TODO: Make an instruction with links :D
            return NotImplemented

        elif user_input == "3":
            return _agreement.license_confirmation()

        elif user_input == "0":
            sys.exit()

        else:
            return self.token_request()

    def validation_check(self, secret):
        # TODO: Method logic
        return NotImplemented

_utils = Utils()
