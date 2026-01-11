
import os
import sys
# Ensure we can find the config file if running from different directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from twilio.rest import Client
    import config
except ImportError:
    Client = None
    config = None

def generate_proposal_message(prices_data, profit_data):
    """
    Formats the proposal message asking for user confirmation.
    """
    crop = prices_data['crop']
    city_price = prices_data['city_price']
    load_kg = 50 
    
    total_gross_profit = profit_data['margin_per_kg'] * load_kg
    
    lines = []
    lines.append(f"Hi Ramesh, {crop.lower()} price in city is ₹{city_price}/kg.")
    lines.append(f"Potential extra earnings: ₹{total_gross_profit} (before transport).")
    lines.append("Reply YES to find a driver and book.")
        
    return "\n".join(lines)

def generate_confirmation_message(logistics_data):
    """
    Formats the final confirmation message.
    """
    lines = []
    lines.append(f"✅ Driver {logistics_data['driver_name']} confirmed!")
    lines.append(f"Pickup Cost: ₹{logistics_data['cost']}.")
    lines.append("They will arrive within 1 hour.")
    return "\n".join(lines)

def send_whatsapp_message(message_body):
    """
    Sends the generated message via Twilio WhatsApp API.
    """
    if not Client or not config:
        return "Error: Twilio library not installed or config.py missing."

    if config.TWILIO_ACCOUNT_SID == "AC_YOUR_ACCOUNT_SID_HERE":
        return "Error: Please update config.py with your actual Twilio credentials."

    try:
        client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            from_=config.TWILIO_WHATSAPP_NUMBER,
            body=message_body,
            to=config.USER_WHATSAPP_NUMBER
        )
        return f"Message sent! SID: {message.sid}"
    except Exception as e:
        return f"Failed to send message: {str(e)}"
