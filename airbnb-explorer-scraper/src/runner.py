thonimport json
import os
from extractors.airbnb_parser import AirbnbParser
from outputs.data_exporter import DataExporter
from config.settings import Settings

def run_scraper():
    settings = Settings.load()

    parser = AirbnbParser(settings)
    listings = parser.scrape_listings()

    exporter = DataExporter(settings)
    exporter.export_data(listings)

if __name__ == "__main__":
    run_scraper()