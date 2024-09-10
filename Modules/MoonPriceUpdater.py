import json
import time

from Modules.ConfigSyncer import ConfigSyncer


class MoonPriceUpdater:

    def __init__(self, json_files: dict):
        self._log_prefix = "MoonPriceUpdater: "
        self._json_file_directory_name = "Json Files"
        self._json_files = json_files

    def update_moon_prices(self):
        self._log("Updating moon prices...")
        self._log("{:<20} {:<20} {:<20}".format("Moon", "Risk", "Price"))
        for moon in self._json_files["main"]["moons"]["moons"]:
            risk = self._get_moon_risk_by_moon_name(moon["key"])
            update_price = self._get_price_by_risk(risk)
            self._log("{:<20} {:<20} {:<20}".format(moon["key"], risk, update_price))
            moon["value"]["price"] = update_price
        self._log("Moon prices updated ✅")
        self._write_json_to_disk()

    def _log(self, msg):
        print(self._log_prefix + msg)

    def _get_price_by_risk(self, risk):
        for risk_item in self._json_files["options_by_risk"]:
            if risk_item["risk"] == risk:
                return risk_item["options"]["price_to_travel"]
        return None

    def _get_moon_risk_by_moon_name(self, moon_name):
        moon_name = ''.join(e for e in moon_name if e.isalpha())
        data = self._json_files[ConfigSyncer.JsonFileName.EXTRA.value]["moons"].get(moon_name)
        if data is not None:
            return data["risk"]
        return None

    def _write_json_to_disk(self):
        with open("{}/{}".format(self._json_file_directory_name, "main.json"), "w") as f:
            json.dump(self._json_files[ConfigSyncer.JsonFileName.MAIN.value], f, indent=4)
        self._log("Json Data Written to main.json! ✅\n")