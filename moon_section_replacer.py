import json
import time
import re
from Classes.ConfigSyncer import ConfigSyncer
from Classes.UserActionGetter import UserAction

json_files = {
}

main_file_scraps = []
main_file_monsters = []
user_file_scraps = []
user_file_monsters = []
main_file_scraps_not_in_user = set()
main_file_monsters_not_in_user = set()
user_file_scraps_not_in_main = set()
user_file_monsters_not_in_main = set()
# moon extra info
moon_extra_info_file = "moon_extra_info.json"
moon_risk_levels = {"D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "S-", "S", "S+", "S++",
                    "Unknown", "P", "Company"}
# multi moon replacement options
multi_moon_replacement_options = ["all", "risk", "manual"]


# Moons available
moon_data = {}
# Valid moon names
moon_names = list()
# Data from the moon extra info file
moon_extra_info_data = {}





def get_moon_section_data(section, target_moon=""):
    # find the moon section data
    for moon in moon_data:
        if target_moon.lower() in moon["key"].lower():
            section_data = moon["value"][section]
            return section_data


def set_new_moon_section_data(section, target_moon, replacement_data, risk_level, moon_count_replaced, moon_count):
    main_file = json_files["main"]
    # find the moon section data
    with open("{}/main.json".format(json_file_directory), "w") as f:
        for moon in moon_data:
            if target_moon.lower() in moon["key"].lower():
                moon["value"][section] = replacement_data
                main_file["moons"]["moons"] = moon_data
                print_successful_update_message(target_moon, section, risk_level, moon_count_replaced, moon_count)
        # replace the main.json file with the new data
        json.dump(main_file, f, indent=4)
        f.close()


def print_successful_update_message(target_moon, section, risk_level, moon_count_replaced, moon_count):
    if risk_level is not None:
        print("{:<25} {:<25} {:<40} {:<45}".format(target_moon, section, risk_level,
                                                   "{}/{}".format(moon_count_replaced, moon_count)))
    else:
        print("{:<25} {:<5}".format(target_moon, section))


def section_to_json_name(section):
    for key, value in section_words.items():
        if value == section:
            return key
    return ""


def validate_section_name(section):
    global section_words
    if section in section_words.keys():
        return True
    else:
        return False


def validate_moon_name(name):
    global moon_names
    # Convert the user's input to lower case
    lower_name = name.lower()
    # Convert the moon names in the list to lower case before comparing
    if lower_name in (moon.lower() for moon in moon_names):
        return True
    else:
        return False


def print_list_of_moon_names():
    print("List of available moon names (alphabetical):\n")
    print("{:<25} {:<5}\n".format("Moon", "Risk Level"))
    for name in moon_names:
        risk_level = moon_extra_info_data["moons"][name]['risk']
        if risk_level == "":
            print("Risk level not set for moon ->{}<-. Please update in {} before continuing.".format(name,
                                                                                                      moon_extra_info_file))
            input("Press Enter to exit...")
            exit(0)
        if validate_moon_risk_level(risk_level) is False:
            print("Invalid risk level detected for moon ->{}<- Risk: {}. Please update in {} before continuing.".format(
                name, risk_level, moon_extra_info_file))
            input("Press Enter to exit...")
            exit(0)
        print("{:<25} {:<5}".format(name, risk_level))
    print("\n")


def process_multi_moon_replacement_risk(multiple_moon_replacement_list):
    risk_level = get_risk_level_from_user()
    for moon in moon_extra_info_data["moons"]:
        if moon_extra_info_data["moons"][moon]["risk"] == risk_level:
            multiple_moon_replacement_list.append(moon)


def get_risk_level_from_user():
    moon_risk_level_to_target = input("Enter the risk level you would like to target: {}".format(moon_risk_levels))
    while not validate_moon_risk_level(moon_risk_level_to_target):
        print("Invalid risk level. Please enter a valid risk level.\n")
        moon_risk_level_to_target = input("Enter the risk level you would like to target: {}".format(moon_risk_levels))
    return moon_risk_level_to_target


def validate_moon_risk_level(level):
    global moon_risk_levels
    if level in moon_risk_levels:
        return True
    else:
        return False


def process_multi_moon_replacement_manual(multiple_moon_replacement_list):
    print("Enter the names of the moons you want to replace data for one at a time.\n")
    moon_name = input("Moon to include in replacement (type \"done!\" to end): ")
    while moon_name != "done!":
        if not validate_moon_name(moon_name):
            print("Invalid moon name.\n")
        else:
            multiple_moon_replacement_list.append(moon_name)
        moon_name = input("Moon to include in replacement (type \"done!\" to end): ")


def get_multi_moon_replacement_type_from_user():
    multi_moon_replacement_type = input(
        "How would you like to replace the data for multiple moons? {}\n".format(multi_moon_replacement_options))
    while not validate_multi_moon_replacement_type(multi_moon_replacement_type):
        print("Invalid multi moon replacement type. Please enter a valid type.\n")
        multi_moon_replacement_type = input(
            "How would you like to replace the data for multiple moons? {}\n".format(multi_moon_replacement_options))
    return multi_moon_replacement_type


def validate_multi_moon_replacement_type(type):
    global multi_moon_replacement_options
    if type in multi_moon_replacement_options:
        return True
    else:
        return False


def get_valid_section_name_from_user():
    section_name = input(
        "Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): ")

    while not validate_section_name(section_name):
        print("Invalid section name. Please enter a valid section name.\n")
        section_name = input(
            "Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): ")
    return section_name


def get_valid_moon_name_from_user():
    moon_name = input("Enter the name of the moon you want to replace data for: ")
    while not validate_moon_name(moon_name):
        print("Invalid moon name. Please enter a valid moon name.\n")
        moon_name = input("Enter the name of the moon you want to replace data for: ")
    return moon_name





def get_file_to_replace_input():
    valid_file_names = ["outside", "inside", "daytime", "all", "skip"]
    user_choice = ""
    while user_choice not in valid_file_names:
        user_choice = input(
            "\nSelect which section of moons to replace by their associated risk: {}".format(valid_file_names))
    return user_choice


def get_user_input_for_scrap_update():
    user_input = input("Would you like to update the scrap section for all moons? (y/n): ")
    while user_input.lower() not in ["y", "n"]:
        print("Invalid input. Please enter a valid input.\n")
        user_input = input("Would you like to update the scrap section for all moons? (y/n): ")
    return user_input


def get_moon_risk(moon):
    moon_name = moon["key"]
    return moon_extra_info_data["moons"][strip_to_alpha(moon_name)]["risk"]


def update_moon_section(moon_name, moon_risk, section, moon_count_replaced, moon_count):
    section_data = get_data_from_json_given_risk(moon_risk, section)
    set_new_moon_section_data(section_words[section], moon_name, section_data, moon_risk, moon_count_replaced,
                              moon_count)


def update_moon_data_by_risk(section_to_update):
    if section_to_update == "skip":
        return
    print("{:<25} {:<25} {:<40} {:<45}\n".format("Moon", "Section", "Risk Level", "Moon Count Replaced/Total"))
    sections_to_update = ["inside", "outside", "daytime"] if section_to_update == "all" else [section_to_update]
    moon_count_replaced = 0
    moon_count = len(moon_data)
    for moon in moon_data:
        touched_moon = False
        moon_risk = get_moon_risk(moon)
        # If moon risk is company, skip the moon
        if moon_risk == "Company":
            print("{:<25} {:<5}".format(moon["key"], "Company - Skipped ❌"))
            continue
        for section in sections_to_update:
            if not touched_moon:
                touched_moon = True
                moon_count_replaced += 1
            update_moon_section(moon["key"], moon_risk, section, moon_count_replaced, moon_count)


def get_data_from_json_given_risk(risk, json_file):
    json_data = json_files[json_file]
    risk_data = ""
    for data in json_data:
        if data["risk"] == risk:
            risk_data = data["data"]
            break
    return risk_data


def strip_to_alpha(input_string):
    return re.sub(r'[^a-zA-Z]', '', input_string)


def update_scrap_section_for_moons():
    target_section = "scrap"
    count = len(moon_data)
    update_count = 1
    print("{:<25} {:<25} {:<40} {:<45}\n".format("Moon", "Section", "Risk Level", "Moon Count Replaced/Total"))
    for moon in moon_data:
        set_new_moon_section_data(section_words[target_section], moon["key"], json_files[target_section],
                                  get_moon_risk(moon), update_count, count)
        update_count += 1


def extract_scrap_data_from_main_file(main_file):
    global main_file_scraps
    for moon in main_file["moons"]["moons"]:
        for scrap in moon["value"]["loot_table"]:
            main_file_scraps.add(scrap["key"])
    main_file_scraps = sorted(main_file_scraps)


def extract_data_from_section(section):
    return sorted(set(item["key"] for item in json_files[section]))


def extract_user_file_data():
    global user_file_monsters
    global user_file_scraps

    print("Extracting data from user files...\n")
    user_file_scraps = extract_data_from_section("scrap")
    user_file_monsters = sorted(list(
        monster_name["key"] for section in ["inside", "outside", "daytime"] for monster in json_files[section] for
        monster_name in monster["data"]))


def update_scrap_json(list_of_missing_scraps):
    entries = json_files["scrap"]
    for scrap in list_of_missing_scraps:
        entries.append({"key": scrap, "value": {
            "override": True,
            "rarity": 0,
        }})
        print("Added missing scrap ->{}<- to scrap.json!".format(scrap))
    with open("{}/{}".format(json_file_directory, json_file_names["scrap"]), "w") as f:
        json.dump(entries, f, indent=4)
        f.close()


def update_monster_jsons(list_of_missing_monsters):
    risk_entries = {}
    for section in ["inside", "outside", "daytime"]:
        risk_entries = json_files[section]
        for monster in list_of_missing_monsters:
            for risk_entry in risk_entries:
                risk_entry["data"].append({"key": monster, "value": {
                    "override": True,
                    "rarity": 0,
                }})
            print("Added missing monster ->{}<- to {}.json!".format(monster, section))
    with open("{}/{}".format(json_file_directory, json_file_names[section]), "w") as f:
        json.dump(risk_entries, f, indent=4)
        f.close()


# main function
if __name__ == "__main__":
    config_syncer = ConfigSyncer()
    user_action = UserAction()
    user_action.get_user_action()

    user_input_section_replacement = get_file_to_replace_input()
    update_moon_data_by_risk(user_input_section_replacement)
    user_input_update_scrap = get_user_input_for_scrap_update()

    if user_input_update_scrap.lower() == "y":
        update_scrap_section_for_moons()

    print("Replacement process complete!\n")
    input("Press Enter to exit...")
