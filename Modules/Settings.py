import json
from enum import Enum


class Settings:
    class ScriptBehavior:
        class SettingName(Enum):
            IGNORE_OUTSIDE = "IgnoreOutsideJsonModifications"

        class SettingDescription(Enum):
            IGNORE_OUTSIDE = "Ignore outside json modifications."

    def __init__(self, path=""):
        self.path = path
        # Initialize the settings dictionary with a dictionary for each section
        self.settings = {
            self.ScriptBehavior.__name__: {},
        }
        self._main_setting_key = "Settings"
        self._settings_file = "Settings.json"
        self._settings_json = self._read_settings()
        self._create_settings()

    def _read_settings(self):
        try:
            with open(self.path + self._settings_file, 'r') as settings_file:
                return json.load(settings_file)
        except FileNotFoundError:
            print("Settings file not found.  - ❌")
            self._generate_settings()
            input("Press enter to exit...")
            exit(0)
        except json.JSONDecodeError:
            print(
                "Error decoding the settings file. Delete the file and re-run this script will regenerate the settings file.")
            input("Press enter to exit...")
            exit(0)

    def _get_setting_value_from_json(self, section: str, setting_name: str):
        return self._settings_json.get(self._main_setting_key, {}).get(section, {}).get(setting_name)

    def _generate_settings(self):
        settings = {
            self._main_setting_key: {
                "ScriptBehavior": {
                    self.ScriptBehavior.SettingName.IGNORE_OUTSIDE.value: False,
                }
            }
        }
        # Write settings to file
        with open(self.path + self._settings_file, 'w') as settings_file:
            json.dump(settings, settings_file, indent=4)
        print("Settings file generated. Please modify the settings file before running the script. - ✅")

    def _create_settings(self):
        # Process each section and its associated settings
        for section, setting_enum in [("ScriptBehavior", self.ScriptBehavior.SettingName)]:
            for setting in setting_enum:
                setting_value = self._get_setting_value_from_json(section, setting.value)
                setting_description = getattr(self.ScriptBehavior.SettingDescription, setting.name).value
                self.settings[section][setting.value] = {
                    "value": setting_value,
                    "description": setting_description
                }

    def get_setting_value(self, setting_name: "Settings.ScriptBehavior.SettingName"):
        return self.settings.get(Settings.ScriptBehavior.__name__).get(setting_name.value, {}).get("value")
