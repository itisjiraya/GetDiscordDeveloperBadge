import json
import os
from src.utils import licence_manager, language_manager, input_handler


def main():
    settings_dir = "./settings/"
    if not os.path.exists(settings_dir) or not os.path.exists(os.path.join(settings_dir, "settings.json")):
        language_manager.LanguageManager.language_selection()

    try:
        with open(os.path.join(settings_dir, "settings.json"), "r") as settings_file:
            settings = json.load(settings_file)

            language = settings.get('language')

            if language not in ['ru', 'en']:
                language_manager.LanguageManager.language_selection()

    except json.decoder.JSONDecodeError:
        language_manager.LanguageManager.language_selection()

    if licence_manager.LicenseManager.check_eula_file():
        input_handler.input_handler_instance.token_request()

    else:
        licence_manager.license_manager_instance.license_confirmation()


if __name__ == "__main__":
    main()
