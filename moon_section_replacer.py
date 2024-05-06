import json
import time

section_words = {
    "scrap": "loot_table",
    "outside": "outside_enemies",
    "inside": "inside_enemies",
    "daytime": "daytime_enemies"
}

# moon extra info
moon_extra_info_file = "moon_extra_info.json"
moon_risk_levels = ["D-", "D", "D+", "C-", "C", "C+", "B-", "B", "B+", "A-", "A", "A+", "S-", "S", "S+", "S++",
                    "Unknown", "P", "Wesley"]
# multi moon replacement options
multi_moon_replacement_options = ["all", "risk", "manual"]

json_file_directory = "Json Files"

# JSON dict
main_file = {}
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
                return data
            except json.JSONDecodeError as e:
                print("Invalid Json file. Please check the file and try again.")
                print(e)
                input("Press Enter to exit...")
                exit(0)
            finally:
                f.close()
    except FileNotFoundError as e:
        print("File not found. Creating an empty file...")
        try:
            with open("{}/{}".format(json_file_directory, file), "w") as f:
                json.dump({}, f, indent=4)
                f.close()
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
    # find the moon section data
    for moon in moon_data:
        if target_moon.lower() in moon["key"].lower():
            moon["value"][section] = replacement_data
            main_file["moons"]["moons"] = moon_data
            # replace the main.json file with the new data
            with open("{}/main.json".format(json_file_directory), "w") as f:
                json.dump(main_file, f, indent=4)
                f.close()
            print("Section ->{}<- for moon ->{}<- has been replaced successfully with data from ->{}.json<-\n".format(
                section, target_moon, section_to_json_name(section)))
            return
    print()


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
    time.sleep(2)
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


def get_main_file():
    global main_file
    # look for main file in current directory
    try:
        main_file = get_json_data("main.json")
    except FileNotFoundError as e:
        print("Main file not found. Make sure main.json is in the same directory as this script.")
        print(e)
        input("Press Enter to exit...")
        exit(0)


def multiple_moons_replacement():
    multiple_moon_replacement_list = list()
    multi_moon_replacement_type = get_multi_moon_replacement_type_from_user()
    if multi_moon_replacement_type == "all":
        multiple_moon_replacement_list = moon_names
    elif multi_moon_replacement_type == "risk":
        process_multi_moon_replacement_risk(multiple_moon_replacement_list)
    elif multi_moon_replacement_type == "manual":
        process_multi_moon_replacement_manual(multiple_moon_replacement_list)

    print("\nMoons you have requested to replace data for: {}\n".format(multiple_moon_replacement_list))
    section_name = get_valid_section_name_from_user()
    for moon in multiple_moon_replacement_list:
        replacement_data = get_json_data("{}.json".format(section_name))
        set_new_moon_section_data(section_words[section_name], moon, replacement_data)


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


def single_moon_replacement():
    target_moon = get_valid_moon_name_from_user()
    section_name = get_valid_section_name_from_user()
    replacement_data = get_json_data("{}.json".format(section_name))
    set_new_moon_section_data(section_words[section_name], target_moon, replacement_data)


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
        print("No new moons detected. Moon extra info data in {} is up to date!\n".format(moon_extra_info_file))
    else:
        print("Make sure to update the risk levels for the new moons in {} before continuing.\n".format( moon_extra_info_file))
        input("Press Enter to continue...")
        exit(0)


# main function
if __name__ == "__main__":
    get_main_file()
    set_moon_data(main_file)
    update_moon_extra_info_data()
    print_list_of_moon_names()

    multiple_moon_inquery = input("Did you want to replace data for multiple moons? (y/n): ")

    if "y" in multiple_moon_inquery.lower():
        multiple_moons_replacement()
    else:
        single_moon_replacement()

    print("Replacement process complete!\n")
    input("Press Enter to exit...")
