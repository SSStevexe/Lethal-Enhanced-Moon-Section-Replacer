import json
from enum import Enum
import re

from Modules import UserActionGetter
from Modules.ConfigSyncer import ConfigSyncer
from Modules.Settings import Settings


def print_successful_update_message(target_moon, section, risk_level, moon_count_replaced, moon_count):
    if risk_level is not None:
        print("{:<25} {:<25} {:<40} {:<45}".format(target_moon, section, risk_level,
                                                   "{}/{}".format(moon_count_replaced, moon_count)))
    else:
        print("{:<25} {:<5}".format(target_moon, section))


class SectionReplacer:
    class MoonRisk(Enum):
        D_MINUS = "D-"
        D = "D"
        D_PLUS = "D+"
        C_MINUS = "C-"
        C = "C"
        C_PLUS = "C+"
        B_MINUS = "B-"
        B = "B"
        B_PLUS = "B+"
        A_MINUS = "A-"
        A = "A"
        A_PLUS = "A+"
        S_MINUS = "S-"
        S = "S"
        S_PLUS = "S+"
        S_PLUS_PLUS = "S++"
        UNKNOWN = "Unknown"
        P = "P"
        COMPANY = "Company"

    class Section(Enum):
        OUTSIDE = "outside"
        INSIDE = "inside"
        DAYTIME = "daytime"
        SCRAP = "scrap"
        ALL = "all"

    class MainFileSection(Enum):
        OUTSIDE = "outside_enemies"
        INSIDE = "inside_enemies"
        DAYTIME = "daytime_enemies"
        SCRAP = "loot_table"

    def __init__(self, json_data, json_directory_name):
        self._json_data = json_data
        self._json_directory_name = json_directory_name
        self._settings = Settings()

    def replacement(self):
        section_to_replace = self._get_file_to_replace_input()
        if section_to_replace == self.Section.SCRAP:
            self._update_scrap_rarities()
        else:
            self._update_moon_data_by_risk(self.Section(section_to_replace))

    def _update_scrap_rarities(self):
        print("{:<25} {:<25} {:<40} {:<45}\n".format("Moon", "Section", "Risk Level", "Moon Count Replaced/Total"))
        update_count = 1
        amount_of_moons = len(self._json_data["main"]["moons"]["moons"])
        for moon in self._json_data["main"]["moons"]["moons"]:
            moon_name = moon["key"]
            section_name = self.Section.SCRAP.name
            risk_level = self._get_moon_risk(moon)
            if risk_level == self.MoonRisk.COMPANY.value:
                continue
            moon["value"]["loot_table"] = self._json_data["scrap"]
            print("{:<25} {:<25} {:<40} {:<45}".format(moon_name, section_name, risk_level,
                                                       f"{update_count} / {amount_of_moons}"))
            update_count = update_count + 1
        with open("{}/main.json".format(self._json_directory_name), "w") as f:
            json.dump(self._json_data["main"], f, indent=4)
            f.close()

    def _get_file_to_replace_input(self) -> Section:
        user_choice = ""
        valid_choices = [section.lower() for section in self.Section.__members__]
        if self._settings.get_setting_value(Settings.ScriptBehavior.SettingName.IGNORE_OUTSIDE) is True:
            valid_choices.remove(self.Section.OUTSIDE.value)
        while user_choice not in valid_choices:
            user_choice = input("\nSelect which section of moons to replace by their associated risk: {}\n".format(
                valid_choices))
            if user_choice not in valid_choices:
                print("Invalid input. Please enter a valid section.\n")
        return self.Section[user_choice.upper()]

    def _update_moon_data_by_risk(self, section_to_update: Section):
        print("{:<25} {:<25} {:<40} {:<45}\n".format("Moon", "Section", "Risk Level", "Moon Count Replaced/Total"))
        sections_to_update = [self.Section.INSIDE, self.Section.OUTSIDE,
                              self.Section.INSIDE.DAYTIME] if section_to_update == self.Section.ALL else [
            section_to_update]
        if self._settings.get_setting_value(Settings.ScriptBehavior.SettingName.IGNORE_OUTSIDE) is True:
            sections_to_update.remove(self.Section.OUTSIDE)
        moon_count_replaced = 0
        moon_data = self._json_data["main"]["moons"]["moons"]
        moon_count = len(moon_data)
        for moon in moon_data:
            touched_moon = False
            moon_risk = self._get_moon_risk(moon)
            # If moon risk is company, skip the moon
            if moon_risk in [self.MoonRisk.COMPANY.value]:
                print("{:<25} {:<5}".format(moon["key"], "{} - Skipped ❌".format(moon_risk)))
                continue
            for section in sections_to_update:
                if not touched_moon:
                    touched_moon = True
                    moon_count_replaced += 1
                self._update_moon_section(moon["key"], moon_risk, section, moon_count_replaced, moon_count)
        print("main.json updated successfully. ✅")
        input("Press enter to exit...")
        exit(0)

    def _get_moon_risk(self, moon) -> MoonRisk:
        moon_name = moon["key"]
        moon_name = self._strip_to_alpha(moon_name)
        return self._json_data[ConfigSyncer.JsonFileName.EXTRA.value]["moons"][moon_name]["risk"]

    def _strip_to_alpha(self, input_string):
        return re.sub(r'[^a-zA-Z]', '', input_string)

    def _update_moon_section(self, moon_name, moon_risk, section, moon_count_replaced, moon_count):
        section_data = self._get_data_from_json_given_risk(moon_risk, section)
        self._set_new_moon_section_data(section, moon_name, section_data, moon_risk, moon_count_replaced,
                                        moon_count)

    def _get_data_from_json_given_risk(self, risk, json_file_name):
        json_data = self._json_data[json_file_name.value]
        risk_data = ""
        for data in json_data:
            if data["risk"] == risk:
                risk_data = data["data"]
                break
        return risk_data

    def _set_new_moon_section_data(self, section: Section, target_moon, replacement_data, risk_level,
                                   moon_count_replaced,
                                   moon_count):
        main_file = self._json_data["main"]
        moon_data = main_file["moons"]["moons"]
        with open("{}/main.json".format(self._json_directory_name), "w") as f:
            for moon in moon_data:
                if target_moon.lower() in moon["key"].lower():
                    moon["value"][self.MainFileSection[section.name].value] = replacement_data
                    main_file["moons"]["moons"] = moon_data
                    print_successful_update_message(target_moon, section.name, risk_level, moon_count_replaced,
                                                    moon_count)
                    # replace the main.json file with the new data
                    json.dump(main_file, f, indent=4)
            f.close()
