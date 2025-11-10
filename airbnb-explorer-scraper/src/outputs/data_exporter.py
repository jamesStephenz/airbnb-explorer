thonimport json

class DataExporter:
    def __init__(self, settings):
        self.settings = settings
        self.output_dir = self.settings["output_dir"]

    def export_data(self, data):
        file_path = os.path.join(self.output_dir, "scraped_data.json")
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)