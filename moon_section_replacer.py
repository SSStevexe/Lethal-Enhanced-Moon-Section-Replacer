import json
import time
import re

section_words = {
    "scrap": "loot_table",
    "outside": "outside_enemies",
    "inside": "inside_enemies",
    "daytime": "daytime_enemies"
}

json_file_names = {
    "scrap": "scrap.json",
    "outside": "outside.json",
    "inside": "inside.json",
    "daytime": "daytime.json",
    "main": "main.json"
}

json_files = {
}

# moon extra info
moon_extra_info_file = "moon_extra_info.json"
moon_risk_levels = ["D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "S-", "S", "S+", "S++",
                    "Unknown", "P", "Company"]
# multi moon replacement options
multi_moon_replacement_options = ["all", "risk", "manual"]

json_file_directory = "Json Files"

# Moons available
moon_data = {}
# Valid moon names
moon_names = list()
# Data from the moon extra info file
moon_extra_info_data = {}


def get_json_data(file):
    try:
        with open("{}/{}".format(json_file_directory, file), "r") as f:
            try:
                data = json.load(f)
                print("Loaded data from ->{}<- successfully! ✅\n".format(file))
                return data
            except json.JSONDecodeError as e:
                print("Invalid Json file. Please check the file and try again.")
                print(e)
                input("Press Enter to exit...")
                exit(0)
            finally:
                f.close()
    except FileNotFoundError as e:
        print("File: {} not found. Creating an empty file...".format(file))
        try:
            with open("{}/{}".format(json_file_directory, file), "w") as f:
                json.dump({}, f, indent=4)
                f.close()
                input("Press Enter to acknowledge the file has been created and continue...This could break things.")
                return {}
        except Exception as e:
            print("An error occurred while creating the file.")
            print(e)
            input("Press Enter to exit...")
            exit(0)


def set_moon_data(data):
    global moon_data
    if data is not None:
        # if there is a key named "moons" in the main file
        try:
            if "moons" in data:
                # set the data to global map
                moon_data = data["moons"]["moons"]
                set_valid_moon_names(moon_data)
            else:
                print("No moons found in main file. This is a required field.")
                input("Press Enter to exit...")
                exit(0)
        except KeyError as e:
            print("No moons found in main file. This is a required field.")
            print(e)
            input("Press Enter to exit...")
            exit(0)
    else:
        print("No data found in main file. Please check the file and try again.")
        input("Press Enter to exit...")
        exit(0)


def set_valid_moon_names(moons):
    global moon_names
    for moon in moons:
        # Strip the key which contains the name of the moon of all numbers and only collect alpha characters
        moon_names.append(''.join(filter(str.isalpha, moon["key"])))
    moon_names.sort()


def get_moon_section_data(section, target_moon=""):
    # find the moon section data
    for moon in moon_data:
        if target_moon.lower() in moon["key"].lower():
            section_data = moon["value"][section]
            return section_data


def set_new_moon_section_data(section, target_moon, replacement_data):
    main_file = json_files["main"]
    # find the moon section data
    for moon in moon_data:
        if target_moon.lower() in moon["key"].lower():
            moon["value"][section] = replacement_data
            main_file["moons"]["moons"] = moon_data
            # replace the main.json file with the new data
            with open("{}/main.json".format(json_file_directory), "w") as f:
                json.dump(main_file, f, indent=4)
                f.close()
                print("Updated data for moon ->{}<- in section ->{}<- successfully! ✅\n".format(target_moon, section))
                return


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


def update_moon_extra_info_data():
    global moon_extra_info_data
    moon_extra_info_data = get_json_data(moon_extra_info_file)
    new_moon_detected = False
    if not moon_extra_info_data:
        moon_extra_info_data["moons"] = {}
    for moon_name in moon_names:
        # create a key in the data file
        if moon_name not in moon_extra_info_data["moons"]:
            print("Detected new moon! ->{}<- added to moon_extra_info.json!\n".format(moon_name))
            new_moon_detected = True
            moon_extra_info_data["moons"][moon_name] = dict(risk="")
    with open("{}/{}".format(json_file_directory, moon_extra_info_file), "w") as f:
        json.dump(moon_extra_info_data, f, indent=4)
        f.close()
    if not new_moon_detected:
        print("No new moons detected in main.json. Moon extra info data in {} is up to date! ✅\n".format(
            moon_extra_info_file))
    else:
        print("Make sure to update the risk levels for the new moons in {} before continuing.\n".format(
            moon_extra_info_file))
        input("Press Enter to continue...")
        exit(0)


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


def load_json_files():
    for key, value in json_file_names.items():
        time.sleep(0.5)
        json_files[key] = get_json_data(value)


def get_moon_risk(moon):
    moon_name = moon["key"]
    return moon_extra_info_data["moons"][strip_to_alpha(moon_name)]["risk"]


def update_moon_section(moon_name, moon_risk, section):
    section_data = get_data_from_json_given_risk(moon_risk, section)
    set_new_moon_section_data(section_words[section], moon_name, section_data)


def update_moon_data_by_risk(section_to_update):
    if section_to_update == "skip":
        return
    sections_to_update = ["inside", "outside", "daytime"] if section_to_update == "all" else [section_to_update]
    for moon in moon_data:
        moon_risk = get_moon_risk(moon)
        for section in sections_to_update:
            update_moon_section(moon["key"], moon_risk, section)


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
    for moon in moon_data:
        set_new_moon_section_data(section_words[target_section], moon["key"], json_files[target_section])


# main function
if __name__ == "__main__":
    print("Loading Json Data...\n")
    load_json_files()
    set_moon_data(json_files["main"])
    update_moon_extra_info_data()
    print_list_of_moon_names()

    user_input_section_replacement = get_file_to_replace_input()
    update_moon_data_by_risk(user_input_section_replacement)

    user_input_update_scrap = get_user_input_for_scrap_update()

    if user_input_update_scrap.lower() == "y":
        update_scrap_section_for_moons()

    print("Replacement process complete!\n")
    input("Press Enter to exit...")
