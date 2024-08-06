import os
import msvcrt
from src.utils import input_handler
import sys

EULA_FILE_PATH = "resources/EULA.txt"


class LicenseManager:
    @staticmethod
    def check_eula_file() -> bool:
        os.system("cls")
        if os.path.exists(EULA_FILE_PATH):
            with open(EULA_FILE_PATH, "r") as eulaFile:
                if "The project is subject to the MIT license.\nEULA agreement=True" == eulaFile.read():
                    return True

                else:
                    return False

        else:
            open(EULA_FILE_PATH, "w+").write("The project is subject to the MIT license.\nEULA agreement=False")
            return False

    def open_license(self):
        os.system("cls")
        with open("resources/LICENSE", "r") as licenseFile:
            print(licenseFile.read())

        print("\nPress any key to continue...")
        msvcrt.getch()
        return self.license_confirmation()

    def license_confirmation(self):
        os.system("cls")
        print("Please confirm your agreement with the TOS license.\n\n1. Accept\n2. Decline\n3. Review\n0. Exit")

        user_input = input_handler.InputHandler.input_request(["1", "2", "3", "0"])

        if user_input == "1":
            with open(EULA_FILE_PATH, "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA agreement=True")

            return input_handler.input_handler_instance.token_request()

        elif user_input == "2":
            with open(EULA_FILE_PATH, "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA agreement=False")
            print("License is mandatory for acceptance. ^-^")
            sys.exit()

        elif user_input == "3":
            self.open_license()
            return self.license_confirmation()

        else:
            sys.exit()


license_manager_instance = LicenseManager()
