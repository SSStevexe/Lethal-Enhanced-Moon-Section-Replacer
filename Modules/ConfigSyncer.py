import json
import time
from Modules.Settings import Settings


class ConfigSyncer:
    def __init__(self):
        self._log_prefix = "ConfigSyncer: "
        self._json_file_directory_name = "Json Files"
        self._moon_names = []
        self._json_file_names = {
            "scrap": "scrap.json",
            "outside": "outside.json",
            "inside": "inside.json",
            "daytime": "daytime.json",
            "main": "main.json",
            "extra": "moon_extra_info.json",
            "options_by_risk": "options_by_risk.json"
        }
        self._json_data = {
            "scrap": {},
            "outside": {},
            "inside": {},
            "daytime": {},
            "main": {},
            "extra": {},
            "options_by_risk": {}
        }

        self._risk_levels = {
            "D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "S", "S+", "S++", "P", "SS", "Unknown",
            "Company"
        }

        self._settings_reader = Settings()
        self._load_files()
        self._check_all_json_do_not_contain_empty_rarity()
        self._update_moon_extra_info_data()
        self._remove_outdated_moon_extra_info_data()
        self._sync_monsters_available()
        self._update_scrap_data()
        self._validate_price_set_per_moon()

    def get_json_data(self, file_name):
        return self._json_data[file_name]

    def get_all_json_data(self):
        return self._json_data

    def get_json_directory_name(self):
        return self._json_file_directory_name

    def _load_files(self):
        self._log("Loading Json Data...\n")
        self._log("{:<20} {:<20}".format("File", "Loaded"))
        for key, value in self._json_file_names.items():
            time.sleep(0.5)
            self._json_data[key] = self._get_json_data(value)
        self._log("Json Data Loaded ✅\n")

    def _get_json_data(self, file):
        try:
            with open("{}/{}".format(self._json_file_directory_name, file), "r") as f:
                try:
                    data = json.load(f)
                    self._log("{:<20} {:<20}".format(file, "✅"))
                    return data
                except json.JSONDecodeError as e:
                    self._log("{:<20} {:<20}".format(file, "❌ - Invalid JSON. Check the file."))
                    self._log(e)
                    input("Press Enter to exit...")
                    exit(0)
                finally:
                    f.close()
        except FileNotFoundError as e:
            self._log("File: {} not found. Creating an empty file...".format(file))
            try:
                with open("{}/{}".format(self._json_file_directory_name, file), "w") as f:
                    json.dump({}, f, indent=4)
                    f.close()
                    input(
                        "Press Enter to acknowledge the file has been created and continue...This could break things.")
                    return {}
            except Exception as e:
                self._log("An error occurred while creating the file.")
                self._log(e)
                input("Press Enter to exit...")
                exit(0)

    def _update_moon_extra_info_data(self):
        self._log("Syncing moon data...\n")
        main_moon_names = self._get_moon_names_from_main()
        extra_info_moon_names = self._get_extra_info_moon_names()
        missing_moons = set(main_moon_names) - set(extra_info_moon_names)
        if len(missing_moons) > 0:
            self._log("Missing moons in moon_extra_info.json: {} - ❌\n".format(missing_moons))
            for moon_name in missing_moons:
                self._log("Adding ->{}<- to moon_extra_info.json\n".format(moon_name))
                self._json_data["extra"]["moons"][moon_name] = dict(risk="")
            self._write_to_file(self._json_data["extra"], "extra")
            self._log(
                "Make sure to update the risk levels for the new moons in {} before continuing.\n".format(
                    self._json_file_names["extra"]))
            input("Press Enter to continue...")
            exit(0)
        else:
            self._log("No missing moons in {}. ✅\n".format(self._json_file_names["extra"]))

    def _remove_outdated_moon_extra_info_data(self):
        main_moon_names = self._get_moon_names_from_main()
        extra_info_moon_names = self._get_extra_info_moon_names()
        outdated_moons = set(extra_info_moon_names) - set(main_moon_names)
        if len(outdated_moons) > 0:
            self._log("Outdated moons in moon_extra_info.json: {}\n".format(outdated_moons))
            for moon_name in outdated_moons:
                self._log("Removing ->{}<- from moon_extra_info.json\n".format(moon_name))
                del self._json_data["extra"]["moons"][moon_name]
                self._write_to_file(self._json_data["extra"])
                self._log(
                    "Make sure to update the risk levels for the new moons in {} before continuing.\n".format(
                        self._json_file_names["extra"]))
                input("Press Enter to continue...")
                exit(0)
        else:
            self._log("No outdated moons in {}. ✅\n".format(self._json_file_names["extra"]))

    def _write_to_file(self, data, section):
        with open(f"{self._json_file_directory_name}/{self._json_file_names[section]}", "w") as f:
            json.dump(data, f, indent=4)
            f.close()

    def _get_moon_names_from_main(self):
        moons = self._json_data["main"]["moons"]["moons"]
        moon_names = []
        for moon in moons:
            # only keep the alpha characters of moon names
            moon_names.append("".join(filter(str.isalpha, moon["key"])))
        return moon_names

    def _get_extra_info_moon_names(self):
        moons = self._json_data["extra"]["moons"]
        moon_names = []
        for key, value in moons.items():
            moon_names.append(key)
        return moon_names

    def _get_scrap_item_names_from_main(self):
        scraps = []
        for moon in self._json_data["main"]["moons"]["moons"]:
            for scrap in moon["value"]["loot_table"]:
                scraps.append(scrap["key"])
        return set(scraps)

    def _get_scrap_item_names_from_user(self):
        scraps = []
        for scrap in self._json_data["scrap"]:
            scraps.append(scrap["key"])
        return set(scraps)

    def _update_scrap_data(self):
        # Get scrap names from main.json
        self._log("Syncing {} and {}\n".format(self._json_file_names["main"], self._json_file_names["scrap"]))
        main_scrap_item_names = self._get_scrap_item_names_from_main()
        user_scrap_item_names = self._get_scrap_item_names_from_user()
        missing_scraps_in_user_file = set(main_scrap_item_names) - set(user_scrap_item_names)
        user_scraps_not_in_main_file = set(user_scrap_item_names) - set(main_scrap_item_names)
        if len(missing_scraps_in_user_file) > 0:
            self._add_missing_scraps_to_user_file(missing_scraps_in_user_file)
        if len(user_scraps_not_in_main_file) > 0:
            self._remove_outdated_scraps_from_user_file(user_scraps_not_in_main_file)
        self._log("Scrap data synced ✅\n")

    def _add_missing_scraps_to_user_file(self, missing_scraps):
        self._log("Missing scraps in scraps.json: {}\n".format(missing_scraps))
        for scrap in missing_scraps:
            self._log("Adding ->{}<- to scraps.json\n".format(scrap))
            self._json_data["scrap"].append(dict(key=scrap, value=dict(override=True, rarity="")))
            self._write_to_file(self._json_data["scrap"], "scrap")
        self._log("Make sure to update the rarity levels for the new scraps in {} before continuing.\n".format(
            self._json_file_names["scrap"]))
        input("Press Enter to continue...")
        exit(0)

    def _remove_outdated_scraps_from_user_file(self, outdated_scraps):
        self._log("Scraps in {} not in {}: {}\n".format(self._json_file_names["scrap"], self._json_file_names["main"],
                                                        outdated_scraps))
        self._json_data["scrap"] = [x for x in self._json_data["scrap"] if x["key"] not in outdated_scraps]
        self._write_to_file(self._json_data["scrap"], "scrap")
        self._log("Removed from scraps.json ✅\n")

    def _log(self, text):
        print("{} {}".format(self._log_prefix, text))

    def _validate_price_set_per_moon(self):
        missing_risks = []
        for risk in self._risk_levels:
            if self._get_price_to_visit_moon(risk) is None:
                missing_risks.append(risk)
        if len(missing_risks) > 0:
            self._add_missing_risks_to_options_by_risk(missing_risks)
        else:
            self._log("No missing risks in {}. ✅\n".format(self._json_file_names["options_by_risk"]))

    def _get_price_to_visit_moon(self, risk):
        for item in self._json_data["options_by_risk"]:
            if item["risk"] == risk:
                return item["options"]["price_to_travel"]
        return None

    def _add_missing_risks_to_options_by_risk(self, missing_risks):
        new_risk = {
            "risk": "",
            "options": {
                "price_to_travel": 0
            }
        }
        self._log("Missing risks in options_by_risk.json: {}\n".format(missing_risks))
        for risk in missing_risks:
            new_risk["risk"] = risk
            self._log("Adding ->{}<- to options_by_risk.json\n".format(risk))
            self._json_data["options_by_risk"].append(new_risk)
        self._write_to_file(self._json_data["options_by_risk"], "options_by_risk")
        self._log("Make sure to update the price set for the new risks in {} before continuing.\n".format(
            self._json_file_names["options_by_risk"]))
        input("Press Enter to continue...")
        exit(0)

    def _sync_monsters_available(self):
        self._log("Syncing monsters available in {} and adding if necessary to {} and {}\n".format(
            self._json_file_names["main"],
            self._json_file_names["inside"], self._json_file_names["outside"]))

        # Gather all monster names available in main.json
        main_monster_names: set = self._get_unique_monster_names_in_main()
        # Gather all monster names available in both outside.json and inside.json
        inside_outside_monster_names: set = self._get_unique_monster_names_in_outside_and_inside()
        # Compare the two sets and add missing monsters to outside.json and inside.json
        missing_monsters_inside_outside = main_monster_names - inside_outside_monster_names
        if len(missing_monsters_inside_outside) > 0:
            self._add_monsters_to_inside_and_outside_json(list(missing_monsters_inside_outside))
            return
        no_longer_used_monsters = inside_outside_monster_names - main_monster_names
        if len(no_longer_used_monsters) > 0:
            self._log("Monsters in {} and {} not in {}: {}\n".format(self._json_file_names["inside"],
                                                                     self._json_file_names["outside"],
                                                                     self._json_file_names["main"],
                                                                     no_longer_used_monsters))
            self._log("Removing monsters from {} and {}\n".format(self._json_file_names["inside"],
                                                                  self._json_file_names["outside"]))
            self._remove_monsters_from_inside_and_outside_json(list(no_longer_used_monsters))

    def _remove_monsters_from_inside_and_outside_json(self, no_longer_used_monsters: list):
        skip_outside = self._settings_reader.get_setting(Settings.Section.SCRIPT_BEHAVIOR,
                                                         Settings.ScriptBehavior.IGNORE_OUTSIDE)
        for monster in no_longer_used_monsters:
            self._log("Removing ->{}<- from outside.json and inside.json\n".format(monster))
            for risk_entry_inside, risk_entry_outside in zip(self._json_data["outside"], self._json_data["inside"]):
                risk_entry_inside["data"] = [x for x in risk_entry_inside["data"] if x["key"] != monster]
                if not skip_outside:
                    risk_entry_outside["data"] = [x for x in risk_entry_outside["data"] if x["key"] != monster]
        if not skip_outside:
            self._write_to_file(self._json_data["outside"], "outside")
        self._write_to_file(self._json_data["inside"], "inside")
        if skip_outside:
            self._log("Not modifying outside.json as per settings.")
        self._log(
            "Monsters removed from {} and {}".format(self._json_file_names["inside"], self._json_file_names["outside"]))

    def _get_unique_monster_names_in_main(self) -> set:
        unique_monster_names = set()
        for moon in self._json_data["main"]["moons"]["moons"]:
            moon_content = moon['value']
            combined_monsters = moon_content['outside_enemies'] + moon_content['inside_enemies']
            combined_monster_names = list()
            for monster in combined_monsters:
                combined_monster_names.append(monster['key'])
            unique_monster_names.update(combined_monster_names)
            self._log("Unique monsters detected in main.json: {}.".format(unique_monster_names.__len__()))
            return unique_monster_names

    def _get_unique_monster_names_in_outside_and_inside(self) -> set:
        unique_monster_names = set()
        inside_outside_combined = self._json_data['inside'] + self._json_data['outside']
        for item in inside_outside_combined:
            for data in item['data']:
                unique_monster_names.add(data['key'])
        self._log(
            "Unique monsters detected in outside.json and inside.json: {}.".format(unique_monster_names.__len__()))
        return unique_monster_names

    def _add_monsters_to_inside_and_outside_json(self, missing_monsters: list):
        skip_outside = self._settings_reader.get_setting(Settings.Section.SCRIPT_BEHAVIOR, Settings.ScriptBehavior.IGNORE_OUTSIDE)
        self._log("Missing monsters in outside.json and inside.json: {}\n".format(missing_monsters))
        for monster in missing_monsters:
            if skip_outside:
                self._log("Adding ->{}<- to inside.json\n".format(monster))
            else:
                self._log("Adding ->{}<- to outside.json and inside.json\n".format(monster))
            for risk_entry_outside, risk_entry_inside in zip(self._json_data["outside"], self._json_data["inside"]):
                risk_entry_inside["data"].append({"key": monster, "value": {"override": True, "rarity": ""}})
                if not skip_outside:
                    risk_entry_outside["data"].append({"key": monster, "value": {"override": True, "rarity": ""}})
        if not skip_outside:
            self._write_to_file(self._json_data["outside"], "outside")
            self._log("Not modifying outside.json as per settings.")
        self._write_to_file(self._json_data["inside"], "inside")
        if skip_outside:
            self._log("Make sure to update the rarity levels for the new monsters in {} before continuing.\n".format(
                self._json_file_names["inside"]))
        else:
            self._log(
                "Make sure to update the rarity levels for the new monsters in {} and {} before continuing.\n".format(
                    self._json_file_names["outside"], self._json_file_names["inside"]))
        input("Press Enter to continue...")
        exit(0)

    def _check_all_json_do_not_contain_empty_rarity(self):
        skip_outside = self._settings_reader.get_setting(Settings.Section.SCRIPT_BEHAVIOR,
                                                         Settings.ScriptBehavior.IGNORE_OUTSIDE)

        def check_empty_rarity(items, file_name):
            for item in items:
                if item["value"]["rarity"] == "":
                    self._log(f"{file_name} contains empty rarity values. First triggered entry: {item['key']} - ❌")
                    input("Press Enter to exit...")
                    exit(0)

        self._log("Checking all json files do not contain empty rarity values...\n")

        for moon_name, risk in self._json_data["extra"]["moons"].items():
            if risk["risk"] == "":
                self._log(f"moon_extra_info.json contains empty rarity values. First triggered entry: {moon_name} - ❌")
                input("Press Enter to exit...")
                exit(0)

        for option in self._json_data["options_by_risk"]:
            if option["options"]["price_to_travel"] == "":
                self._log(
                    f"options_by_risk.json contains empty rarity values. First triggered entry: {option['risk']} - ❌")
                input("Press Enter to exit...")
                exit(0)

        check_empty_rarity(self._json_data["scrap"], "Scrap.json")

        json_file_tokens = ["outside", "inside", "daytime"]

        if skip_outside is True:
            json_file_tokens.remove("outside")
            self._log("Ignoring outside.json as per settings.")

        for token in json_file_tokens:
            for json_file in self._json_data[token]:
                check_empty_rarity(json_file["data"], f"{token.capitalize()}.json")

        self._log("All json files do not contain empty rarity values. ✅\n")

