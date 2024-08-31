import json
from enum import Enum

from Modules import UserActionGetter


class RarityModifier:
    class Action(Enum):
        MODIFY_RARITIES = 1
        REPLACE_SECTION = 2
        EXIT_SCRIPT = 3

    class MonsterLocation(Enum):
        INSIDE = "inside_enemies"
        DAYTIME = "daytime_enemies"
        OUTSIDE = "outside_enemies"

    def __init__(self, json_data: dict, json_directory_name: str):
        self._json_data = json_data
        self._json_data_directory_name = json_directory_name

    def modify_rarities(self):
        user_choice = UserActionGetter.get_scrap_or_monster_replacement_action()
        if user_choice == UserActionGetter.ScrapOrMonster.SCRAP.value:
            self._replace_moon_scrap_rarities()
        elif user_choice == UserActionGetter.ScrapOrMonster.MONSTER.value:
            self._replace_moon_monster_rarities()

    def _replace_moon_monster_rarities(self):
        user_choice = UserActionGetter.get_set_rarities_or_change_by()
        moon_data = self._get_moons_from_main_file()
        moon_count = len(moon_data)

        if user_choice == UserActionGetter.ChangeRarity.SET.value:
            set_rarity_to = UserActionGetter.get_amount_to_set_rarity_to()
            print("\nSetting monster rarities in {} moons to {}... Please wait...".format(moon_count,
                                                                                          set_rarity_to))
            self._set_monster_rarities_to(set_rarity_to, moon_data)
        elif user_choice == UserActionGetter.ChangeRarity.RAISE.value:
            change_rarity_by = UserActionGetter.get_amount_to_raise_rarity_by()
            print("\nRaising monster rarities in {} moons by {}... Please wait...".format(moon_count,
                                                                                          change_rarity_by))
            self._raise_monster_rarities_by(change_rarity_by, moon_data)

    def _set_monster_rarities_to(self, rarity: int, moon_data: dict):
        for location in self.MonsterLocation:
            for moon in moon_data:
                enemies = moon["value"][location.value]
                for enemy in enemies:
                    enemy["value"]["rarity"] = rarity
        self._update_main_file()

    def _raise_monster_rarities_by(self, amount: int, moon_data: dict):
        for location in self.MonsterLocation:
            for moon in moon_data:
                enemies = moon["value"][location.value]
                for enemy in enemies:
                    enemy["value"]["rarity"] += amount
        self._update_main_file()

    def _replace_moon_scrap_rarities(self):
        user_choice = UserActionGetter.get_set_rarities_or_change_by()
        moon_data = self._get_moons_from_main_file()

        scrap_count = len(self._json_data["scrap"])
        moon_count = len(moon_data)
        if user_choice == UserActionGetter.ChangeRarity.SET.value:
            set_rarity_to = UserActionGetter.get_amount_to_set_rarity_to()
            print("\nSetting {} scrap rarities in {} moons to {}... Please wait...".format(scrap_count, moon_count,
                                                                                           set_rarity_to))
            self._set_moon_scrap_rarities_to(set_rarity_to, moon_data)
        elif user_choice == UserActionGetter.ChangeRarity.RAISE.value:
            raise_rarity_by = UserActionGetter.get_amount_to_raise_rarity_by()
            print("\nRaising scrap rarities in {} moons by {}... Please wait...".format(moon_count, raise_rarity_by))
            self._raise_moon_scrap_rarities_by(raise_rarity_by)

    def _set_moon_scrap_rarities_to(self, rarity: int, moon_data: dict):
        for moon in moon_data:
            moon_loot_table = moon["value"]["loot_table"]
            for item in moon_loot_table:
                item["value"]["rarity"] = rarity
        self._update_main_file()

    def _raise_moon_scrap_rarities_by(self, amount: int):
        moon_data = self._get_moons_from_main_file()
        for moon in moon_data:
            moon_loot_table = moon["value"]["loot_table"]
            for item in moon_loot_table:
                item["value"]["rarity"] += amount
        self._update_main_file()

    def _get_moons_from_main_file(self):
        return self._json_data["main"]["moons"]["moons"]

    def _update_main_file(self):
        with open("{}/main.json".format(self._json_data_directory_name), "w") as f:
            json.dump(self._json_data["main"], f, indent=4)
            f.close()
        print("main.json updated successfully. ✅")
        input("Press enter to exit...")
        exit(0)
