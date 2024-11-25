

class Region:
    def __init__(self, name, region_type, adjacent, coordinates=None):
        self.name = name
        self.type = region_type  # 'land' or 'sea'
        self.adjacent = adjacent  # List of adjacent region names
        self.owner = None  # Player instance
        self.units = []  # List of Unit instances
        self.coordinates = coordinates  # For rendering purposes (optional)

class Board:
    def __init__(self, map_data):
        self.regions = {}
        self.load_regions(map_data)

    def load_regions(self, map_data):
        for region_info in map_data.get('regions', []):
            name = region_info['name']
            region_type = region_info['type']
            adjacent = region_info['adjacent']
            coordinates = region_info.get('coordinates')  # Optional
            self.regions[name] = Region(name, region_type, adjacent, coordinates)

    def get_region(self, region_name):
        return self.regions.get(region_name)

    def get_all_regions(self):
        return self.regions.values()
