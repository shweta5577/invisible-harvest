"""
agents/communicator.py
This agent is responsible for the final interaction with the user.
It takes all the analyzed data and formats a human-readable message.
"""

def generate_message(prices_data, profit_data, logistics_data):
    """
    Formats the final message to be sent to the farmer.
    
    Args:
        prices_data (dict): Contains crop name and prices.
        profit_data (dict): Contains margin logic.
        logistics_data (dict): Contains driver info and cost.
    """
    crop = prices_data['crop']
    city_price = prices_data['city_price']
    
    # Let's assume a standard load of 50kg for the total profit calculation example
    # (In a real app, this quantity would be input)
    load_kg = 50 
    
    total_gross_profit = profit_data['margin_per_kg'] * load_kg
    final_profit = total_gross_profit - logistics_data['cost']
    
    lines = []
    lines.append(f"Hi Ramesh, {crop.lower()} price in city is ₹{city_price}/kg.")
    # Only promise "extra" money if it's actually positive after transport!
    if final_profit > 0:
        lines.append(f"After transport, you can earn ₹{final_profit} extra on {load_kg}kg.")
        lines.append("Reply YES to book the driver.")
    else:
        lines.append("Profit is too low to cover transport costs.")
        
    return "\n".join(lines)
