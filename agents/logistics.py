"""
agents/logistics.py
This agent handles the transportation logic.
It simulates finding a driver and negotiating a price.
"""

def find_driver(location):
    """
    Simulates searching for a driver in a specific location.
    
    Args:
        location (str): The location to search in (not used in mock, but good practice).
        
    Returns:
        dict: Details of the found driver and the transport cost.
    """
    # Mocking the process of finding a driver
    driver_name = "Raju"
    transport_cost = 500  # Flat rate in ₹ for the trip
    
    return {
        'driver_name': driver_name,
        'cost': transport_cost
    }
