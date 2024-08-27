import json
from enum import Enum


class Settings:
    class ScriptBehavior(Enum):
        IGNORE_OUTSIDE = "IgnoreOutsideJsonModifications"

    class Section(Enum):
        SCRIPT_BEHAVIOR = "ScriptBehavior"

    def __init__(self, path=""):
        self.path = path
        self._main_setting_key = "Settings"
        self._settings_file = "Settings.json"
        self._settings_json = self._read_settings()

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

    def get_setting(self, section: Section, setting: Enum):
        section_name = section.value
        setting_name = setting.value
        return self._settings_json.get(self._main_setting_key).get(section_name).get(setting_name)

    def _generate_settings(self):
        settings = {
            self._main_setting_key: {
                self.Section.SCRIPT_BEHAVIOR.value: {
                    self.ScriptBehavior.IGNORE_OUTSIDE.value: False
                }
            }
        }
        # Write settings to file
        with open(self.path + self._settings_file, 'w') as settings_file:
            json.dump(settings, settings_file, indent=4)
        print("Settings file generated. Please modify the settings file before running the script. - ✅")
