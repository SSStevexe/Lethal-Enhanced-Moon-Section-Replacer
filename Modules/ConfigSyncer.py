import json
import time


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
            "extra": "moon_extra_info.json"
        }
        self._json_data = {
            "scrap": {},
            "outside": {},
            "inside": {},
            "daytime": {},
            "main": {},
            "extra": {}
        }
        self._load_files()
        self._update_moon_extra_info_data()
        self._remove_outdated_moon_extra_info_data()
        self._update_scrap_data()

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
            self._log("Missing moons in moon_extra_info.json: {}\n".format(missing_moons))
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
            self._json_data["scrap"].append(dict(key=scrap, value=dict(override=True, rarity=0)))
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
        print("{}: {}".format(self._log_prefix, text))
