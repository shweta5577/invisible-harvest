"""
agents/analyst.py
This agent is responsible for analyzing the financial viability of selling the crop.
It calculates potential profit based on price differences.
"""

def calculate_profit(prices_data):
    """
    Calculates the profit per kg and determines if it meets the profitability threshold.
    
    Args:
        prices_data (dict): A dictionary containing 'city_price' and 'village_price'.

    Returns:
        dict: A dictionary with profit details and a boolean 'is_profitable' flag.
    """
    city_price = prices_data['city_price']
    village_price = prices_data['village_price']

    # Calculate gross profit margin per kg
    margin = city_price - village_price
    
    # Define our threshold for profitability (20% of village price)
    # If we make more than 20% on top of the base price, it's worth it.
    # (Example logic: user wants > 20% profit)
    profit_threshold = village_price * 0.20
    
    is_profitable = False
    if margin > profit_threshold:
        is_profitable = True
        
    return {
        'margin_per_kg': margin,       # How much we make per kg
        'is_profitable': is_profitable # YES/NO decision
    }
