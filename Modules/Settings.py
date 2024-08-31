import json
from enum import Enum


class Settings:
    class ScriptBehavior:
        class SettingName(Enum):
            IGNORE_OUTSIDE = "IgnoreOutsideJsonModifications"
            MISSING_MONSTER_START_RARITY = "MissingMonsterStartRarity"
            INCREASE_MONSTER_RARITY_PER_RISK = "IncreaseMonsterRarityPerRisk"

        class SettingDescription(Enum):
            IGNORE_OUTSIDE = "Ignore outside json modifications. Outside.json will not be modified if set to True."
            MISSING_MONSTER_START_RARITY = "The starting rarity at D- Risk of the monster if the rarity is not found in the json file."
            INCREASE_MONSTER_RARITY_PER_RISK = "The amount of rarity to increase per risk level."

        class SettingType(Enum):
            IGNORE_OUTSIDE = bool,
            MISSING_MONSTER_START_RARITY = int,
            INCREASE_MONSTER_RARITY_PER_RISK = int

    def __init__(self, path=""):
        self._log_prefix = "Settings Module: "
        self._path = path
        # Initialize the settings dictionary with a dictionary for each section
        self._settings = {
            self.ScriptBehavior.__name__: {},
        }
        self._main_setting_key = "Settings"
        self._settings_file = "Settings.json"
        self._settings_json = self._read_settings()
        self._create_settings()
        self._validate_setting_types()
        self._print_settings_and_descriptions()

    def _log(self, message: str):
        print(self._log_prefix + message)

    def _print_settings_and_descriptions(self):
        self._log("Printing settings and descriptions:\n")
        # Calculate maximum lengths for alignment
        max_section_length = max(len(section) for section in self._settings.keys())
        max_setting_name_length = max(
            len(setting_name) for settings in self._settings.values() for setting_name in settings.keys())
        max_value_length = max(
            len(str(setting['value'])) for settings in self._settings.values() for setting in settings.values())

        for section, settings in self._settings.items():
            for setting_name, setting in settings.items():
                value = str(setting['value'])
                description = setting['description']
                self._log(
                    f"{setting_name.ljust(max_setting_name_length)}: {value.ljust(max_value_length)} - {description}\n")
        input("\nPress enter to continue...")

    def _read_settings(self):
        try:
            with open(self._path + self._settings_file, 'r') as settings_file:
                return json.load(settings_file)
        except FileNotFoundError:
            self._log("Settings file not found.  - ❌")
            self._generate_settings()
            input("Press enter to exit...")
            exit(0)
        except json.JSONDecodeError:
            self._log(
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
        self._log("Settings file generated. Please modify the settings file before running the script. - ✅")

    def _create_settings(self):
        # Process each section and its associated settings
        for section, setting_enum in [("ScriptBehavior", self.ScriptBehavior.SettingName)]:
            for setting in setting_enum:
                setting_value = self._get_setting_value_from_json(section, setting.value)
                setting_description = getattr(self.ScriptBehavior.SettingDescription, setting.name).value
                self._settings[section][setting.value] = {
                    "value": setting_value,
                    "description": setting_description
                }

    def _validate_setting_types(self):
        for name, expected_type, description in zip(Settings.ScriptBehavior.SettingName,
                                                    Settings.ScriptBehavior.SettingType,
                                                    Settings.ScriptBehavior.SettingDescription):
            setting_value = self._settings[Settings.ScriptBehavior.__name__][name.value]["value"]
            if not isinstance(setting_value, expected_type.value):
                self._log(f"Setting {name.value} is not of type {expected_type.value}. - ❌")
                self._log(
                    "This means the setting file has an incorrect value type. Please fix the settings file and try again.")
                self._log(f"Expected type: {expected_type.value}, Actual type: {type(setting_value)}")
                exit(0)

    def get_setting_value(self, setting_name: "Settings.ScriptBehavior.SettingName"):
        return self._settings.get(Settings.ScriptBehavior.__name__).get(setting_name.value, {}).get("value")
