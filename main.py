import json
import os
from src.utils import agreement
from src.utils import utils


def main():
    settings_dir = "./settings/"
    if not os.path.exists(settings_dir) or not os.path.exists(os.path.join(settings_dir, "settings.json")):
        utils.utils_instance.language_selection()

    try:
        with open(os.path.join(settings_dir, "settings.json"), "r") as settings_file:
            settings = json.load(settings_file)

            language = settings.get('language')

            if language not in ['ru', 'en']:
                utils.utils_instance.language_selection()

    except json.decoder.JSONDecodeError:
        utils.utils_instance.language_selection()

    agreement.agreement_instance.check_eula_file()


if __name__ == '__main__':
    main()
