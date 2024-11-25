# utils/helpers.py

import json


def load_map(file_path):
    """
    Load the map configuration from a JSON file.

    Expected JSON structure:
    {
        "regions": [
            {
                "name": "London",
                "type": "sea",
                "adjacent": ["North Sea", "Yorkshire", "Edinburgh"]
                // Add coordinates for rendering if necessary
            },
            // ... more regions
        ]
    }
    """
    with open(file_path, 'r') as f:
        map_data = json.load(f)
    return map_data
