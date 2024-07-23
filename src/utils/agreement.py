import os
import msvcrt
from src.utils.utils import _utils
import sys

class Agreement:    
    """
    class
    """
    def __init__(self):
        self.clear_screen = os.system("cls")

    def check_eula_file(self):
        self.clear_screen()
        if os.path.exists("EULA.txt"):
            with open("EULA.txt", "r") as eulaFile:
                if "The project is subject to the MIT license.\nEULA=True" == eulaFile.read():
                    return _utils.token_request()
                
                else:
                    return self.license_confirmation()
                
        else:
            open("EULA.txt", "w+").write("The project is subject to the MIT license.\nEULA=False")
            return self.license_confirmation()

    def open_license(self):
        self.clear_screen()
        with open("LICENSE", "r") as file:
            print(file.read())
        print("\nPress any key to continue...")
        msvcrt.getch()
        return self.license_confirmation()

    def license_confirmation(self):
        self.clear_screen()
        print("Please confirm your agreement with the terms of use license.\n\n1. Accept\n2. Decline\n3. Review\n0. Exit")

        
        user_input = _utils.input_request(["1", "2", "3", "0"])
            
        if user_input == "1":
            with open("EULA.txt", "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA=True")

            return _utils.token_request()

        elif user_input == "2":
            with open("EULA.txt", "w") as eulaFile:
                eulaFile.write("The project is subject to the MIT license.\nEULA=False")
            print("License is mandatory for acceptance. ^-^")
            sys.exit()

        elif user_input == "3":
            self.open_license()
            return self.license_confirmation()

        else:
            sys.exit()


_agreement = Agreement()

_agreement.license_confirmation()