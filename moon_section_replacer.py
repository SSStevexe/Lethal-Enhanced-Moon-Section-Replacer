import json
import time

section_words = {
    "scrap": "loot_table",
    "outside": "outside_enemies",
    "inside": "inside_enemies",
    "daytime": "daytime_enemies"
}

json_file_directory = "Json Files"

# JSON dict
main_file = {}
# Moons available
moon_data = {}
# Valid moon names
moon_names = list()


def get_json_data(file):
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
            with open("Json Files/main.json", "w") as f:
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
    moon_names.sort()
    print("List of available moon names (alphabetical):\n")
    time.sleep(2)
    for name in moon_names:
        # have some space from the left
        print(" " * 5 + name)
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


# main function
if __name__ == "__main__":
    get_main_file()
    set_moon_data(main_file)
    print_list_of_moon_names()
    target_moon = input("Enter the name of the moon you want to replace data for: ")

    while not validate_moon_name(target_moon):
        print("Invalid moon name. Please enter a valid moon name.\n")
        target_moon = input("Enter the name of the moon you want to replace data for: ")

    print("Valid moon name entered. Now targeting moon: " + target_moon + "\n")

    section_name = input(
        "Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): ")

    while not validate_section_name(section_name):
        print("Invalid section name. Please enter a valid section name.\n")
        section_name = input(
            "Enter the name of the section you want to replace data for (scrap, outside, inside, daytime): ")

    section_data = get_moon_section_data(section_words[section_name], target_moon)
    replacement_data = get_json_data("{}.json".format(section_name))
    set_new_moon_section_data(section_words[section_name], target_moon, replacement_data)
    input("Press Enter to exit...")
