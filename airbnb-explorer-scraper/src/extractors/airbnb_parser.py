thonimport requests
from datetime import datetime

class AirbnbParser:
    def __init__(self, settings):
        self.settings = settings
        self.base_url = "https://www.airbnb.com/api/v2/search_results"

    def scrape_listings(self):
        listings = []
        for location in self.settings["locations"]:
            params = {
                "location": location,
                "check_in": self.settings["check_in"],
                "check_out": self.settings["check_out"],
                "price_min": self.settings["price_min"],
                "price_max": self.settings["price_max"]
            }
            response = requests.get(self.base_url, params=params)
            data = response.json()

            for item in data["search_results"]:
                listing = self.parse_listing(item)
                listings.append(listing)
        return listings

    def parse_listing(self, item):
        return {
            "location": item["listing"]["location"]["city"],
            "price": item["pricing_quote"]["rate"]["amount"],
            "description": item["listing"]["description"],
            "amenities": item["listing"]["amenities"],
            "ratings": item["listing"]["star_rating"],
            "reviews": item["listing"]["reviews_count"],
            "check_in": self.settings["check_in"],
            "check_out": self.settings["check_out"]
        }