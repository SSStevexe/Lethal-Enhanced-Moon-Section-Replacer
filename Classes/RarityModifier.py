class RarityModifier:
    def __init__(self, json_data: dict):
        self.json_data = json_data
        self.rarity_modifiers = self.json_data["rarity_modifiers"]
