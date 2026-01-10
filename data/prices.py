"""
data/prices.py
This module acts as a mock database for crop prices.
It returns hardcoded values to simulate fetching data from a real market API.
"""

def get_crop_prices():
    """
    Returns a dictionary containing the name of the crop and its prices
    in the village (local market) and the city (destination market).
    """
    # In a real app, this would call an external API.
    return {
        'crop': 'Tomato',       # The crop we are analyzing
        'village_price': 15,    # Price per kg in the local village market (₹)
        'city_price': 40        # Price per kg in the city market (₹)
    }
