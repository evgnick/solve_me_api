from encodings.punycode import selective_find

from src.enums.user_enams import Status
from src.generators.player_localization import PlayerLocalization


class Player:

    def __init__(self):
        self.result = {}

        self.reset()

    def set_status(self, status=Status.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar="https://google.com"):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.result["localize"] = {
            "en": PlayerLocalization("en_US").build(),
            "ru": PlayerLocalization("ru_RU").build()
        }
        return self

    def update_inner_value(self, key, value):
        self.result[key] = value
        return self

    def build(self):
        return self.result
