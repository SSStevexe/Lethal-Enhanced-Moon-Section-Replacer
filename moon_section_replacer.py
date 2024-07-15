from Modules.ConfigSyncer import ConfigSyncer
from Modules.MoonPriceUpdater import MoonPriceUpdater
from Modules.RarityModifier import RarityModifier
from Modules.SectionReplacer import SectionReplacer
import Modules.UserActionGetter as UserActionGetter

# main function
if __name__ == "__main__":
    config_syncer = ConfigSyncer()
    section_replacer = SectionReplacer(config_syncer.get_all_json_data(), config_syncer.get_json_directory_name())
    rarity_modifier = RarityModifier(config_syncer.get_all_json_data(), config_syncer.get_json_directory_name())
    moon_price_updater = MoonPriceUpdater(config_syncer.get_all_json_data())

    # Get user input for action:
    user_choice: int = UserActionGetter.get_user_action()

    # Switch case for user choice
    if user_choice == UserActionGetter.MainActions.REPLACE_SECTION.value:
        section_replacer.replacement()
    elif user_choice == UserActionGetter.MainActions.MODIFY_RARITIES.value:
        rarity_modifier.modify_rarities()
    elif user_choice == UserActionGetter.MainActions.MOON_PRICE_UPDATE.value:
        moon_price_updater.update_moon_prices()
