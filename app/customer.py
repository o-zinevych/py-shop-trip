# import json
# MIGHT INCLUDE THIS INSIDE MAIN
#
# with open("config.json", "r") as config_file:
#     data = json.load(config_file)
#     customer_data = data["customers"]
from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"
