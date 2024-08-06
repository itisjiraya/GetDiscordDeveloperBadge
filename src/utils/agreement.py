import os
import msvcrt
from src.utils import utils
import sys

EULA_FILE = "EULA.txt"


class Agreement:
    @staticmethod
    def check_eula_file() -> bool:
        """
        Check if the EULA.txt file exists and if it contains the correct license.
        """
        os.system("cls")
        if os.path.exists(EULA_FILE):
            with open(EULA_FILE, "r") as eulaFile:
                if "The project is subject to the MIT license.\nEULA agreement=True" == eulaFile.read():
                    return True

                else:
                    return False

        else:
            open(EULA_FILE, "w+").write("The project is subject to the MIT license.\nEULA agreement=False")
            return False

    def open_license(self):
        """
        Opens the LICENSE file and prints its contents to the console.
        Clears the console screen before displaying the license.
        Prompts the user to press any key to continue.
        Returns the result of the license_confirmation method.
        """
        os.system("cls")
        with open("LICENSE", "r") as file:
            print(file.read())
        print("\nPress any key to continue...")
        msvcrt.getch()
        return self.license_confirmation()

    def license_confirmation(self):
        """
        Prompts the user to confirm their agreement with the terms of use license.

        This function displays a menu with options to accept, decline, review, or exit.
        The user's input is validated and the appropriate action is taken based on the input.
        """
        os.system("cls")
        print("Please confirm your agreement with the TOS license.\n\n1. Accept\n2. Decline\n3. Review\n0. Exit")

        user_input = utils.Utils.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            with open(EULA_FILE, "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA agreement=True")

            return utils.utils_instance.token_request()

        elif user_input == "2":
            with open(EULA_FILE, "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA agreement=False")
            print("License is mandatory for acceptance. ^-^")
            sys.exit()

        elif user_input == "3":
            self.open_license()
            return self.license_confirmation()

        else:
            sys.exit()


agreement_instance = Agreement()
